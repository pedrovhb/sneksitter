---
file: /home/pedro/Documents/chatgpt_export/Markdown/NetworkX for Manipulating ASTs.md
heading_stack: <root> -> 71a1ccac-6cd0-4408-bc8a-2b431709a5d1 -> System -> 1dad7dfb-bea4-4abe-9d4a-6ce3af566faa -> System -> aaa28000-9b67-40c0-adba-594fac31b5cd -> User -> 470ac03f-1ee2-40df-9d83-ca0d9770fcde -> Assistant -> Representing ASTs as Graphs -> Operations -> 1. Transforming AST to NetworkX Graph -> 2. Analyzing and Manipulating -> 3. Transforming NetworkX Graph back to AST -> Advantages -> Caveats -> aaa2a60d-5686-41b9-b7fb-d8df3cc4f04c -> User -> 327b3201-45d7-486b-92a0-a30e90f9ea7b -> Assistant -> Operations Made Easier by NetworkX -> Alternative Libraries and Data Structures -> aaa20456-db56-4cf6-816c-cb073fe52d98 -> User -> 754fbcfa-654b-4ebd-a4f9-6a5906b4fa7a -> Assistant -> Applications in AST Manipulation -> Workflow with ASTs -> Considerations -> aaa22415-a6b1-4c7f-a115-839b15532cee -> User -> f640d2ca-5869-4792-909c-68b7071c6e82 -> Assistant -> Formal Definition -> Applications -> Algorithms -> Complexity -> NetworkX and Subgraph Isomorphism -> aaa29107-8cc0-4f2f-b5c5-e424f598075d -> User -> 1411f692-1f4a-4ef1-9196-9e7ae906240d -> Assistant -> Theory Behind Subgraph Isomorphism in Nested Data Structures -> Nodes -> Edges -> Typing Unification -> Code Demonstration -> 237e73c3-4c4e-42b7-91b3-29e325a122c1 -> Assistant
---
# Assistant

```python
import networkx as nx
from networkx.algorithms import isomorphism

# Create a graph to represent JSON-like nested data structure
G = nx.DiGraph()

# Node format: (Node ID, {'key': 'key name', 'type': 'data type'})
# Adding nodes
G.add_nodes_from([
    (1, {'key': 'name', 'type': 'string'}),
    (2, {'key': 'age', 'type': 'int'}),
    (3, {'key': 'address', 'type': 'object'}),
    (4, {'key': 'street', 'type': 'string'}),
    (5, {'key': 'city', 'type': 'string'}),
    (6, {'key': 'friends', 'type': 'array'}),
    (7, {'key': 'name', 'type': 'string'}),
    (8, {'key': 'age', 'type': 'int'})
])

# Adding edges to represent parent-child relationships in JSON
# Edge format: (Parent Node ID, Child Node ID)
G.add_edges_from([
    (3, 4),
    (3, 5),
    (6, 7),
    (6, 8)
])

# Create a sub-schema graph to find within the main graph
H = nx.DiGraph()
H.add_nodes_from([
    (1, {'key': 'name', 'type': 'string'}),
    (2, {'key': 'age', 'type': 'int'})
])
H.add_edge(1, 2)

# Initialize VF2 algorithm for subgraph isomorphism
GM = isomorphism.DiGraphMatcher(G, H, node_match=lambda n1, n2: n1['key'] == n2['key'] and n1['type'] == n2['type'])

# Find and list all subgraph isomorphisms
subgraphs = [dict(iso) for iso in GM.subgraph_isomorphisms_iter()]
subgraphs
```

[child ⬇️](#913cbd7d-22b8-4453-a7ea-552f502d4e37)

---

(main branch ⎇)
###### 913cbd7d-22b8-4453-a7ea-552f502d4e37
[parent ⬆️](#237e73c3-4c4e-42b7-91b3-29e325a122c1)
