---
file: /home/pedro/Documents/chatgpt_export/Markdown/Graph Integration with Dataclasses.md
heading_stack: <root> -> d5ee1f8c-0262-460f-ae64-079de955da83 -> System -> 4df2c66a-be68-4ed7-939e-5244c07c0394 -> System -> aaa29239-053e-4660-afbe-53e2c8bdaf73 -> User -> 68e1c43a-7d95-419f-8a58-ed77216df416 -> Assistant -> Design Goals -> Components -> Node Class -> Edge Class -> Graph Class -> Observers -> Complete Example
---
### Complete Example

Here's a simple example integrating all the components:

```python
from dataclasses import dataclass, field
import networkx as nx

@dataclass
class Node:
    name: str
    id: int = field(default_factory=int)

@dataclass
class Edge:
    source: Node
    destination: Node
    weight: float = 1.0

class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node: Node):
        self.graph.add_node(node.id, data=node)

    def add_edge(self, edge: Edge):
        self.graph.add_edge(edge.source.id, edge.destination.id, weight=edge.weight)

    def neighbors(self, node: Node):
        return [self.graph.nodes[n]['data'] for n in self.graph.neighbors(node.id)]

# Example Usage
node1 = Node(name="A", id=1)
node2 = Node(name="B", id=2)
edge = Edge(source=node1, destination=node2)

graph = Graph()
graph.add_node(node1)
graph.add_node(node2)
graph.add_edge(edge)

print(graph.neighbors(node1))
```

This is a basic version; we can add more advanced features like traversal methods, validation, etc. Would you like to proceed with that?

[child ⬇️](#aaa2b8c0-61e3-452c-ab9f-729395a2d79c)

---

(main branch ⎇)
###### aaa2b8c0-61e3-452c-ab9f-729395a2d79c
[parent ⬆️](#68e1c43a-7d95-419f-8a58-ed77216df416)
