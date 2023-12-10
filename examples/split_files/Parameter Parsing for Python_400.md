# Tool

```python
---------------------------------------------------------------------------
ValidationError                           Traceback (most recent call last)
Cell In[1], line 116
     93 tree = parser.parse(d("""
     94     def foo(*vararg: str, x, y=1, /, f="a string default", *, z: int=5, w: Callable[P, T]=print, **kwargs) -> int:
     95         '''This is a docstring.
   (...)
    112         return x + y
    113 """).encode().strip())
    115 parameters_node = tree.root_node.children_by_field_name("function_definition")[0].children_by_field_name("parameters")[0]
--> 116 parsed_parameters = Parameter.from_node_parameters(parameters_node)
    117 parsed_parameters_data = [vars(param) for param in parsed_parameters]
    118 parsed_parameters_data

Cell In[1], line 72, in Parameter.from_node_parameters(cls, node)
     69     saw_keyword_separator = True
     70     continue
---> 72 param = cls.from_node(child)
     74 if saw_positional_separator and not saw_keyword_separator:
     75     param.is_positional_only = True

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

[child ⬇️](#70a2b6d6-7443-4156-9620-6d1a8160a815)

---

(other branch ⎇)
###### 70a2b6d6-7443-4156-9620-6d1a8160a815
[parent ⬆️](#1613eac2-9f9d-4503-bc20-69e7dc7e4a8d)
