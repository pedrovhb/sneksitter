---
file: /home/pedro/Documents/chatgpt_export/Markdown/Usearch Setup and Testing.md
heading_stack: <root> -> 736a6f35-0c3a-4def-8e5f-fb433283b0a3 -> System -> 7e1fc11a-385d-4641-83a5-24bcd0f772a6 -> System -> aaa28f28-7a3d-4adc-9c31-2e24b825ee2c -> User -> 431e417f-ba17-4c71-8651-4bb4fc005b8a -> Assistant -> 5efa9536-227a-4097-a943-8a062fa36ebb -> Tool -> 0125b662-4281-4b16-a7df-c31bce9c8ddd -> Assistant -> bbb603db-a333-4ce8-90a2-a060fe0913fe -> Tool -> e359e771-2ded-442d-84dd-9197c84f3a10 -> Assistant -> 52917e86-ff86-4af7-b631-331103ecd0ba -> Tool -> faa2d1e3-8ba1-40f7-bb9b-0529d8b66d9b -> Assistant -> eedb56d6-43ee-4b2a-bab7-b0a66cd5e743 -> Tool -> ede47510-19d2-4507-9e28-e101779dfc56 -> Assistant -> d36982cb-1dff-408e-a3e2-7ebbd9651f28 -> Tool -> 80c4522b-cbf5-44a7-a234-be8818417cee -> Assistant
---
# Assistant

{
  "file_id": "bd307b66-5e95-434a-9ff2-d2599b457e0c",
  "cell_type": "code",
  "source": [
    "import numpy as np",
    "from usearch.index import Index",
    "",
    "index = Index(",
    "    ndim=3,",
    "    metric='cos',",
    "    dtype='f32',",
    "    connectivity=16,",
    "    expansion_add=128,",
    "    expansion_search=64,",
    ")",
    "",
    "vector = np.array([0.2, 0.6, 0.4])",
    "index.add(42, vector)",
    "matches = index.search(vector, 10)",
    "",
    "assert len(index) == 1",
    "assert len(matches) == 1",
    "assert matches[0].key == 42",
    "assert matches[0].distance <= 0.001",
    "assert np.allclose(index[42], vector)"
  ]
}

[child ⬇️](#f9a4c4b4-dd9b-4aa5-a44d-8261813f74eb)

---

(main branch ⎇)
###### f9a4c4b4-dd9b-4aa5-a44d-8261813f74eb
[parent ⬆️](#80c4522b-cbf5-44a7-a234-be8818417cee)
