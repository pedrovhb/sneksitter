---
file: /home/pedro/Documents/chatgpt_export/Markdown/Graph Matching Feasibility Explanation.md
heading_stack: <root> -> c107c9c9-8f6a-495c-904b-235d56a5d2b2 -> System -> 201c3e31-2aa4-4889-bf9a-7b2f47a7b304 -> System -> aaa251a3-5cb0-4526-a1ed-39cc659d7cc2 -> User -> 77b07057-503b-4e8f-bac8-e1a6de24738f -> Assistant -> Syntactic Feasibility -> Semantic Feasibility -> aaa2c26f-c4b8-4e51-8df5-fd93d6377e9e -> User -> 5103b6c1-bfb8-4864-8c23-7d1455a6a36d -> Assistant -> d1235c26-f990-48c6-b489-d93d840c3431 -> Assistant
---
# Assistant

```python
import networkx as nx
import json

def json_to_graph(json_obj, graph=None, parent=None):
    if graph is None:
        graph = nx.Graph()
    
    if isinstance(json_obj, dict):
        for k, v in json_obj.items():
            graph.add_node(k)
            if parent:
                graph.add_edge(parent, k)
            json_to_graph(v, graph, k)
    elif isinstance(json_obj, list):
        for i, v in enumerate(json_obj):
            index_key = f"{parent}[{i}]"
            graph.add_node(index_key)
            graph.add_edge(parent, index_key)
            json_to_graph(v, graph, index_key)
    return graph

# Example JSON API responses
json1 = {
    "name": "Alice",
    "age": 30,
    "address": {
        "city": "NYC",
        "zip": "10001"
    }
}

json2 = {
    "name": "Bob",
    "age": 40,
    "address": {
        "city": "SF",
        "state": "CA"
    },
    "email": "bob@example.com"
}

# Convert to graphs
graph1 = json_to_graph(json1)
graph2 = json_to_graph(json2)

graph1.nodes(), graph2.nodes()
```

[child ⬇️](#4f565871-050f-49dd-955b-dc794660f886)

---

(other branch ⎇)
###### 4f565871-050f-49dd-955b-dc794660f886
[parent ⬆️](#d1235c26-f990-48c6-b489-d93d840c3431)
