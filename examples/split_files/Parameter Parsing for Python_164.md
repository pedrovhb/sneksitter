# Assistant

```python
# Refining extract_name to navigate into child nodes for list_splat_pattern or dictionary_splat_pattern
def extract_name(node: Node) -> bytes:
    if node.type in ['typed_parameter', 'default_parameter', 'typed_default_parameter']:
        # Navigate into child nodes for more specific patterns
        special_pattern_nodes = [child for child in node.children if child.type in ['list_splat_pattern', 'dictionary_splat_pattern']]
        if special_pattern_nodes:
            return extract_name(special_pattern_nodes[0])
        else:
            identifier_nodes = [child for child in node.named_children if child.type == 'identifier']
            if identifier_nodes:
                return identifier_nodes[0].text

    elif node.type == 'list_splat_pattern' or node.type == 'dictionary_splat_pattern':
        identifier_nodes = [child for child in node.named_children if child.type == 'identifier']
        if identifier_nodes:
            return identifier_nodes[0].text

    return node.text if node.type == 'identifier' else b""

# Rerun the test to verify the changes
parsed_parameters = Parameter.from_node_parameters(parameters_node)
parsed_parameters_data = [vars(param) for param in parsed_parameters]
parsed_parameters_data
```

[child ⬇️](#61378b28-e70f-46b9-9600-f564576da799)

---

(main branch ⎇)
###### 61378b28-e70f-46b9-9600-f564576da799
[parent ⬆️](#4afd4aff-8d28-4e3b-8cca-2b9bf5e75475)
