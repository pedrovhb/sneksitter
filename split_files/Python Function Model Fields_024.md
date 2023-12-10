---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Function Model Fields.md
heading_stack: <root> -> fc21465c-83b3-4590-acfe-f9d5a0b572a2 -> System -> cb3c4449-2fc8-4ce1-92fe-9a4f04da2133 -> System -> aaa21556-5253-4a46-a033-9f889d8f4fe6 -> User -> d61e28b4-86e0-47ae-a9f7-3ac02d241d40 -> Assistant -> aaa23a57-506a-4481-9176-60c22bd16ebf -> User -> 80d1fe06-a661-4cfe-834d-cc0c0f73ed70 -> Assistant -> aaa2cba1-09a9-4470-b1b7-d9847cf69842 -> User -> 557b8e25-f737-466e-880c-7323000b11c9 -> Assistant -> aaa2ecf2-c237-44f1-a584-88b71182ed75 -> User -> 3c2727b5-66c7-4eab-bd7d-3c0c192b1b09 -> Assistant -> aaa272c5-3631-4746-a0f3-1619a476f340 -> User -> 5f2e0949-a723-4535-9ada-f9932c1a4bae -> Assistant
---
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