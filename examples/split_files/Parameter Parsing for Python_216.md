# Assistant

```python
# Debugging: Investigating the node structure for the typed_default_parameter for parameter w to understand why the default value is not captured
typed_default_param_node_w = [child for child in parameters_node.children if child.type == 'typed_default_parameter' and b'w' in child.text][0]
list(print_tree(typed_default_param_node_w, 0, True))
```

[child ⬇️](#ac57c31b-45a3-4b99-a20c-d05368c637b1)

---

(main branch ⎇)
###### ac57c31b-45a3-4b99-a20c-d05368c637b1
[parent ⬆️](#77441818-ab4d-4f20-9816-659fcd3ce5c4)
