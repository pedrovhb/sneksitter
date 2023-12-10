# Assistant

I apologize for the oversight. To properly extract the docstring from Tree Sitter nodes, you should navigate through the tree to find the relevant docstring nodes and concatenate their text. Here's the modified `extract_docstring` function:

```python
def extract_docstring(node: Node) -> Optional[str]:
    def find_string_nodes(node):
        # Recursively find all string nodes in the tree
        if node.type == 'string':
            return [node]
        string_nodes = []
        for child in node.children:
            string_nodes.extend(find_string_nodes(child))
        return string_nodes

    # Find all string nodes in the tree
    string_nodes = find_string_nodes(node)

    if string_nodes:
        # Concatenate the text of all found string nodes
        docstring_parts = [string_node.text for string_node in string_nodes]
        return '\n'.join(docstring_parts)

    return None
```

This modified function recursively traverses the Tree Sitter nodes and collects all string nodes, then concatenates their text to form the complete docstring. It should work properly for extracting docstrings associated with functions.

---
