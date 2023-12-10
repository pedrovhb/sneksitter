---
file: /home/pedro/Documents/chatgpt_export/Markdown/Explore Python Syntax Graphviz.md
heading_stack: <root> -> 5d11d6a6-248f-4f42-87c7-2cfeefdc5887 -> System -> 68c39207-346e-47cf-8c4c-5f153f2ac305 -> System -> aaa27992-bb31-4d04-9962-3478d816a032 -> User -> b6e4ecf9-36bd-4820-af58-e4a9f1f5464f -> Assistant -> 73685182-6dbf-42fb-b01f-65ae86e8c2ec -> Tool -> fba7b060-5569-45ff-8746-e0a25d230d1b -> Assistant -> cd968572-a4a2-4360-887a-120f08b7542f -> Tool -> 0163a4d5-f781-4253-ae6d-1f6b7a26924e -> Assistant -> aaa29628-f8f7-410e-b529-8c997524df22 -> User -> 0dd38e9b-4ebc-479f-b81b-40977ca36cd6 -> Assistant -> 9210ea39-cb8a-4240-9aa8-76d97f5c28af -> Tool -> 00dbaeba-6aed-455d-8e33-fd264ae3ac4e -> Assistant -> aaa2b441-f1df-40aa-88cf-b44a26423358 -> User -> 2cf213fe-d050-4421-8c66-02a043530734 -> Assistant -> 2cdb71f0-0e1f-4921-a8d3-3e9e1906acab -> Tool -> a3edaf30-99c0-4a46-a143-d91577190b12 -> Assistant -> 1fe8f69f-8617-4e0c-bc4e-d4ad44a23fe3 -> Assistant -> aaa27edf-4845-4899-9a38-ceaf1a5d7b5e -> User -> 96b436d5-d3b6-4f5d-b15b-1be00af5d5f2 -> Assistant -> ad084724-69b7-40b4-aecf-925b65dee6d0 -> Tool -> 64ff2b40-db69-4835-9788-7578f111f46f -> Assistant -> aaa217a8-ff5c-43d2-a014-6db1590ad616 -> User -> 6ded173f-4fd2-43ce-b01f-323ef6be8750 -> Assistant -> d0c92034-93f9-4197-8cdc-4d69c7e62459 -> Tool -> aaa2e2a0-b4eb-4a3c-9f31-f32a381933ca -> User -> 74802aec-7aef-4aa3-8aea-bea2923fbaad -> Assistant -> aaa2ca8f-0d98-4714-875a-5386fc48f859 -> User -> 6e64d9ae-d68c-4fc1-8a10-051543acd979 -> Assistant -> ae793d8f-e4d3-49c8-96a7-92f3fff4ba99 -> Tool -> fbabf230-e744-4690-ad63-eca029735b67 -> Assistant -> aaa22663-e915-48c4-bea7-373bfc8baa8b -> User -> 3e6567d5-9f63-4ad4-9d82-ffc5dcb63414 -> Assistant
---
# Assistant

```python
# Importing the necessary method to get the SQLite parser
from tree_sitter_languages import get_parser

# Initializing the SQLite parser
sqlite_parser = get_parser("sqlite")

# Exploring the syntax of SQLite by using the lookahead_iterator method
sqlite_lookahead_iterator_output = [(sqlite_parser.field_name_for_id(l), sqlite_parser.node_kind_for_id(l))
                                    for l in sqlite_parser.lookahead_iterator(1)]

sqlite_lookahead_iterator_output
```

[child ⬇️](#82ee9c8b-dd73-4204-a9c0-1f13781867c5)

---

(main branch ⎇)
###### 82ee9c8b-dd73-4204-a9c0-1f13781867c5
[parent ⬆️](#3e6567d5-9f63-4ad4-9d82-ffc5dcb63414)
