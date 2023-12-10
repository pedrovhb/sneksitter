# Assistant

```python
# Debugging the extract_default function to understand why it's not capturing the default value for parameter f
actual_default_nodes_f = [child for child in default_param_node_f.children if child.type not in ['identifier', ':', '=', 'type'] and len(child.children) == 0]
actual_default_nodes_f
```

[child ⬇️](#c3e47d86-5a6c-444e-8afc-a3cadb9d6af5)

---

(main branch ⎇)
###### c3e47d86-5a6c-444e-8afc-a3cadb9d6af5
[parent ⬆️](#4205963f-c5ec-4fb9-8e56-c8e558f24b4a)
