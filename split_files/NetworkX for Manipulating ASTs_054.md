---
file: /home/pedro/Documents/chatgpt_export/Markdown/NetworkX for Manipulating ASTs.md
heading_stack: <root> -> 71a1ccac-6cd0-4408-bc8a-2b431709a5d1 -> System -> 1dad7dfb-bea4-4abe-9d4a-6ce3af566faa -> System -> aaa28000-9b67-40c0-adba-594fac31b5cd -> User -> 470ac03f-1ee2-40df-9d83-ca0d9770fcde -> Assistant -> Representing ASTs as Graphs -> Operations -> 1. Transforming AST to NetworkX Graph -> 2. Analyzing and Manipulating -> 3. Transforming NetworkX Graph back to AST -> Advantages -> Caveats -> aaa2a60d-5686-41b9-b7fb-d8df3cc4f04c -> User -> 327b3201-45d7-486b-92a0-a30e90f9ea7b -> Assistant -> Operations Made Easier by NetworkX -> Alternative Libraries and Data Structures -> aaa20456-db56-4cf6-816c-cb073fe52d98 -> User -> 754fbcfa-654b-4ebd-a4f9-6a5906b4fa7a -> Assistant -> Applications in AST Manipulation -> Workflow with ASTs -> Considerations -> aaa22415-a6b1-4c7f-a115-839b15532cee -> User -> f640d2ca-5869-4792-909c-68b7071c6e82 -> Assistant -> Formal Definition -> Applications -> Algorithms -> Complexity -> NetworkX and Subgraph Isomorphism -> aaa29107-8cc0-4f2f-b5c5-e424f598075d -> User -> 1411f692-1f4a-4ef1-9196-9e7ae906240d -> Assistant -> Theory Behind Subgraph Isomorphism in Nested Data Structures -> Nodes -> Edges -> Typing Unification -> Code Demonstration -> 237e73c3-4c4e-42b7-91b3-29e325a122c1 -> Assistant -> 913cbd7d-22b8-4453-a7ea-552f502d4e37 -> Tool -> 994a736c-9a29-47c4-9323-ac4f54849f7a -> Assistant -> 5e02d0ca-93b2-4d53-bb2e-42722132078e -> Assistant
---
# Assistant

```python
# Adjust the sub-schema graph to find within the main graph
# We'll look for any 'object' that contains a 'name' of type 'string' and an 'age' of type 'int'
H_adjusted = nx.DiGraph()
H_adjusted.add_nodes_from([
    (1, {'key': 'object', 'type': 'object'}),
    (2, {'key': 'name', 'type': 'string'}),
    (3, {'key': 'age', 'type': 'int'})
])
H_adjusted.add_edges_from([
    (1, 2),
    (1, 3)
])

# Initialize VF2 algorithm for subgraph isomorphism with the adjusted sub-schema
GM_adjusted = isomorphism.DiGraphMatcher(G, H_adjusted, node_match=lambda n1, n2: n1['key'] == n2['key'] and n1['type'] == n2['type'])

# Find and list all subgraph isomorphisms with the adjusted sub-schema
subgraphs_adjusted = [dict(iso) for iso in GM_adjusted.subgraph_isomorphisms_iter()]
subgraphs_adjusted
```

[child ⬇️](#f454ad32-af8f-40cc-8f50-ff26f136ed76)

---

(main branch ⎇)
###### f454ad32-af8f-40cc-8f50-ff26f136ed76
[parent ⬆️](#5e02d0ca-93b2-4d53-bb2e-42722132078e)
