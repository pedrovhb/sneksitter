---
file: /home/pedro/Documents/chatgpt_export/Markdown/Graph Matching Feasibility Explanation.md
heading_stack: <root> -> c107c9c9-8f6a-495c-904b-235d56a5d2b2 -> System -> 201c3e31-2aa4-4889-bf9a-7b2f47a7b304 -> System -> aaa251a3-5cb0-4526-a1ed-39cc659d7cc2 -> User -> 77b07057-503b-4e8f-bac8-e1a6de24738f -> Assistant -> Syntactic Feasibility -> Semantic Feasibility
---
### Semantic Feasibility
Semantic feasibility, on the other hand, involves additional, user-defined rules that go beyond the basic structural aspects. These might involve attributes of the nodes and edges, or some other domain-specific information that the graphs encode. For example, if the nodes represent cities, a semantic rule might be that two nodes can only be matched if their populations are within a certain range of each other.

In the implementation you mentioned, the `semantic_feasibility()` function is a placeholder for these user-defined, domain-specific rules. By default, it returns `True`, meaning that semantic checks are not performed unless you specifically override this method to include your own checks.

To summarize:
- Syntactic feasibility is about structural rules (e.g., degree of nodes, existence of edges).
- Semantic feasibility is about domain-specific rules (e.g., node attributes, edge weights).

Both checks are combined using logical AND, meaning both have to pass for two nodes (or edges) to be considered a match.

[child 1 ⬇️](#aaa2c26f-c4b8-4e51-8df5-fd93d6377e9e) | [child 2 ⬇️](#aaa22904-04dd-4618-976b-ad06c7f5577e)

---

(other branch ⎇)
###### aaa2c26f-c4b8-4e51-8df5-fd93d6377e9e
[parent ⬆️](#77b07057-503b-4e8f-bac8-e1a6de24738f)
