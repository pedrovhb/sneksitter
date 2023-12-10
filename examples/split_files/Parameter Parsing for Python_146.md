# Assistant

```python
# Importing textwrap for text manipulation
import textwrap
from typing import Iterator

# Defining the print_tree function for better debugging of the tree structure
def print_tree(node: Node, depth: int, named_only: bool=False) -> Iterator[str]:
    tree_repr = " " * depth + f"{node.type}"
    if node.type == node.text.decode():
        node_snippet = ""
    else:
        tree_repr = tree_repr.ljust(40, " ")
        node_snippet = textwrap.shorten(node.text.decode(), 80 - depth * 2, placeholder="...")

    if not named_only or node.is_named:
        # Print the node type and its snippet
        yield f"{tree_repr} | {node_snippet}"

    for child in node.children:
        yield from print_tree(child, depth + 1, named_only)

# Using the print_tree function to debug the structure of the typed_parameter node for *vararg
list(print_tree(vararg_node, 0, True))
```

[child ⬇️](#15facccd-4504-412a-935f-44f49e3fc6e4)

---

(main branch ⎇)
###### 15facccd-4504-412a-935f-44f49e3fc6e4
[parent ⬆️](#fd2bcbd7-d371-4e07-b328-a3479485a8c6)
