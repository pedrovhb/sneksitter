# Assistant

```python
# Debugging: Investigating the node structure for the default_parameter for parameter f to understand why the default value is not captured
default_param_node_f = [child for child in parameters_node.children if child.type == 'default_parameter' and b'f' in child.text][0]
list(print_tree(default_param_node_f, 0, True))
```

[child ⬇️](#8ecec0ff-8a0d-42dd-a392-65a977d7ae78)

---

(main branch ⎇)
###### 8ecec0ff-8a0d-42dd-a392-65a977d7ae78
[parent ⬆️](#e113d7e5-8570-499e-9172-c70b21651ad2)
