---
file: /home/pedro/Documents/chatgpt_export/Markdown/Graph Integration with Dataclasses.md
heading_stack: <root> -> d5ee1f8c-0262-460f-ae64-079de955da83 -> System -> 4df2c66a-be68-4ed7-939e-5244c07c0394 -> System -> aaa29239-053e-4660-afbe-53e2c8bdaf73 -> User -> 68e1c43a-7d95-419f-8a58-ed77216df416 -> Assistant -> Design Goals -> Components -> Node Class -> Edge Class -> Graph Class
---
#### Graph Class
The Graph class will encapsulate a `networkx.Graph` object and offer additional methods for traversal and management.

```python
import networkx as nx

class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node: Node):
        self.graph.add_node(node.id, data=node)

    def add_edge(self, edge: Edge):
        self.graph.add_edge(edge.source.id, edge.destination.id, weight=edge.weight)

    def neighbors(self, node: Node):
        return [self.graph.nodes[n]['data'] for n in self.graph.neighbors(node.id)]
```

