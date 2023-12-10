---
file: /home/pedro/Documents/chatgpt_export/Markdown/Graph Integration with Dataclasses.md
heading_stack: <root> -> d5ee1f8c-0262-460f-ae64-079de955da83 -> System -> 4df2c66a-be68-4ed7-939e-5244c07c0394 -> System -> aaa29239-053e-4660-afbe-53e2c8bdaf73 -> User -> 68e1c43a-7d95-419f-8a58-ed77216df416 -> Assistant -> Design Goals -> Components -> Node Class -> Edge Class -> Graph Class -> Observers -> Complete Example -> aaa2b8c0-61e3-452c-ab9f-729395a2d79c -> User -> 14a21363-9c4f-4d33-b7f1-3eca1e79d29c -> Assistant -> 4a5e2a3f-ac57-4e0e-9048-1f1fc82073aa -> Tool -> cea21ee6-1cb1-4fc6-b2ce-a82138645c80 -> Assistant -> aaa27cc4-8bab-410d-ba5e-040a093984ca -> User -> 37c8a936-a17b-4aef-a851-5c1dcd876078 -> Assistant -> c2f8ec96-a0e5-4ab6-b956-27ce1c9ddadd -> Tool -> 5ff5e072-3745-44c8-84b6-675d749b9c35 -> Assistant -> c3de0a80-97f4-4421-8dd9-84f565e6d762 -> Assistant -> d0e745db-6225-4bd6-8b49-6e5c832ec309 -> Tool -> f6feb84d-c67e-47cb-b660-27818edcd6c4 -> Assistant -> 65144943-f7f7-404e-bc70-5e5a83d5d496 -> Assistant -> 5cdf8a64-a799-4b4e-a452-7a4fe7902df0 -> Tool
---
# Tool

```python
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[4], line 9
      5     id: int = field(default_factory=int)
      7 # Rearrange the Person subclass fields accordingly
      8 @dataclass
----> 9 class Person(Node['Person']):
     10     age: int
     12 # Example usage remains the same

File /usr/lib/python3.8/dataclasses.py:1019, in dataclass(cls, init, repr, eq, order, unsafe_hash, frozen)
   1016     return wrap
   1018 # We're called as @dataclass without parens.
-> 1019 return wrap(cls)

File /usr/lib/python3.8/dataclasses.py:1011, in dataclass.<locals>.wrap(cls)
   1010 def wrap(cls):
-> 1011     return _process_class(cls, init, repr, eq, order, unsafe_hash, frozen)

File /usr/lib/python3.8/dataclasses.py:925, in _process_class(cls, init, repr, eq, order, unsafe_hash, frozen)
    921     # Include InitVars and regular fields (so, not ClassVars).
    922     flds = [f for f in fields.values()
    923             if f._field_type in (_FIELD, _FIELD_INITVAR)]
    924     _set_new_attribute(cls, '__init__',
--> 925                        _init_fn(flds,
    926                                 frozen,
    927                                 has_post_init,
    928                                 # The name to use for the "self"
    929                                 # param in __init__.  Use "self"
    930                                 # if possible.
    931                                 '__dataclass_self__' if 'self' in fields
    932                                         else 'self',
    933                                 globals,
    934                       ))
    936 # Get the fields as a list, and include only real fields.  This is
    937 # used in all of the following methods.
    938 field_list = [f for f in fields.values() if f._field_type is _FIELD]

File /usr/lib/python3.8/dataclasses.py:502, in _init_fn(fields, frozen, has_post_init, self_name, globals)
    500             seen_default = True
    501         elif seen_default:
--> 502             raise TypeError(f'non-default argument {f.name!r} '
    503                             'follows default argument')
    505 locals = {f'_type_{f.name}': f.type for f in fields}
    506 locals.update({
    507     'MISSING': MISSING,
    508     '_HAS_DEFAULT_FACTORY': _HAS_DEFAULT_FACTORY,
    509 })

TypeError: non-default argument 'age' follows default argument

```

[child ⬇️](#c23439ce-ae5a-463b-8f61-f5b9a326adaa)

---

(main branch ⎇)
###### c23439ce-ae5a-463b-8f61-f5b9a326adaa
[parent ⬆️](#5cdf8a64-a799-4b4e-a452-7a4fe7902df0)
