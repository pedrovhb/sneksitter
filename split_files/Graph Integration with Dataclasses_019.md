---
file: /home/pedro/Documents/chatgpt_export/Markdown/Graph Integration with Dataclasses.md
heading_stack: <root> -> d5ee1f8c-0262-460f-ae64-079de955da83 -> System -> 4df2c66a-be68-4ed7-939e-5244c07c0394 -> System -> aaa29239-053e-4660-afbe-53e2c8bdaf73 -> User -> 68e1c43a-7d95-419f-8a58-ed77216df416 -> Assistant -> Design Goals -> Components -> Node Class -> Edge Class -> Graph Class -> Observers -> Complete Example -> aaa2b8c0-61e3-452c-ab9f-729395a2d79c -> User -> 14a21363-9c4f-4d33-b7f1-3eca1e79d29c -> Assistant
---
# Assistant

```python
from dataclasses import dataclass, field, fields
from typing import List, Optional
import networkx as nx

# Define the Node dataclass
@dataclass
class Node:
    name: str
    id: int = field(default_factory=int)

# Define the Edge dataclass
@dataclass
class Edge:
    source: Node
    destination: Node
    weight: float = 1.0

# Define the Graph class
class Graph:
    def __init__(self):
        self.graph = nx.Graph()
        
    def add_node(self, node: Node):
        self.graph.add_node(node.id, data=node)
        
    def add_edge(self, edge: Edge):
        self.graph.add_edge(edge.source.id, edge.destination.id, weight=edge.weight)

    def neighbors(self, node: Node) -> List[Node]:
        return [self.graph.nodes[n]['data'] for n in self.graph.neighbors(node.id)]

    def __getattr__(self, name):
        if name == 'friends':
            def wrapper(node: Node) -> List[Node]:
                return self.neighbors(node)
            return wrapper

# Example usage
node1 = Node(name="Alice", id=1)
node2 = Node(name="Bob", id=2)
node3 = Node(name="Charlie", id=3)
edge1 = Edge(source=node1, destination=node2)
edge2 = Edge(source=node1, destination=node3)

graph = Graph()
graph.add_node(node1)
graph.add_node(node2)
graph.add_node(node3)
graph.add_edge(edge1)
graph.add_edge(edge2)

# Retrieve neighbors of node1 using attribute-style access 'friends'
friends_of_node1 = graph.friends(node1)
friends_of_node1
```

[child ⬇️](#4a5e2a3f-ac57-4e0e-9048-1f1fc82073aa)

---

(main branch ⎇)
###### 4a5e2a3f-ac57-4e0e-9048-1f1fc82073aa
[parent ⬆️](#14a21363-9c4f-4d33-b7f1-3eca1e79d29c)
