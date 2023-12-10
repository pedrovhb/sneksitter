# Assistant

```python
# Further refining extract_default to correctly capture default values that are identifiers
def extract_default(node: Node) -> Optional[bytes]:
    if node.type in ['default_parameter', 'typed_default_parameter']:
        # Excluding identifiers only when they are the first child (i.e., the parameter name)
        actual_default_nodes = [child for i, child in enumerate(node.children) if child.type not in ['identifier', ':', '='] or (i > 0 and child.type == 'identifier')]
        if actual_default_nodes:
            return actual_default_nodes[-1].text
    else:
        default_nodes = [child for child in node.children if child.type == 'default_parameter' or child.type == 'typed_default_parameter']
        if default_nodes:
            actual_default_nodes = [child for i, child in enumerate(default_nodes[0].children) if child.type not in ['identifier', ':', '='] or (i > 0 and child.type == 'identifier')]
            if actual_default_nodes:
                return actual_default_nodes[-1].text
    return None

# Rerun the test to verify the changes
parsed_parameters = Parameter.from_node_parameters(parameters_node)
parsed_parameters_data = [vars(param) for param in parsed_parameters]
parsed_parameters_data
```

[child ⬇️](#d6ffb6ed-c94c-433e-be37-5604e3f5d2b6)

---

(main branch ⎇)
###### d6ffb6ed-c94c-433e-be37-5604e3f5d2b6
[parent ⬆️](#28d08a91-f7e0-4e7c-be45-eac28591ca40)
