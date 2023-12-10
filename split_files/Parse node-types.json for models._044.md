---
file: /home/pedro/Documents/chatgpt_export/Markdown/Parse node-types.json for models..md
heading_stack: <root> -> 484de9b7-6d66-4eed-a655-00940b23dffd -> System -> 40bb608e-2dfa-4a1b-a046-7b8d340b36c3 -> System -> aaa2de54-e0e3-4848-813c-de80cbe3e253 -> User -> Basic Info -> Internal Nodes -> Task -> 9387b9ba-fae2-448c-b4df-a2a1a946c3b6 -> Tool -> b6a63d27-6380-4d59-9ae7-88eabcad6cff -> Assistant -> Key Components: -> Observations: -> Examples: -> aaa2bc1e-c7a6-4ef9-8020-e692c381a096 -> User -> 3682d6bc-a0f0-4628-af8b-6b87bf5ae291 -> Assistant -> 4e945266-3138-47a1-8055-825076720fed -> Tool -> 29f0d10f-1f29-4fa2-9f0a-94ab3ada303e -> Assistant -> d82f3fa2-d61e-4b62-9791-4fa5d90fd3d8 -> Tool -> 9d0513e1-7bb4-44d8-ba04-4017488bd7b5 -> Assistant -> 5687973b-f6b4-44dd-8753-d874c792849a -> Assistant -> aaa2f83c-9b8f-4200-aaf4-8f3ee7735d09 -> User -> 5a29425e-53e2-4952-b620-5a7c0b6b440a -> Assistant -> 078cb5a0-cad0-41fa-9128-9a1ccd758aad -> Tool -> 04fdd7fe-79e6-4377-8b0c-c0a74491dfa4 -> Assistant -> aaa2125e-286f-4a91-b0de-1d02b611af03 -> User -> 230aa5aa-41ed-44a7-8b5e-da0ee141b9b1 -> Assistant -> 6187af27-e71d-4c9e-b986-24776b23b1e0 -> Tool
---
# Tool

```python
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
Cell In[10], line 34
     31     subtypes: List[NodeType]
     33 # Re-parse the JSON data into dataclass instances
---> 34 parsed_nodes = [parse_node(node) for node in node_types_data]
     36 # Create a dictionary of node types for easy lookup
     37 all_nodes = {node.type: node for node in parsed_nodes}

Cell In[10], line 34, in <listcomp>(.0)
     31     subtypes: List[NodeType]
     33 # Re-parse the JSON data into dataclass instances
---> 34 parsed_nodes = [parse_node(node) for node in node_types_data]
     36 # Create a dictionary of node types for easy lookup
     37 all_nodes = {node.type: node for node in parsed_nodes}

Cell In[5], line 14, in parse_node(node_json)
     12     fields = {}
     13     for k, v in node_json["fields"].items():
---> 14         fields[k] = ChildType(
     15             required=v["required"],
     16             multiple=v["multiple"],
     17             types=[parse_node(t) for t in v["types"]]
     18         )
     20 children = None
     21 if "children" in node_json:

Cell In[10], line 12, in NodeType.__new__(cls, *args, **kwargs)
     11 def __new__(cls, *args, **kwargs):
---> 12     key = (kwargs['type'], kwargs['named'])
     13     if key not in cls._instances:
     14         instance = super().__new__(cls)

KeyError: 'type'

```

[child ⬇️](#146e447e-973f-42b9-b6c1-d43b5932c1d9)

---

(other branch ⎇)
###### 146e447e-973f-42b9-b6c1-d43b5932c1d9
[parent ⬆️](#6187af27-e71d-4c9e-b986-24776b23b1e0)
