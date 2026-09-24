# Modern science-fiction book search

Research snapshot: 2026-09-24. Goal: 2,000 **book-length** science-fiction works first published in 1950 or later, with a redistributable free/open license. Short stories, podcast episodes, role-playing manuals, magazines, reviews about fiction, and multiple file formats of the same book do not count as separate books. A modern scan of an older book does not make the work post-1950.

## License boundary

For an **open-culture** torrent, accept rights-holder-authorized CC0, CC BY, CC BY-SA, or an equivalent license that allows copying, adaptation, and commercial use. Creative Commons [distinguishes these from its NC and ND licenses](https://creativecommons.org/public-domain/freeworks/). CC BY-NC, CC BY-NC-SA, and CC BY-NC-ND can allow noncommercial redistribution, but belong in a separately named **restricted redistribution** collection if we decide to host them. “Free to read,” “free download,” and an open license on a *review or catalog record* do not license the underlying novel.

Every book requires an edition-level check of the author/publisher's rights statement, the actual downloadable file (including cover and art), publication date, genre, length, license version, and attribution. A catalog hit is a lead, not permission. [open-leads.json](open-leads.json) contains six promising book-level leads with primary rights pages; none is yet approved for a torrent.

## Scale check

I queried the [Internet Archive advanced-search API](https://archive.org/advancedsearch.php?q=mediatype%3Atexts%20AND%20subject%3A%22science%20fiction%22%20AND%20licenseurl%3A%2A%20AND%20year%3A%5B1950%20TO%202026%5D&rows=0&output=json) for `mediatype:texts AND subject:"science fiction" AND licenseurl:* AND year:[1950 TO 2026]`. It returned **1,576 records**, before deduplication or rights review. Of these, **73** had CC BY or CC BY-SA metadata, **169** CC0 metadata, **983** NC/ND metadata, **349** public-domain marks, and **2** other labels. This is one search slice, not an estimate of all open science fiction. Metadata can be wrong: the same result set marks a copy of *Dune* as public domain. Neither that mark nor a CC license on a search result is enough to include a book.

[Unglue.it](https://unglue.it/free/) is more useful for individually released books because some records state that the rights holder released the ebook under a named CC license. The six leads below come from such records and an author book page. Its science-fiction facet also mixes public-domain classics and several formats of the same work, so a facet count cannot be treated as a book count.

## Book-level leads

| Work | First publication / language | Open-license evidence | Review remaining |
| --- | --- | --- | --- |
| [Green Comet](https://unglue.it/work/128673/) | 2012 / en | Rights-holder release, CC BY-SA 4.0 | Inspect offered file and embedded credits. |
| [Parasite Puppeteers](https://unglue.it/work/146704/) | 2015 / en | Rights-holder release, CC BY-SA 4.0 | Inspect offered file and embedded credits. |
| [The Francesians](https://unglue.it/work/226428/) | 2017 / en | Rights-holder release, CC BY-SA 4.0 | Inspect offered file and embedded credits. |
| [House of Refuge](https://unglue.it/work/144855/) | 2014 / en | Rights-holder release, CC BY-SA | Confirm exact version and all file elements. |
| [Biodigital](https://unglue.it/work/136615/) | 2014 / en | Rights-holder release, CC BY-SA | Confirm exact version and distinguish it from the earlier *Acts of the Apostles*. |
| [The Relay](https://www.after-certainty.com/explore/books/the-relay) | 2026 / en | Author's book page says CC BY-SA and offers EPUB/PDF/DOCX | Confirm exact version, complete text, and file credits. |

Other promising discovery sources: [Lizzie Crowdagger's French fiction repository](https://github.com/crowdagger/textes) states CC BY-SA 4.0 and includes novels, novellas, and short stories; each book must be classified individually. [Free Speculative Fiction Online](https://freesfonline.net/AdvancedSearch.html) has a CC filter but principally indexes stories and links, not rights evidence. The [SCP Foundation's licensing guide](https://scp-wiki.wikidot.com/licensing-guide) permits CC BY-SA 3.0 compilations, but its articles are individual stories and some images need separate checks. These sources do not currently establish 2,000 books.

## Restricted redistribution leads, excluded from the open count

- [Peter Watts's backlist](https://www.rifters.com/real/shorts.htm) allows noncommercial copying of his novels, with no alteration of his prose.
- [Cory Doctorow's books](https://wiki.creativecommons.org/wiki/Case_Studies/Cory_Doctorow) commonly use CC BY-NC-SA or CC BY-NC-ND; check each edition.
- [Rudy Rucker's *Ware Tetralogy*](https://www.rudyrucker.com/wares/cc_downloads/) uses CC BY-NC-ND. Four novels are bundled into one download, not four separately licensed files by assumption.
- [Charles Stross's *Accelerando*](https://wiki.creativecommons.org/wiki/Accelerando) uses CC BY-NC-ND 2.5.

**Current result:** six book-level open leads, zero pack-ready science-fiction books, and no credible route yet to 2,000 post-1950 full-length open-license books. The next step is to verify and package the small primary-source set while continuing discovery; reaching 2,000 may require a broader definition that includes individually licensed short fiction or non-open NC/ND titles, each in its own accurately labelled collection.
