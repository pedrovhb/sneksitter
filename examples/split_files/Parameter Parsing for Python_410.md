# Assistant

```python
# Modify from_node_parameters to check if the node is a separator before attempting to instantiate a Parameter object.

@classmethod
def from_node_parameters(cls, node: Node) -> List[Parameter]:
    parameters = []
    saw_positional_separator = False
    saw_keyword_separator = False

    relevant_child_nodes = [child for child in node.children if child.type not in ['(', ')', ',']]

    for child in relevant_child_nodes:
        if child.type in ['positional_separator', 'keyword_separator']:
            if child.type == 'positional_separator':
                saw_positional_separator = True
            else:
                saw_keyword_separator = True
            continue

        # Skip instantiation if the node is a separator
        if child.type in ['positional_separator', 'keyword_separator']:
            continue

        param = cls.from_node(child)

        if saw_positional_separator and not saw_keyword_separator:
            param.is_positional_only = True
        elif saw_keyword_separator:
            param.is_keyword_only = True

        if child.type == 'list_splat_pattern' or (child.type == 'typed_parameter' and any(c.type == 'list_splat_pattern' for c in child.children)):
            param.is_vararg = True
        elif child.type == 'dictionary_splat_pattern' or (child.type == 'typed_parameter' and any(c.type == 'dictionary_splat_pattern' for c in child.children)):
            param.is_kwarg = True

        parameters.append(param)

    return parameters

# Setting the classmethod in the Parameter class
Parameter.from_node_parameters = from_node_parameters

# Rerun the test to verify the changes
parsed_parameters = Parameter.from_node_parameters(parameters_node)
parsed_parameters_data = [vars(param) for param in parsed_parameters]
parsed_parameters_data
```

[child ⬇️](#5bc1a8f1-1c65-4302-b54c-c7a5c2853de1)

---

(other branch ⎇)
###### 5bc1a8f1-1c65-4302-b54c-c7a5c2853de1
[parent ⬆️](#32c81f0b-3c93-45fe-8a5b-2d9dd95da0d5)
