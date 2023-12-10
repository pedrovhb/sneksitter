# Assistant

```python
# Refining extract_default to be more permissive in capturing default values
def extract_default(node: Node) -> Optional[bytes]:
    if node.type in ['default_parameter', 'typed_default_parameter']:
        # Find the last child that is not an identifier, :, or =
        actual_default_nodes = [child for child in node.children if child.type not in ['identifier', ':', '=']]
        if actual_default_nodes:
            return actual_default_nodes[-1].text
    else:
        default_nodes = [child for child in node.children if child.type == 'default_parameter' or child.type == 'typed_default_parameter']
        if default_nodes:
            actual_default_nodes = [child for child in default_nodes[0].children if child.type not in ['identifier', ':', '=']]
            if actual_default_nodes:
                return actual_default_nodes[-1].text
    return None

# Rerun the test to verify the changes
parsed_parameters = Parameter.from_node_parameters(parameters_node)
parsed_parameters_data = [vars(param) for param in parsed_parameters]
parsed_parameters_data
```

[child ⬇️](#7cb3c312-7695-43bb-8b21-d9b6885a07ea)

---

(main branch ⎇)
###### 7cb3c312-7695-43bb-8b21-d9b6885a07ea
[parent ⬆️](#c79bf822-b9c9-4480-8990-a4579d6ed52e)
