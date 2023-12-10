---
file: /home/pedro/Documents/chatgpt_export/Markdown/Parse node-types.json for models..md
heading_stack: <root> -> 484de9b7-6d66-4eed-a655-00940b23dffd -> System -> 40bb608e-2dfa-4a1b-a046-7b8d340b36c3 -> System -> aaa2de54-e0e3-4848-813c-de80cbe3e253 -> User -> Basic Info -> Internal Nodes -> Task -> 9387b9ba-fae2-448c-b4df-a2a1a946c3b6 -> Tool -> b6a63d27-6380-4d59-9ae7-88eabcad6cff -> Assistant -> Key Components: -> Observations: -> Examples: -> aaa2bc1e-c7a6-4ef9-8020-e692c381a096 -> User -> 3682d6bc-a0f0-4628-af8b-6b87bf5ae291 -> Assistant -> 4e945266-3138-47a1-8055-825076720fed -> Tool -> 29f0d10f-1f29-4fa2-9f0a-94ab3ada303e -> Assistant -> d82f3fa2-d61e-4b62-9791-4fa5d90fd3d8 -> Tool -> 9d0513e1-7bb4-44d8-ba04-4017488bd7b5 -> Assistant -> 5687973b-f6b4-44dd-8753-d874c792849a -> Assistant -> aaa2f83c-9b8f-4200-aaf4-8f3ee7735d09 -> User -> 5a29425e-53e2-4952-b620-5a7c0b6b440a -> Assistant -> 078cb5a0-cad0-41fa-9128-9a1ccd758aad -> Tool -> 04fdd7fe-79e6-4377-8b0c-c0a74491dfa4 -> Assistant -> aaa2125e-286f-4a91-b0de-1d02b611af03 -> User -> 230aa5aa-41ed-44a7-8b5e-da0ee141b9b1 -> Assistant -> 6187af27-e71d-4c9e-b986-24776b23b1e0 -> Tool -> 146e447e-973f-42b9-b6c1-d43b5932c1d9 -> Assistant -> 861b740c-d72a-4285-a88e-a9d9e14a7be3 -> Assistant -> aaa257df-7e8f-4589-83a8-2bc5efadf708 -> User -> dd745f2e-985c-421f-a601-e6aec7acec08 -> Assistant -> 56b0e5ff-e78a-4fef-a0fb-34ad9c90e3a2 -> Tool -> 0b3a9a0b-715e-427b-a82a-637f80259d88 -> Assistant -> 883f97f1-c528-4d32-98df-fd6f13c0e613 -> Assistant -> 846f0d62-58f5-4d2d-852b-bae243578c50 -> Tool -> f977b04d-50ea-4234-a9f6-4edad18ac7c7 -> Assistant -> 63de661d-7ce6-42ef-97d4-486bb77df05c -> Assistant -> 7cd14f83-02f1-43d9-bd11-544417540b3d -> Tool -> 7d9e09ca-f434-4128-837e-c7092ebc1cc2 -> Assistant -> aaa2b595-8594-475d-aee6-27644f6fd586 -> User -> 537da754-8eff-473d-9902-f57a00d76d3d -> Assistant -> c3433625-b20b-4ced-a2b4-2bed2a6283e8 -> Assistant -> 2ff00ce9-0cba-42fc-a7f9-b9cbe86cf49a -> Assistant -> 092e59a4-c0d7-4b75-9d9c-3bdeedde0f9c -> Assistant -> 940ca50a-6ed9-403a-ba42-acdc7648254b -> Tool -> af960d3f-566c-4f4c-96e9-597b5c831648 -> Assistant -> 3ac6792a-0f25-41a2-b97d-31be31a5ef0a -> Assistant -> 58bd6eff-aafe-4f64-b04f-160e2031fa8c -> Tool
---
# Tool

```python
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[24], line 22
     18         return cls._instances[key]
     20 # Update ChildType, InternalNodeType, and SupertypeNode to match the new field order
     21 @dataclass(frozen=True)
---> 22 class ChildType(NodeType):
     23     types: List[NodeType]
     25 @dataclass(frozen=True)
     26 class InternalNodeType(NodeType):

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

TypeError: non-default argument 'types' follows default argument

```

[child ⬇️](#c8aac6b4-1627-4c3c-be9b-d5aac4438cd2)

---

(other branch ⎇)
###### c8aac6b4-1627-4c3c-be9b-d5aac4438cd2
[parent ⬆️](#58bd6eff-aafe-4f64-b04f-160e2031fa8c)
