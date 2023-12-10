---
file: /home/pedro/Documents/chatgpt_export/Markdown/Parse ts-python-node-types JSON.md
heading_stack: <root> -> e99eb7ad-94e4-41d7-b226-2e95209438dc -> System -> f5218b62-0612-4055-a04f-15c2a4456b30 -> System -> aaa24a7d-6d79-4f2a-aa46-73a3895b401a -> User -> e2bcdb24-7d4d-4880-bc78-36cac65ea2b7 -> Assistant -> 3af7ae0b-c579-4d4a-90d3-732ef36c4077 -> Assistant -> 8d7a4cfc-4710-4160-b2cd-0ae6821ce860 -> Tool -> 4d1b6605-d6a7-4faf-a82b-dbdbcecc9118 -> Assistant -> aaa292e7-abf4-48a3-8ec5-c9395760f1df -> User -> 95e92a2a-1ecc-4d37-a231-440fb0df8742 -> Assistant -> 61a16991-9ab7-4460-a1c6-a8b1a7370e7e -> Assistant -> 62ccd67c-1542-4215-8ac3-81d905af856a -> Tool -> 3842346c-c97b-4398-8973-b03072176022 -> Assistant -> ae562db2-9408-4995-aff8-83204950a0e6 -> Assistant -> 48038f5b-5642-4239-92fc-ed7a2c2bbf2e -> Tool -> 86358309-252e-450f-82d1-f0b27959217b -> Assistant -> 5832b2f2-9f18-4013-9a6c-8fe0a4fbe805 -> Assistant -> 54b26d93-fb7f-4ce3-92f0-672c2459392a -> Tool -> f9f6837a-d02a-400d-8afe-f5b2250bb4bd -> Assistant -> 318c246e-abbf-433e-80b8-59b11912d7c9 -> Assistant
---
# Assistant

```python
from toolz import map

# Recursive function to convert dictionary to NodeType instance
def dict_to_node_type_recursive(node_dict):
    type_ = node_dict.get('type')
    named = node_dict.get('named', False)
    subtypes = node_dict.get('subtypes', [])
    
    # Recursively convert subtypes
    subtypes_instances = list(map(dict_to_node_type_recursive, subtypes))
    
    return NodeType(type_, named, subtypes_instances)

# Convert named and unnamed nodes to NodeType instances
named_nodes_instances = list(map(dict_to_node_type_recursive, named_nodes))
unnamed_nodes_instances = list(map(dict_to_node_type_recursive, unnamed_nodes))

# Display first instance to verify
named_nodes_instances[0]
```

[child ⬇️](#89778cd6-69e2-418c-8509-700ee06e2255)

---

(main branch ⎇)
###### 89778cd6-69e2-418c-8509-700ee06e2255
[parent ⬆️](#318c246e-abbf-433e-80b8-59b11912d7c9)
