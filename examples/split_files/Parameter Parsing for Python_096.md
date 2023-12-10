# Assistant

```python
# Debugging: Investigating the node structure for a *vararg parameter to understand why the name is not being captured
vararg_node = [child for child in parameters_node.children if child.type == 'typed_parameter'][0]
vararg_node.children, [n.type for n in vararg_node.children]
```

[child ⬇️](#d82ebf91-47f7-400a-9572-1537da9ed5ce)

---

(main branch ⎇)
###### d82ebf91-47f7-400a-9572-1537da9ed5ce
[parent ⬆️](#ebb12a39-38a9-4ed9-a83d-ba5778ca88c0)
