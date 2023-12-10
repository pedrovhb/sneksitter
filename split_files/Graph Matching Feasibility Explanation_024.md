---
file: /home/pedro/Documents/chatgpt_export/Markdown/Graph Matching Feasibility Explanation.md
heading_stack: <root> -> c107c9c9-8f6a-495c-904b-235d56a5d2b2 -> System -> 201c3e31-2aa4-4889-bf9a-7b2f47a7b304 -> System -> aaa251a3-5cb0-4526-a1ed-39cc659d7cc2 -> User -> 77b07057-503b-4e8f-bac8-e1a6de24738f -> Assistant -> Syntactic Feasibility -> Semantic Feasibility -> aaa2c26f-c4b8-4e51-8df5-fd93d6377e9e -> User -> 5103b6c1-bfb8-4864-8c23-7d1455a6a36d -> Assistant -> d1235c26-f990-48c6-b489-d93d840c3431 -> Assistant -> 4f565871-050f-49dd-955b-dc794660f886 -> Tool -> 217fd290-3683-4577-a0a6-24d240457cfa -> Assistant -> 0232b550-a655-4b35-8e31-c171ada0f0bf -> Assistant -> d05aeb1d-fff5-4a2d-b95c-62aaddffda84 -> Tool
---
# Tool

```python
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[2], line 1
----> 1 class JSONSchemaMatcher(nx.GraphMatcher):
      2     def semantic_feasibility(self, G1_node, G2_node):
      3         # Get the outward edges for both nodes
      4         G1_edges = set(self.G1[G1_node])

File ~/.local/lib/python3.8/site-packages/networkx/__init__.py:51, in __getattr__(name)
     42 if name == "write_yaml":
     43     raise ImportError(
     44         "\nwrite_yaml has been removed from NetworkX, please use `yaml`\n"
     45         "directly:\n\n"
   (...)
     49         "This message will be removed in NetworkX 3.0."
     50     )
---> 51 raise AttributeError(f"module {__name__} has no attribute {name}")

AttributeError: module networkx has no attribute GraphMatcher

```

[child ⬇️](#0b721f7f-a563-4fc4-bf0d-f93aacf247ad)

---

(other branch ⎇)
###### 0b721f7f-a563-4fc4-bf0d-f93aacf247ad
[parent ⬆️](#d05aeb1d-fff5-4a2d-b95c-62aaddffda84)
