#!/usr/bin/env python3
"""Verify a pinned book pack and write deterministic BitTorrent v1 metadata."""

import argparse
import hashlib
import json
import re
import sys
import urllib.request
from pathlib import Path


def bencode(value):
    if isinstance(value, int):
        return b"i" + str(value).encode("ascii") + b"e"
    if isinstance(value, str):
        value = value.encode("utf-8")
    if isinstance(value, bytes):
        return str(len(value)).encode("ascii") + b":" + value
    if isinstance(value, list):
        return b"l" + b"".join(bencode(item) for item in value) + b"e"
    if isinstance(value, dict):
        return b"d" + b"".join(
            bencode(key) + bencode(value[key]) for key in sorted(value)
        ) + b"e"
    raise TypeError(f"cannot bencode {type(value).__name__}")


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def validate_file(path, book):
    if not path.is_file():
        raise ValueError(f"missing {path}; run again with --download")
    if path.stat().st_size != book["bytes"] or sha256(path) != book["sha256"]:
        raise ValueError(f"size or SHA-256 mismatch: {path}")
    if path.suffix.lower() == ".pdf" and path.open("rb").read(5) != b"%PDF-":
        raise ValueError(f"not a PDF: {path}")


def download(path, book):
    if path.exists():
        return
    url = book["source_url"]
    if not url.startswith("https://"):
        raise ValueError(f"HTTPS source required: {url}")
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".partial")
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "ShelfSeed/0.1"})
        with urllib.request.urlopen(request, timeout=60) as response, tmp.open("wb") as out:
            while block := response.read(1024 * 1024):
                out.write(block)
        validate_file(tmp, book)
        tmp.replace(path)
    finally:
        tmp.unlink(missing_ok=True)


def build(manifest_path, should_download=False, check_only=False):
    manifest_path = manifest_path.resolve()
    pack_dir = manifest_path.parent
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    pack_id = data["pack_id"]
    if data["schema"] != 1 or not re.fullmatch(r"[a-z0-9][a-z0-9.-]+-pack-[0-9]{3,}", pack_id):
        raise ValueError("unsupported schema or unsafe pack ID")
    if not data["license"] or not data["books"]:
        raise ValueError("pack must have a license and at least one book")
    piece_length = data["piece_length"]
    if piece_length < 16384 or piece_length & (piece_length - 1):
        raise ValueError("piece length must be a power of two, at least 16 KiB")

    root = pack_dir / "payload" / pack_id
    root.mkdir(parents=True, exist_ok=True)
    names = set()
    for book in data["books"]:
        name = book["file"]
        if Path(name).name != name or name in names or name == "ATTRIBUTION.md":
            raise ValueError(f"duplicate or unsafe filename: {name}")
        names.add(name)
        path = root / name
        if should_download:
            download(path, book)
        validate_file(path, book)

    attribution = (pack_dir / "ATTRIBUTION.md").read_bytes()
    (root / "ATTRIBUTION.md").write_bytes(attribution)
    files = sorted(root.iterdir(), key=lambda p: p.name.encode("utf-8"))
    expected = names | {"ATTRIBUTION.md"}
    if {p.name for p in files} != expected or any(not p.is_file() for p in files):
        raise ValueError("payload contains files not listed in the manifest")

    # BitTorrent v1 hashes the concatenation of files in the info dictionary's order.
    file_entries = []
    piece_hashes = bytearray()
    pending = bytearray()
    total_bytes = 0
    for path in files:
        size = path.stat().st_size
        file_entries.append({"length": size, "path": [path.name]})
        total_bytes += size
        with path.open("rb") as stream:
            while block := stream.read(1024 * 1024):
                pending.extend(block)
                while len(pending) >= piece_length:
                    piece_hashes.extend(hashlib.sha1(pending[:piece_length]).digest())
                    del pending[:piece_length]
    if pending:
        piece_hashes.extend(hashlib.sha1(pending).digest())
    info = {
        "files": file_entries,
        "name": pack_id,
        "piece length": piece_length,
        "pieces": bytes(piece_hashes),
    }
    torrent = bencode({"info": info})
    output = pack_dir / f"pack-{pack_id.rsplit('-pack-', 1)[1]}.torrent"
    if check_only:
        if not output.is_file() or output.read_bytes() != torrent:
            raise ValueError(f"torrent metadata mismatch: {output}")
    else:
        output.write_bytes(torrent)
    print(f"{pack_id}: {len(data['books'])} editions, {total_bytes} payload bytes")
    print(f"infohash (v1): {hashlib.sha1(bencode(info)).hexdigest()}")
    print(f"torrent SHA-256: {hashlib.sha256(torrent).hexdigest()}")
    print(f"torrent: {output}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--download", action="store_true", help="fetch missing pinned files")
    parser.add_argument("--check", action="store_true", help="verify committed torrent bytes")
    args = parser.parse_args()
    try:
        build(args.manifest, args.download, args.check)
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
