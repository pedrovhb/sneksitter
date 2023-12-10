---
file: /home/pedro/Documents/chatgpt_export/Markdown/Graph Matching Feasibility Explanation.md
heading_stack: <root> -> c107c9c9-8f6a-495c-904b-235d56a5d2b2 -> System -> 201c3e31-2aa4-4889-bf9a-7b2f47a7b304 -> System -> aaa251a3-5cb0-4526-a1ed-39cc659d7cc2 -> User -> 77b07057-503b-4e8f-bac8-e1a6de24738f -> Assistant -> Syntactic Feasibility -> Semantic Feasibility -> aaa2c26f-c4b8-4e51-8df5-fd93d6377e9e -> User -> 5103b6c1-bfb8-4864-8c23-7d1455a6a36d -> Assistant -> d1235c26-f990-48c6-b489-d93d840c3431 -> Assistant -> 4f565871-050f-49dd-955b-dc794660f886 -> Tool -> 217fd290-3683-4577-a0a6-24d240457cfa -> Assistant -> 0232b550-a655-4b35-8e31-c171ada0f0bf -> Assistant
---
# Assistant

```python
class JSONSchemaMatcher(nx.GraphMatcher):
    def semantic_feasibility(self, G1_node, G2_node):
        # Get the outward edges for both nodes
        G1_edges = set(self.G1[G1_node])
        G2_edges = set(self.G2[G2_node])
        
        # Check if the nodes have the same outward edges (same keys in JSON)
        return G1_edges == G2_edges

# Create a graph matcher object
matcher = JSONSchemaMatcher(graph1, graph2)

# Find all common subgraphs that are also semantically feasible
common_subgraphs = list(matcher.subgraph_isomorphisms_iter())

common_subgraphs
```

[child ⬇️](#d05aeb1d-fff5-4a2d-b95c-62aaddffda84)

---

(other branch ⎇)
###### d05aeb1d-fff5-4a2d-b95c-62aaddffda84
[parent ⬆️](#0232b550-a655-4b35-8e31-c171ada0f0bf)
