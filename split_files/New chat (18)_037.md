---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (18).md
heading_stack: <root> -> 63d1e0db-b84d-4b93-8cac-dcde4fb27d2f -> System -> e1231b1e-c6dd-4e6f-8b11-b07e97b45e65 -> System -> aaa242ce-7fcb-4865-bc06-4b38eb8a2fdd -> User -> 95861e20-24b9-49e9-be62-3c256f5e4720 -> Assistant -> aaa20b0d-2bf8-44e9-9467-b40ac5f514ca -> User -> fbe3cdf8-7d59-4d9c-bfdf-8e131d0c5d7c -> Assistant -> aaa28153-7531-404e-9050-98ddff7f1b25 -> User -> d1bfe94e-e0ff-4c69-a1e4-1db1fb06b009 -> Assistant -> aaa2f9b6-b863-4dda-ba08-c7b20cbbbd63 -> User -> 57f72327-baa2-4d25-9b9f-a877fb819b45 -> Assistant -> aaa23cf9-02b0-4c09-a436-9617da42d7ba -> User -> fb6d51ea-c303-4e3a-851e-28bc4d04b2d4 -> Assistant -> aaa22696-a2af-4732-8f32-322df1189d1b -> User -> bd5f736d-fc24-4825-a46a-4a1acb74119d -> Assistant -> Context Analysis -> Challenges and Possible Approaches -> Possible Approaches -> aaa24e35-6533-426b-a08b-88343ed584f3 -> User -> c6ce9189-ab31-4647-978b-3fa638dc6661 -> Assistant -> Concrete Plan: Finite State Machine (FSM) + Depth-First Traversal -> States
---
#### States

1. `START`: Initial state before any parameter is processed.
2. `POSITIONAL_ONLY`: After encountering `/`, all parameters must be positional-only.
3. `VARARGS`: After encountering `*args` or `*`, which implies that subsequent parameters should be keyword-only.
4. `KWARGS`: After encountering `**kwargs`.

