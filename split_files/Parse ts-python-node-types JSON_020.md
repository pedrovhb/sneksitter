---
file: /home/pedro/Documents/chatgpt_export/Markdown/Parse ts-python-node-types JSON.md
heading_stack: <root> -> e99eb7ad-94e4-41d7-b226-2e95209438dc -> System -> f5218b62-0612-4055-a04f-15c2a4456b30 -> System -> aaa24a7d-6d79-4f2a-aa46-73a3895b401a -> User -> e2bcdb24-7d4d-4880-bc78-36cac65ea2b7 -> Assistant -> 3af7ae0b-c579-4d4a-90d3-732ef36c4077 -> Assistant -> 8d7a4cfc-4710-4160-b2cd-0ae6821ce860 -> Tool -> 4d1b6605-d6a7-4faf-a82b-dbdbcecc9118 -> Assistant -> aaa292e7-abf4-48a3-8ec5-c9395760f1df -> User -> 95e92a2a-1ecc-4d37-a231-440fb0df8742 -> Assistant -> 61a16991-9ab7-4460-a1c6-a8b1a7370e7e -> Assistant
---
# Assistant

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class NodeType:
    type: str
    named: bool
    subtypes: List['NodeType'] = field(default_factory=list)

# A simple function to convert a dictionary to a NodeType instance
def dict_to_node_type(node_dict):
    type_ = node_dict.get('type')
    named = node_dict.get('named', False)
    subtypes = node_dict.get('subtypes', [])
    return NodeType(type_, named, subtypes)

# Show example conversion
dict_to_node_type(node_types_data[0])
```

[child ⬇️](#62ccd67c-1542-4215-8ac3-81d905af856a)

---

(main branch ⎇)
###### 62ccd67c-1542-4215-8ac3-81d905af856a
[parent ⬆️](#61a16991-9ab7-4460-a1c6-a8b1a7370e7e)
