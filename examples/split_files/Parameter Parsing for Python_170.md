# Assistant

```python
# Refining the extract_default function to correctly extract default values
def extract_default(node: Node) -> Optional[bytes]:
    default_nodes = [child for child in node.children if child.type == 'default_parameter' or child.type == 'typed_default_parameter']
    if default_nodes:
        actual_default_nodes = [child for child in default_nodes[0].children if child.type not in ['identifier', ':', '=']]
        if actual_default_nodes:
            return actual_default_nodes[0].text
    return None

# Updating the from_node_parameters method to correctly identify *vararg and **kwargs patterns
class Parameter(Parameter):
    @classmethod
    def from_node_parameters(cls, node: Node) -> List['Parameter']:
        parameters = []
        saw_positional_separator = False
        saw_keyword_separator = False

        # Filtering out irrelevant nodes
        relevant_child_nodes = [
            child for child in node.children if child.type not in ['(', ')', ',']
        ]

        for child in relevant_child_nodes:
            if child.type == 'positional_separator':
                saw_positional_separator = True
                continue
            elif child.type == 'keyword_separator':
                saw_keyword_separator = True
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

# Rerun the test to verify the changes
parsed_parameters = Parameter.from_node_parameters(parameters_node)
parsed_parameters_data = [vars(param) for param in parsed_parameters]
parsed_parameters_data
```

[child ⬇️](#02d68261-9bdb-4c46-950d-170d04e561b8)

---

(main branch ⎇)
###### 02d68261-9bdb-4c46-950d-170d04e561b8
[parent ⬆️](#d67bf523-10b1-4105-b238-1138298a0791)
