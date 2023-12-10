---
file: /home/pedro/Documents/chatgpt_export/Markdown/Graph Integration with Dataclasses.md
heading_stack: <root> -> d5ee1f8c-0262-460f-ae64-079de955da83 -> System -> 4df2c66a-be68-4ed7-939e-5244c07c0394 -> System -> aaa29239-053e-4660-afbe-53e2c8bdaf73 -> User -> 68e1c43a-7d95-419f-8a58-ed77216df416 -> Assistant -> Design Goals -> Components -> Node Class -> Edge Class -> Graph Class -> Observers -> Complete Example -> aaa2b8c0-61e3-452c-ab9f-729395a2d79c -> User -> 14a21363-9c4f-4d33-b7f1-3eca1e79d29c -> Assistant -> 4a5e2a3f-ac57-4e0e-9048-1f1fc82073aa -> Tool -> cea21ee6-1cb1-4fc6-b2ce-a82138645c80 -> Assistant -> aaa27cc4-8bab-410d-ba5e-040a093984ca -> User -> 37c8a936-a17b-4aef-a851-5c1dcd876078 -> Assistant -> c2f8ec96-a0e5-4ab6-b956-27ce1c9ddadd -> Tool -> 5ff5e072-3745-44c8-84b6-675d749b9c35 -> Assistant -> c3de0a80-97f4-4421-8dd9-84f565e6d762 -> Assistant
---
# Assistant

```python
from dataclasses import dataclass, field, fields
from typing import List, TypeVar, Generic, Type, Any
import networkx as nx

# Define type variables for Node and Edge
NodeT = TypeVar('NodeT', bound='Node')
EdgeT = TypeVar('EdgeT', bound='Edge')

# Define metaclass for Graph
class GraphMeta(type):
    def __new__(cls, name, bases, attrs):
        for attr_name, attr_type in attrs.get('__annotations__', {}).items():
            if issubclass(attr_type, Node):
                # Logic to automatically manage Node attributes can be added here
                pass
        return super().__new__(cls, name, bases, attrs)

# Define the Node class with rearranged fields
@dataclass
class Node(Generic[NodeT]):
    id: int = field(default_factory=int)
    name: str

# Define the Edge class
@dataclass
class Edge(Generic[EdgeT]):
    source: NodeT
    destination: NodeT
    weight: float = 1.0

# Define the Graph class with the metaclass
class Graph(Generic[NodeT, EdgeT], metaclass=GraphMeta):
    def __init__(self):
        self.graph = nx.Graph()
        
    def add_node(self, node: NodeT):
        self.graph.add_node(node.id, data=node)
        
    def add_edge(self, edge: EdgeT):
        self.graph.add_edge(edge.source.id, edge.destination.id, weight=edge.weight)

    def neighbors(self, node: NodeT) -> List[NodeT]:
        return [self.graph.nodes[n]['data'] for n in self.graph.neighbors(node.id)]

    def __getattr__(self, name):
        if name == 'friends':
            def wrapper(node: NodeT) -> List[NodeT]:
                return self.neighbors(node)
            return wrapper

# Define a subclass of Node for demonstration
@dataclass
class Person(Node['Person']):
    age: int

# Example usage
person1 = Person(id=1, name="Alice", age=30)
person2 = Person(id=2, name="Bob", age=40)
person3 = Person(id=3, name="Charlie", age=50)

friendship = Edge(source=person1, destination=person2)
acquaintance = Edge(source=person1, destination=person3)

social_graph = Graph[Person, Edge[Person]]()
social_graph.add_node(person1)
social_graph.add_node(person2)
social_graph.add_node(person3)
social_graph.add_edge(friendship)
social_graph.add_edge(acquaintance)

# Retrieve neighbors of person1
friends_of_person1 = social_graph.friends(person1)
friends_of_person1
```

[child ⬇️](#d0e745db-6225-4bd6-8b49-6e5c832ec309)

---

(main branch ⎇)
###### d0e745db-6225-4bd6-8b49-6e5c832ec309
[parent ⬆️](#c3de0a80-97f4-4421-8dd9-84f565e6d762)
