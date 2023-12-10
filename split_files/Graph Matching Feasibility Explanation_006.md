---
file: /home/pedro/Documents/chatgpt_export/Markdown/Graph Matching Feasibility Explanation.md
heading_stack: <root> -> c107c9c9-8f6a-495c-904b-235d56a5d2b2 -> System -> 201c3e31-2aa4-4889-bf9a-7b2f47a7b304 -> System -> aaa251a3-5cb0-4526-a1ed-39cc659d7cc2 -> User
---
# User

An implementation of VF2 algorithm for graph isomorphism testing.

The simplest interface to use this module is to call networkx.is_isomorphic().

Introduction
The GraphMatcher and DiGraphMatcher are responsible for matching graphs or directed graphs in a predetermined manner. This usually means a check for an isomorphism, though other checks are also possible. For example, a subgraph of one graph can be checked for isomorphism to a second graph.

Matching is done via syntactic feasibility. It is also possible to check for semantic feasibility. Feasibility, then, is defined as the logical AND of the two functions.

To include a semantic check, the (Di)GraphMatcher class should be subclassed, and the semantic_feasibility() function should be redefined. By default, the semantic feasibility function always returns True. The effect of this is that semantics are not considered in the matching of G1 and G2.

---

What is meant by semantic vs synctatic feasibility in the above?

[child ⬇️](#77b07057-503b-4e8f-bac8-e1a6de24738f)

---

(main branch ⎇)
###### 77b07057-503b-4e8f-bac8-e1a6de24738f
[parent ⬆️](#aaa251a3-5cb0-4526-a1ed-39cc659d7cc2)
