# Assistant

```python
# Refining extract_default to correctly identify and extract default value nodes for complex typed_default_parameter nodes
def extract_default(node: Node) -> Optional[bytes]:
    if node.type in ['default_parameter', 'typed_default_parameter']:
        # Directly process the node if it's already of the correct type
        actual_default_nodes = [child for child in node.children if child.type not in ['identifier', ':', '=', 'type'] and not child.has_children]
        if actual_default_nodes:
            return actual_default_nodes[0].text
    else:
        default_nodes = [child for child in node.children if child.type == 'default_parameter' or child.type == 'typed_default_parameter']
        if default_nodes:
            actual_default_nodes = [child for child in default_nodes[0].children if child.type not in ['identifier', ':', '=', 'type'] and not child.has_children]
            if actual_default_nodes:
                return actual_default_nodes[0].text
    return None

# Rerun the test to verify the changes
parsed_parameters = Parameter.from_node_parameters(parameters_node)
parsed_parameters_data = [vars(param) for param in parsed_parameters]
parsed_parameters_data
```

[child ⬇️](#188296f5-4a7f-4320-9045-42b963773f75)

---

(main branch ⎇)
###### 188296f5-4a7f-4320-9045-42b963773f75
[parent ⬆️](#78bc1e31-eb8a-4831-9c6b-4b07a6a85882)
