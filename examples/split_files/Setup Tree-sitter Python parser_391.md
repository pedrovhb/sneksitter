# Tool

```python
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[40], line 44
     42 # Test the FunctionInfo class with a sample node
     43 sample_decorated_definition_node = decorator_sample_tree.root_node.children[0]
---> 44 FunctionInfo.from_node(sample_decorated_definition_node)

Cell In[40], line 28, in FunctionInfo.from_node(cls, node)
     26 decorator_name = child.children[1].text.decode()
     27 decorator_args = []
---> 28 for arg_node in child.children[2].children:
     29     if arg_node.type in ['string', 'integer']:
     30         decorator_args.append(arg_node.text.decode().replace('"', ''))

IndexError: list index out of range

```

[child ⬇️](#f82ff2f1-6d79-401f-9d16-44ee18821876)

---

(other branch ⎇)
###### f82ff2f1-6d79-401f-9d16-44ee18821876
[parent ⬆️](#228a1410-86f3-4a88-887d-fc45c82694a6)
