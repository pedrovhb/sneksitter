# Assistant

```python
# Debugging: Investigating the node structure for a default_parameter to understand why the default value is not being captured
default_param_node = [child for child in parameters_node.children if child.type == 'default_parameter'][0]
list(print_tree(default_param_node, 0, True))
```

[child ⬇️](#f66c07ad-357b-4c52-8164-022db85b6826)

---

(main branch ⎇)
###### f66c07ad-357b-4c52-8164-022db85b6826
[parent ⬆️](#14971085-266e-4e3d-87a1-6781f455aca2)
