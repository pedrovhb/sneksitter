# Assistant

```python
# Debugging: Investigating the child node for list_splat_pattern in *vararg to see why name is not being captured
vararg_list_splat_node = [child for child in vararg_node.children if child.type == 'list_splat_pattern'][0]
vararg_list_splat_node.children, [n.type for n in vararg_list_splat_node.children]
```

[child ⬇️](#50b823cc-1951-4c42-9e67-f523d98dc7c3)

---

(main branch ⎇)
###### 50b823cc-1951-4c42-9e67-f523d98dc7c3
[parent ⬆️](#9a1141b0-2f51-480e-811b-b77947566fc6)
