# Assistant

```python
# Updating the from_node_parameters method to filter out irrelevant nodes
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

            if child.type == 'list_splat_pattern':
                param.is_vararg = True
            elif child.type == 'dictionary_splat_pattern':
                param.is_kwarg = True

            parameters.append(param)

        return parameters

# Rerun the test to verify the changes
parsed_parameters = Parameter.from_node_parameters(parameters_node)
parsed_parameters_data = [vars(param) for param in parsed_parameters]
parsed_parameters_data
```

[child ⬇️](#dcf1fac9-70fa-4f5d-8e4f-05066363c068)

---

(main branch ⎇)
###### dcf1fac9-70fa-4f5d-8e4f-05066363c068
[parent ⬆️](#09c8e042-b8b8-4ef8-8cdb-84825e97ec17)
