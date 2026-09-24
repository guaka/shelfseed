# CC BY 4.0 children's pack 001 — draft

This pilot contains four unmodified PDF editions from the Global Digital Library, whose API marks each as `CC-BY-4.0`. The PDFs contain their own StoryWeaver attribution and license pages. The external [ATTRIBUTION.md](ATTRIBUTION.md) is copied into the torrent payload as an index; it does not replace those pages. [pack.json](pack.json) pins the exact source URLs and SHA-256 digests.

To build locally with Python 3:

```sh
python3 tools/build_pack.py drafts/children/cc-by-4.0/pack.json --download
python3 tools/build_pack.py drafts/children/cc-by-4.0/pack.json
```

The builder refuses a changed or missing file. The payload is ignored by Git; the `.torrent`, manifest, attribution index, and builder are committed. The `.torrent` has no tracker or private flag and can use public DHT. Its v1 infohash is `72fec02beaf6e44a0f7d77728ebedb308a569592`; the torrent file's SHA-256 is `cbe5ab0f365fb326e2e89926b3c7584f5372179890439c6365adbb6eb059608a`. This is a technical draft, not an announced torrent or a 2,000-book release.

Current coverage: English, French, Spanish (Spain), and Portuguese (Brazil). Dutch, Portuguese (Portugal), German, comics, and confirmed ages 10–15 need separately checked source editions before inclusion. The French web book is an educational title; the others are science/nature reading. The PDF itself describes the source reading level as Level 3; that does not establish a 10–15 age rating.

Source and rights policy: [GDL API](https://content.digitallibrary.io/api/), [GDL license policy](https://content.digitallibrary.io/license/), and [StoryWeaver attribution guidelines](https://storyweaver.org.in/or/attributions).
