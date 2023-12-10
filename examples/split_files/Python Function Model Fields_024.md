# Assistant

I apologize for the oversight. To extract the docstring properly, we need to consider that docstrings can span multiple lines and may include escape sequences. Here's an updated `extract_docstring` function that should work correctly:

```python
import ast

def extract_docstring(node: Node) -> Optional[str]:
    docstring_nodes = [child for child in node.children if child.type == 'string']
    if docstring_nodes:
        docstring_parts = [child.text for child in docstring_nodes]
        # Join multiple docstring parts into a single string
        docstring = '\n'.join(docstring_parts)
        
        # Parse the docstring using Python's built-in ast module to handle escape sequences
        try:
            docstring_ast = ast.parse(docstring)
            if isinstance(docstring_ast, ast.Module) and len(docstring_ast.body) == 1:
                docstring_node = docstring_ast.body[0]
                if isinstance(docstring_node, ast.Expr) and isinstance(docstring_node.value, ast.Str):
                    return docstring_node.value.s
        except SyntaxError:
            pass  # Handle parsing errors gracefully
        
    return None
```

This updated `extract_docstring` function first joins the docstring parts into a single string. Then, it attempts to parse the docstring using Python's `ast` module, which handles escape sequences and provides a properly formatted docstring. If parsing is successful, it returns the parsed docstring; otherwise, it returns `None`.

---

(main branch ⎇)
###### aaa20811-98a3-494a-a4dc-3768de5c0e76
[parent ⬆️](#3c2727b5-66c7-4eab-bd7d-3c0c192b1b09)
