---
file: /home/pedro/Documents/chatgpt_export/Markdown/Setup Tree-sitter Python parser.md
heading_stack: <root> -> 48404b29-4887-462e-acd5-c1ecf0317fbf -> System -> 116c69b9-0217-4c43-bedc-42dcbf0f826d -> System -> aaa2b2b9-a972-49a4-8072-387253454bc2 -> User -> 65ebe623-cb59-4071-a891-b0ecac4a7299 -> Assistant -> 3b9d8f44-31ea-4a18-a85c-2144c2c1c659 -> Tool -> 74a3cf29-c1fc-4242-817b-f8e9f83315ef -> Assistant -> 8801ae9a-ded1-475a-a3e9-bd817697ad99 -> Tool -> 133fb8b4-7853-4484-b203-3efbc6ed24b1 -> Assistant -> aaa293e9-a16a-4dcb-bf1e-e1a857731e97 -> User -> 953ccdca-be2f-4765-bdf5-13151dff1986 -> Assistant -> 9f67d0a5-d0f4-44e9-8fa7-40963c60e88f -> Tool -> 4dc004ce-1401-4ffc-871d-bd967d2f63a9 -> Assistant -> 99984851-9314-483f-a2a3-126c895dec19 -> Assistant -> da744ba2-ecd2-4dc0-8655-fa8aaee2bf9b -> Tool -> 15f61e74-54fd-47d9-8008-f0d889bf12b7 -> Assistant -> aaa2d60b-338e-4152-9e50-83b6a20eff30 -> User -> de6b35bd-5bff-4de0-95b8-221d8d435c40 -> Assistant -> 4cdff389-2396-4ab1-be1d-8b1b82078b94 -> Tool -> 4cb279b0-a577-45ef-94ca-c4387df6dbab -> Assistant -> aaa2cde9-4bc5-421a-8b93-1227a5b142ce -> User -> 08eb7667-59b0-4428-bac9-03470a3c43e9 -> Assistant -> da0e3adc-f279-4bb0-8190-f613e2c89c6f -> Tool -> ea4b757d-c12b-4ea8-9576-483fac3d32d7 -> Assistant -> aaa2fadc-e768-42c3-8f1d-1e2175896635 -> User -> 0ca77f9c-ecfc-4df4-be6b-ec2c96eb4460 -> Assistant -> aaa2bf74-6601-4af7-bc2d-ab12017d2dac -> User -> 0eaa25f5-df9f-4760-8870-6c10e86e7b93 -> Assistant -> Base Classes and Data Models -> Builder Pattern -> Idiomatic Use -> Query Serialization -> Support for Complex Queries -> Convenience Functions -> DSL-like Experience -> Trade-offs and Considerations -> Conclusion -> aaa29063-77a1-4d2e-bd50-f6ee519da7f6 -> User -> e05fc06a-8b75-42da-b78a-c76514e42642 -> Assistant -> Basic Building Blocks -> Dataclasses for Basic Blocks -> Builder Pattern -> QueryBuilder Class -> Composing Complex Queries -> Example Usage -> Extending for Advanced Features -> Validating Queries -> Type Safety and Intellisense -> Summary -> aaa293aa-2e35-42a9-975e-2c60025c5c81 -> User -> e39c17cd-eb8c-44f0-921c-f747f586900f -> Assistant -> Hypothetical Usage -> API Design -> Node Construction and Capture -> Field Qualification -> Grouping and Nesting -> Anchors and Wildcards -> Predicates -> Data Structures -> Query Builder Class -> Query Validation and Building -> Summary -> aaa22527-f7af-4d58-9cde-1ff0cf27b18f -> User -> acf2e97a-76ad-4094-9e62-d942f0e2cf8f -> Assistant -> Design Goals -> Hypothetical Simplified Usage -> Simplified API Methods -> Summary -> aaa2563a-66a4-4475-8293-82669e9d763d -> User -> 20e49cad-e7d1-4e3e-bfdd-aff5bb96a9d0 -> Assistant -> Libraries for Inspiration -> Refined Hypothetical Usage with Magic Methods -> Proposed API Changes -> Summary -> aaa26d41-a02f-47e2-a819-7027c91eda12 -> User -> 31472c16-5be9-4094-9f8b-b88d11caf2a4 -> Assistant -> 1. Pandas
---
### 1. Pandas

Pandas DataFrame API is quite powerful and allows for complex queries in an intuitive manner.

#### Simple Example
Selecting a column by name:
```python
df['column_name']
```

#### Advanced Example
Applying lambda functions as predicates:
```python
df[df['column_name'].apply(lambda x: x > 5)]
```

