---
file: /home/pedro/Documents/chatgpt_export/Markdown/Graph Integration with Dataclasses.md
heading_stack: <root> -> d5ee1f8c-0262-460f-ae64-079de955da83 -> System -> 4df2c66a-be68-4ed7-939e-5244c07c0394 -> System -> aaa29239-053e-4660-afbe-53e2c8bdaf73 -> User -> 68e1c43a-7d95-419f-8a58-ed77216df416 -> Assistant -> Design Goals -> Components -> Node Class -> Edge Class
---
#### Edge Class
The Edge class will define connections between Nodes.

```python
from dataclasses import dataclass

@dataclass
class Edge:
    source: Node
    destination: Node
    weight: float = 1.0
```

