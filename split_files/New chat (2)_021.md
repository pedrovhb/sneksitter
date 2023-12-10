---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (2).md
heading_stack: <root> -> e7c9baec-ffab-4c2e-bbb4-561fd977d430 -> System -> 536e0e74-8c30-49ea-ae85-f83cc1361c13 -> System -> aaa29187-c9e6-4055-a115-71076813ffbc -> User -> cc136d1c-37a8-4c4a-b365-9b8369a2b895 -> Assistant -> Approaches: -> Generalized to ASTs: -> Code Example: -> a238746d-f3e1-4b77-a9b7-ba0f5e8f7049 -> Assistant -> 29d82439-fb56-42eb-afe8-8ca15db19eb8 -> Tool -> f1219ce2-4490-4271-881d-328b7eed1acf -> Assistant -> aaa2c008-0c05-4714-90ce-395abd9559a8 -> User -> b4bb145a-3220-4564-b3ee-c5ec6c3ac485 -> Assistant
---
# Assistant

```python
import networkx as nx
from networkx.algorithms import isomorphism

# Create a DiGraph
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (3, 5), (1, 6), (6, 7), (1, 8)])

# Create a pattern DiGraph to search for
P = nx.DiGraph()
P.add_edges_from([(1, 2), (2, 3), (1, 3)])

# Check for subgraph isomorphism
GM = isomorphism.DiGraphMatcher(G, P)

# Find all subgraph isomorphisms
subgraphs = [dict(zip(P.nodes(), nodes)) for nodes in GM.subgraph_isomorphisms_iter()]

subgraphs
```

[child ⬇️](#8d058de8-bf7e-4d33-8add-ff38a294ccf3)

---

(main branch ⎇)
###### 8d058de8-bf7e-4d33-8add-ff38a294ccf3
[parent ⬆️](#b4bb145a-3220-4564-b3ee-c5ec6c3ac485)
