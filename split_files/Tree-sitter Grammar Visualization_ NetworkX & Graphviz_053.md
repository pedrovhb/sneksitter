---
file: /home/pedro/Documents/chatgpt_export/Markdown/Tree-sitter Grammar Visualization_ NetworkX & Graphviz.md
heading_stack: <root> -> b871f517-1eff-4ce0-a351-f14ea50e2084 -> System -> 10bdd2ac-112a-465d-8a80-9a7e6b87ee8a -> System -> aaa26ed0-25be-4ce1-881e-13f438a81018 -> User -> 16f82114-8497-4426-bb51-62a94559597a -> Assistant -> NetworkX -> Graphviz -> Combining NetworkX and Graphviz for Tree-sitter Grammar Visualization -> The Challenge -> The Approach -> Creative Ideas -> Technical Implementation -> Potential Pitfalls -> Conclusion -> aaa26fc9-1f37-46e5-9259-458a8d55dd15 -> User -> 9c564aec-e677-44c1-a480-a6c57d293462 -> Assistant -> a3eb6e27-f341-4b7a-a3d2-34f4cc84ec17 -> Assistant -> c52b2616-0df0-48a9-9a0a-0953bfbd2965 -> Tool -> ae11aab9-6f35-454c-94b2-c2c53890111e -> Assistant -> ca2f2a60-b9a3-4f93-9754-5ebe5ba70517 -> Assistant -> 8fba5a35-e974-4d97-ae80-844eb75c9ac4 -> Tool -> 6d10afb6-8dde-460d-9bad-821eb823350a -> Assistant -> cfa78ec0-6094-4895-a72e-3a426f4b264f -> Assistant -> 873bf5b9-8358-4f4b-828c-bc6c8c8b0cb2 -> Tool -> 1e02448a-70e8-498b-9928-ca9322d13faa -> Assistant -> aaa2f428-a377-42b7-a840-b7891498e057 -> User -> f63d0e39-9f0b-48d6-84eb-9062cb61b68e -> Assistant -> c6ac11e8-313a-4e50-9fdd-313705be3dee -> Assistant -> 326bbb63-28ff-4ade-9893-1f1b83ad81e9 -> Tool -> 35bfbcf8-aee4-4527-9f9c-8e48ebda444e -> Assistant -> 1377b9b9-b2c5-4e10-94a2-3e290eb55e68 -> Assistant -> eaa32754-88aa-408b-921f-31ceba106533 -> Tool
---
# Tool

```python
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[5], line 5
      2 from IPython.display import Image
      4 # Create a PyGraphviz graph from the NetworkX graph
----> 5 A = nx.to_agraph(G)
      7 # Define a pastel color theme based on node types
      8 color_map = {
      9     'ALIAS': '#FAD02E',
     10     'BLANK': '#D3F3EE',
   (...)
     23     'TOKEN': '#C4BBF0'
     24 }

File ~/.local/lib/python3.8/site-packages/networkx/__init__.py:51, in __getattr__(name)
     42 if name == "write_yaml":
     43     raise ImportError(
     44         "\nwrite_yaml has been removed from NetworkX, please use `yaml`\n"
     45         "directly:\n\n"
   (...)
     49         "This message will be removed in NetworkX 3.0."
     50     )
---> 51 raise AttributeError(f"module {__name__} has no attribute {name}")

AttributeError: module networkx has no attribute to_agraph

```

[child ⬇️](#d5b4e9e9-1c90-4e65-8d96-7566a2fa587a)

---

(other branch ⎇)
###### d5b4e9e9-1c90-4e65-8d96-7566a2fa587a
[parent ⬆️](#eaa32754-88aa-408b-921f-31ceba106533)
