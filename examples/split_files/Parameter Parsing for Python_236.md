# Tool

```python
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[46], line 86
     83         return parameters
     85 # Rerun the test to verify the changes
---> 86 parsed_parameters = Parameter.from_node_parameters(parameters_node)
     87 parsed_parameters_data = [vars(param) for param in parsed_parameters]
     88 parsed_parameters_data

Cell In[46], line 69, in Parameter.from_node_parameters(cls, node)
     66     saw_keyword_separator = True
     67     continue
---> 69 param = cls.from_node(child)
     71 if saw_positional_separator and not saw_keyword_separator:
     72     param.is_positional_only = True

Cell In[46], line 43, in Parameter.from_node(cls, node, description)
     41 name = extract_name(node)
     42 type_annotation = extract_type(node)
---> 43 default_value = extract_default(node)
     44 return cls(
     45     name=name,
     46     type=type_annotation,
     47     default=default_value,
     48     description=description,
     49 )

Cell In[44], line 5, in extract_default(node)
      2 def extract_default(node: Node) -> Optional[bytes]:
      3     if node.type in ['default_parameter', 'typed_default_parameter']:
      4         # Directly process the node if it's already of the correct type
----> 5         actual_default_nodes = [child for child in node.children if child.type not in ['identifier', ':', '=', 'type'] and not child.has_children]
      6         if actual_default_nodes:
      7             return actual_default_nodes[0].text

Cell In[44], line 5, in <listcomp>(.0)
      2 def extract_default(node: Node) -> Optional[bytes]:
      3     if node.type in ['default_parameter', 'typed_default_parameter']:
      4         # Directly process the node if it's already of the correct type
----> 5         actual_default_nodes = [child for child in node.children if child.type not in ['identifier', ':', '=', 'type'] and not child.has_children]
      6         if actual_default_nodes:
      7             return actual_default_nodes[0].text

AttributeError: 'tree_sitter.Node' object has no attribute 'has_children'

```

[child ⬇️](#8665735e-a6a0-4ab3-abe4-a65e7764a04b)

---

(main branch ⎇)
###### 8665735e-a6a0-4ab3-abe4-a65e7764a04b
[parent ⬆️](#3f19c561-ec1b-4b0b-aee0-52221fe21e11)
