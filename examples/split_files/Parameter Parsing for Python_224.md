# Tool

```python
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[44], line 17
     14     return None
     16 # Rerun the test to verify the changes
---> 17 parsed_parameters = Parameter.from_node_parameters(parameters_node)
     18 parsed_parameters_data = [vars(param) for param in parsed_parameters]
     19 parsed_parameters_data

Cell In[42], line 90, in Parameter.from_node_parameters(cls, node)
     87     saw_keyword_separator = True
     88     continue
---> 90 param = cls.from_node(child)
     92 if saw_positional_separator and not saw_keyword_separator:
     93     param.is_positional_only = True

Cell In[42], line 65, in Parameter.from_node(cls, node, description)
     63 type_annotation = extract_type(node)
     64 default_value = extract_default(node)
---> 65 return cls(
     66     name=name,
     67     type=type_annotation,
     68     default=default_value,
     69     description=description,
     70 )

TypeError: Parameter() takes no arguments

```

[child ⬇️](#5e7eb841-a452-4e5a-9230-cf148ec88a53)

---

(main branch ⎇)
###### 5e7eb841-a452-4e5a-9230-cf148ec88a53
[parent ⬆️](#188296f5-4a7f-4320-9045-42b963773f75)
