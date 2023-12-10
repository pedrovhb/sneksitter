# Tool

```python
---------------------------------------------------------------------------
ValidationError                           Traceback (most recent call last)
Cell In[2], line 57
     54 Parameter.from_node_parameters = from_node_parameters
     56 # Rerun the test to verify the changes
---> 57 parsed_parameters = Parameter.from_node_parameters(parameters_node)
     58 parsed_parameters_data = [vars(param) for param in parsed_parameters]
     59 parsed_parameters_data

Cell In[2], line 34, in from_node_parameters(cls, node)
     31         saw_keyword_separator = True
     32     continue
---> 34 param = cls.from_node(child)
     36 if param.name is None:
     37     continue

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

[child ⬇️](#8a82996c-f0c0-43f2-b046-548f1621339c)

---

(other branch ⎇)
###### 8a82996c-f0c0-43f2-b046-548f1621339c
[parent ⬆️](#2fee69ae-a692-47df-87c3-a736556d476e)
