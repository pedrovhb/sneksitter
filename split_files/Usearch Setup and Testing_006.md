---
file: /home/pedro/Documents/chatgpt_export/Markdown/Usearch Setup and Testing.md
heading_stack: <root> -> 736a6f35-0c3a-4def-8e5f-fb433283b0a3 -> System -> 7e1fc11a-385d-4641-83a5-24bcd0f772a6 -> System -> aaa28f28-7a3d-4adc-9c31-2e24b825ee2c -> User
---
# User

Please create a notebook and set up usearch as such:

$ pip install usearch

import numpy as np
from usearch.index import Index

index = Index(
    ndim=3, # Define the number of dimensions in input vectors
    metric='cos', # Choose 'l2sq', 'haversine' or other metric, default = 'ip'
    dtype='f32', # Quantize to 'f16' or 'i8' if needed, default = 'f32'
    connectivity=16, # Optional: How frequent should the connections in the graph be
    expansion_add=128, # Optional: Control the recall of indexing
    expansion_search=64, # Optional: Control the quality of search
)

vector = np.array([0.2, 0.6, 0.4])
index.add(42, vector)
matches = index.search(vector, 10)

assert len(index) == 1
assert len(matches) == 1
assert matches[0].key == 42
assert matches[0].distance <= 0.001
assert np.allclose(index[42], vector)

[child ⬇️](#431e417f-ba17-4c71-8651-4bb4fc005b8a)

---

(main branch ⎇)
###### 431e417f-ba17-4c71-8651-4bb4fc005b8a
[parent ⬆️](#aaa28f28-7a3d-4adc-9c31-2e24b825ee2c)
