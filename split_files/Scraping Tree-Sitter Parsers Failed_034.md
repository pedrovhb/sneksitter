---
file: /home/pedro/Documents/chatgpt_export/Markdown/Scraping Tree-Sitter Parsers Failed.md
heading_stack: <root> -> d983c898-d843-48b2-8d19-e6358c6b3117 -> System -> e17b45cd-afd8-40ff-9f17-efd45736b653 -> System -> aaa20636-5e4b-4441-bb5f-bf9eba90dce2 -> User -> 432ed60e-ec95-40ea-b496-fd523a6dea8d -> Assistant -> 46b32ca1-24f5-4323-8f5d-f353801b264c -> Tool -> 5d6e7cb4-e20c-4759-95a6-070b010d5169 -> Assistant -> aeb33008-033e-4c51-9795-353210680c11 -> Tool -> 72a817b1-2783-48d4-bf78-8f9daa221f44 -> Assistant -> c73162e6-83db-48ae-8c00-9fd50a81c5af -> Tool -> 7da4ef10-11a0-4f4f-8aec-d157fe8b9927 -> Assistant -> 348e0146-9bb9-495d-b8c4-bde20485181c -> Tool -> 4f1f0651-482e-4cab-a55d-39df9816a94f -> Assistant -> 110fa627-9882-4cc6-8366-bb4269a99851 -> Tool -> d639a724-6245-4c34-ae81-2a1a7a238b1a -> Assistant -> 4cf1eff7-4257-4611-9cf2-67a51ee45ace -> Tool -> 5eb515b5-5e93-4d99-834e-48d5bdd44983 -> Assistant -> 511015e7-9298-47ab-9ff5-7b4680d8c3b2 -> Tool
---
# Tool

==== Cell ID: cb4f174f-0d62-4d93-b73c-ca08653c32c4
Cell Type: code
Cell State: finished_with_error
== Source ==
import asyncio
parsers = asyncio.run(fetch_tree_sitter_parsers())
parsers
== Output ==
```
{ 'ename': 'RuntimeError',
  'evalue': 'asyncio.run() cannot be called from a running event loop'}
```



[child ⬇️](#6723818c-93de-443d-a2f6-d6bfd8afa36c)

---

(main branch ⎇)
###### 6723818c-93de-443d-a2f6-d6bfd8afa36c
[parent ⬆️](#511015e7-9298-47ab-9ff5-7b4680d8c3b2)
