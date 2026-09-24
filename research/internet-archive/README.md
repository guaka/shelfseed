# Internet Archive book torrents

ShelfSeed can point readers to Internet Archive (IA) torrents that already exist. This is a **live external index**, not a ShelfSeed bundle or a mirror. The links below query IA for text items with its `Archive BitTorrent` format. Search results can change; open an item's page and use its current **TORRENT** download option. IA [documents this search filter and its item torrents](https://archivesupport.zendesk.com/hc/en-us/articles/360004715251-Archive-BitTorrents).

## Browse

- [All IA text items with torrents](https://archive.org/search?query=mediatype%3Atexts%20AND%20format%3A%22Archive%20BitTorrent%22)
- [Children's books with torrents](https://archive.org/search?query=mediatype%3Atexts%20AND%20format%3A%22Archive%20BitTorrent%22%20AND%20subject%3A%22children%22)
- [Science fiction with torrents](https://archive.org/search?query=mediatype%3Atexts%20AND%20format%3A%22Archive%20BitTorrent%22%20AND%20subject%3A%22science%20fiction%22)
- [Portuguese](https://archive.org/search?query=mediatype%3Atexts%20AND%20format%3A%22Archive%20BitTorrent%22%20AND%20language%3A%22Portuguese%22) · [German](https://archive.org/search?query=mediatype%3Atexts%20AND%20format%3A%22Archive%20BitTorrent%22%20AND%20language%3A%22German%22) · [French](https://archive.org/search?query=mediatype%3Atexts%20AND%20format%3A%22Archive%20BitTorrent%22%20AND%20language%3A%22French%22) · [Spanish](https://archive.org/search?query=mediatype%3Atexts%20AND%20format%3A%22Archive%20BitTorrent%22%20AND%20language%3A%22Spanish%22) · [Dutch](https://archive.org/search?query=mediatype%3Atexts%20AND%20format%3A%22Archive%20BitTorrent%22%20AND%20language%3A%22Dutch%22)

The language and subject filters use uploader metadata. They do not distinguish European from Brazilian Portuguese, establish an age range, or prove genre. Refine the search on IA, then check each item.

## How ShelfSeed records an IA link

For a reviewed listing, store the IA identifier, item URL, current `.torrent` URL, title, language/variant, intended audience, rights statement and its evidence URL, and the date checked. Label it `external-ia-torrent`. Use the actual torrent filename shown in the item's download list or [metadata API](https://archive.org/developers/metadata-schema/index.html), not a guessed filename. If a torrent disappears or becomes stale, link to the item page while the listing is checked again. IA says item updates can make old torrents obsolete, so links should lead to the current item whenever possible.

An IA torrent may contain multiple files and derivatives, not just one book. Torrent availability and a permissive metadata tag are not rights clearance. Browse links above include material outside ShelfSeed's open-license criteria. A listing labeled **reviewed open** needs evidence for the actual text, translation, illustrations, and edition; otherwise label it **unreviewed IA index**. An IA torrent stays under IA's own identifier and infohash and does not consume a ShelfSeed pack number or change a ShelfSeed catalog revision.
