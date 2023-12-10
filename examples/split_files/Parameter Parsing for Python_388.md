# User

    Traceback (most recent call last)
Cell In[1], line 150
    122 tree = parser.parse(
    123     d(
    124         """
   (...)
    147     .strip()
    148 )
    149 parameters_node = tree.root_node.children_by_field_name("function_definition")[0].children_by_field_name("parameters")[0]
--> 150 parsed_parameters = Parameter.from_node_parameters(parameters_node)
    151 parsed_parameters_data = [vars(param) for param in parsed_parameters]
    152 print(parsed_parameters_data)

Cell In[1], line 103, in Parameter.from_node_parameters(cls, node)
    100     saw_keyword_separator = True
    101     continue
--> 103 param = cls.from_node(child)
    105 if saw_positional_separator and not saw_keyword_separator:
    106     param.is_positional_only = True

Cell In[1], line 74, in Parameter.from_node(cls, node, description)
     71                 return actual_default_nodes[-1].text
     72     return None
---> 74 name = extract_name(node)
     75 type_annotation = extract_type(node)
     76 default_value = extract_default(node)

Cell In[1], line 55, in Parameter.from_node.<locals>.extract_name(node)
     54 def extract_name(node: Node) -> bytes:
---> 55     return [child for child in node.children if child.type == 'identifier'][0].text

IndexError: list index out of range

[child ⬇️](#656146d2-86b4-456f-97f9-44bb0f5d5356)

---

(other branch ⎇)
###### 656146d2-86b4-456f-97f9-44bb0f5d5356
[parent ⬆️](#aaa2b3d3-d468-4d8a-be0a-f9e9a06cd90b)
