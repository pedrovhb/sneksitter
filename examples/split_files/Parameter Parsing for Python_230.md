# Tool

```python
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[45], line 8
      5     class Config:
      6         extra = "forbid"
----> 8 class Parameter(Model):
      9     name: bytes = Field(..., description="The name (identifier) of the parameter.")
     10     type: bytes | None = Field(
     11         None,
     12         description="The type annotation of the parameter, the same as it was present in the code (if at all).",
     13     )

File ~/.local/lib/python3.8/site-packages/pydantic/main.py:179, in pydantic.main.ModelMetaclass.__new__()

File ~/.local/lib/python3.8/site-packages/pydantic/typing.py:399, in pydantic.typing.resolve_annotations()

File /usr/lib/python3.8/typing.py:270, in _eval_type(t, globalns, localns)
    266 """Evaluate all forward references in the given type t.
    267 For use of globalns and localns see the docstring for get_type_hints().
    268 """
    269 if isinstance(t, ForwardRef):
--> 270     return t._evaluate(globalns, localns)
    271 if isinstance(t, _GenericAlias):
    272     ev_args = tuple(_eval_type(a, globalns, localns) for a in t.__args__)

File /usr/lib/python3.8/typing.py:518, in ForwardRef._evaluate(self, globalns, localns)
    515     elif localns is None:
    516         localns = globalns
    517     self.__forward_value__ = _type_check(
--> 518         eval(self.__forward_code__, globalns, localns),
    519         "Forward references must evaluate to types.",
    520         is_argument=self.__forward_is_argument__)
    521     self.__forward_evaluated__ = True
    522 return self.__forward_value__

File <string>:1

TypeError: unsupported operand type(s) for |: 'type' and 'NoneType'

```

[child ⬇️](#8dc4de2f-8d0e-4100-afbb-36985ab8cd2a)

---

(main branch ⎇)
###### 8dc4de2f-8d0e-4100-afbb-36985ab8cd2a
[parent ⬆️](#d0f55c00-a777-4f04-86de-478a88758be8)
