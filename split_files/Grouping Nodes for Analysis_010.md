---
file: /home/pedro/Documents/chatgpt_export/Markdown/Grouping Nodes for Analysis.md
heading_stack: <root> -> 6db24c38-564f-43d4-b8c9-2fec4e4db353 -> System -> 2953287f-20e5-44fb-a584-4bfe4f961bbb -> System -> aaa23f50-fb72-4433-a7f7-075d9fdfe0f3 -> User -> b5e935e4-8ecf-4850-ac07-4d63ba79b17e -> Assistant -> ad08acfc-210e-4de6-8495-802cfd6644c0 -> Assistant
---
# Assistant

```python
from collections import defaultdict
from typing import List, Tuple

# Dummy class to simulate the Node object in the example.
class Node:
    def __init__(self, type: str, start_point: Tuple[int, int], end_point: Tuple[int, int]):
        self.type = type
        self.start_point = start_point
        self.end_point = end_point

# Dummy data to simulate the provided output.
nodes = [
    Node("call", (2, 1), (2, 26)), Node("identifier", (2, 1), (2, 10)),
    Node("argument_list", (2, 10), (2, 26)), Node("identifier", (3, 1), (3, 11)),
    Node("identifier", (3, 1), (3, 11)), Node("function_definition", (4, 0), (31, 58)),
    Node("identifier", (4, 4), (4, 20)), Node("parameters", (4, 20), (4, 66)),
    Node("identifier", (4, 21), (4, 29)), Node("type", (4, 31), (4, 34))
]

node_groups = defaultdict(list)

for node in nodes:
    key = (node.type, node.start_point)
    node_groups[key].append(node)

node_groups
```

[child ⬇️](#58d33044-a31f-4722-880d-41adf2e0d2e9)

---

(main branch ⎇)
###### 58d33044-a31f-4722-880d-41adf2e0d2e9
[parent ⬆️](#ad08acfc-210e-4de6-8495-802cfd6644c0)
