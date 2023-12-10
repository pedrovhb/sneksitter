# Assistant

```python
# Refining the extract_name function to correctly handle *vararg and **kwargs patterns
def extract_name(node: Node) -> bytes:
    if node.type in ['typed_parameter', 'default_parameter', 'typed_default_parameter']:
        identifier_nodes = [child for child in node.children if child.type == 'identifier']
        if identifier_nodes:
            return identifier_nodes[0].text

    elif node.type == 'list_splat_pattern' or node.type == 'dictionary_splat_pattern':
        identifier_nodes = [child for child in node.children if child.type == 'identifier']
        if identifier_nodes:
            return identifier_nodes[0].text

    return node.text if node.type == 'identifier' else b""

# Rerun the test to verify the changes
parsed_parameters = Parameter.from_node_parameters(parameters_node)
parsed_parameters_data = [vars(param) for param in parsed_parameters]
parsed_parameters_data
```

[child ⬇️](#199e263d-6e76-4ff1-9df0-57b81a1fc8ec)

---

(main branch ⎇)
###### 199e263d-6e76-4ff1-9df0-57b81a1fc8ec
[parent ⬆️](#34120d4f-e778-4097-a18f-03a87e4cb235)
