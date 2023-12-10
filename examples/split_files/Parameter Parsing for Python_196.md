# Assistant

```python
# Debugging: Investigating the node structure for a typed_default_parameter to understand why the default value is capturing type annotations
typed_default_param_node = [child for child in parameters_node.children if child.type == 'typed_default_parameter'][0]
list(print_tree(typed_default_param_node, 0, True))
```

[child ⬇️](#0120392d-3102-406d-9751-6e497ac377d2)

---

(main branch ⎇)
###### 0120392d-3102-406d-9751-6e497ac377d2
[parent ⬆️](#9e02be39-2e7d-40c6-9608-567daca6cba6)
