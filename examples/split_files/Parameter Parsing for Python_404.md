# Assistant

```python
# Skipping separators like '/' and '*' when building the parameters list in from_node_parameters
from typing import Iterator

def print_tree(node: Node, depth: int, named_only: bool = False) -> Iterator[str]:
    tree_repr = " " * depth + f"{node.type}"
    if node.type == node.text.decode():
        node_snippet = ""
    else:
        tree_repr = tree_repr.ljust(40, " ")
        node_snippet = node.text.decode()[:40].replace('\n', '\\n')

    if not named_only or node.is_named:
        yield f"{tree_repr} | {node_snippet}"

    for child in node.children:
        yield from print_tree(child, depth + 1, named_only)

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

        param = cls.from_node(child)

        if param.name is None:
            continue

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

[child ⬇️](#2fee69ae-a692-47df-87c3-a736556d476e)

---

(other branch ⎇)
###### 2fee69ae-a692-47df-87c3-a736556d476e
[parent ⬆️](#6345b2c5-052f-468d-b885-45d929cd3ce5)
