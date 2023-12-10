# Tool

```python
---------------------------------------------------------------------------
ValidationError                           Traceback (most recent call last)
Cell In[3], line 43
     40 Parameter.from_node_parameters = from_node_parameters
     42 # Rerun the test to verify the changes
---> 43 parsed_parameters = Parameter.from_node_parameters(parameters_node)
     44 parsed_parameters_data = [vars(param) for param in parsed_parameters]
     45 parsed_parameters_data

Cell In[3], line 23, in from_node_parameters(cls, node)
     20 if child.type in ['positional_separator', 'keyword_separator']:
     21     continue
---> 23 param = cls.from_node(child)
     25 if saw_positional_separator and not saw_keyword_separator:
     26     param.is_positional_only = True

Cell In[1], line 49, in Parameter.from_node(cls, node, description)
     46 type_annotation = extract_type(node)
     47 default_value = extract_default(node)
---> 49 return cls(
     50     name=name,
     51     type=type_annotation,
     52     default=default_value,
     53     description=description,
     54 )

File ~/.local/lib/python3.8/site-packages/pydantic/main.py:165, in BaseModel.__init__(__pydantic_self__, **data)
    163 # `__tracebackhide__` tells pytest and some other tools to omit this function from tracebacks
    164 __tracebackhide__ = True
--> 165 __pydantic_self__.__pydantic_validator__.validate_python(data, self_instance=__pydantic_self__)

ValidationError: 1 validation error for Parameter
name
  Input should be a valid bytes [type=bytes_type, input_value=None, input_type=NoneType]
    For further information visit https://errors.pydantic.dev/2.3/v/bytes_type

```

[child ⬇️](#7867c704-3df5-4d5e-adea-dcf18f022864)

---

(other branch ⎇)
###### 7867c704-3df5-4d5e-adea-dcf18f022864
[parent ⬆️](#5bc1a8f1-1c65-4302-b54c-c7a5c2853de1)
