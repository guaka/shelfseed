# Book bundle releases

External torrent indexes, such as [Internet Archive book torrents](research/internet-archive/README.md), are links to another host's existing items. They are tracked separately from ShelfSeed packs and do not trigger a catalog revision when IA adds or updates an item.

## Names and versions

- A **pack** is an immutable torrent payload. Its ID includes collection, rights class, and a sequence number, for example `shelfseed-children-cc-by-4.0-pack-001`. A pack number never denotes a complete snapshot.
- A **catalog revision** (`r0001`, `r0002`, …) lists the active packs and editions that together make up the current collection. Publish a new revision only when a reviewed batch or correction is ready. Record the publication date separately; there is no fixed cadence.
- `latest.json` may point to the current catalog revision after publication. Keep every numbered catalog revision immutable.
- Never replace a torrent or reuse its pack ID after its bytes change. Publish a new pack and record the old edition as superseded or removed in the next catalog revision.

Example: `r0001` lists packs 001 for CC BY 4.0 and 001 for a separately reviewed public-domain jurisdiction. A later `r0002` can add CC BY pack 002 and remove one edition from the active catalog without redistributing pack 001.

## Required record for each edition

Record a stable source edition ID; title; creators and translators where available; language **variant**; reading level or reviewed age range; source landing page and exact download URL; license and rights evidence; local filename, byte count, and SHA-256 digest. Count translated editions separately, but deduplicate the same edition and file within each language. Do not infer `pt-PT` from generic Portuguese or `pt-BR` metadata. Do not assign ages 10–15 from a reading-level number alone.

The release catalog also records each pack's torrent infohash, torrent-file SHA-256, file count, total bytes, release date, changes since the preceding revision, and any superseded or removed edition IDs. Keep attribution and copyright notices inside the files; put a human-readable attribution index in each pack.

## Rights and corrections

Use one rights class per pack, with exact version for Creative Commons licenses. Public domain is jurisdiction-dependent: record the jurisdiction, author/translator/illustrator dates as needed, and the evidence for **this edition** before inclusion. Do not treat a Project Gutenberg “public domain in the USA” notice as worldwide clearance. Review covers, illustrations, translations, and scans as well as text.

A torrent cannot be recalled. On a rights or quality correction, remove the affected edition from the current catalog, stop seeding the affected pack where possible, and publish a replacement or notice. Previous catalog revisions remain historical records, not recommendations to seed withdrawn content. Smaller packs limit the number of unrelated files affected by such a correction.

The first draft has no published catalog revision or `latest.json`; its pack number is a proposed ID. Publish `r0001` only after the desired first batch and rights review are complete.
