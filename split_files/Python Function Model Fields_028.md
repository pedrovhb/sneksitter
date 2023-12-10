---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Function Model Fields.md
heading_stack: <root> -> fc21465c-83b3-4590-acfe-f9d5a0b572a2 -> System -> cb3c4449-2fc8-4ce1-92fe-9a4f04da2133 -> System -> aaa21556-5253-4a46-a033-9f889d8f4fe6 -> User -> d61e28b4-86e0-47ae-a9f7-3ac02d241d40 -> Assistant -> aaa23a57-506a-4481-9176-60c22bd16ebf -> User -> 80d1fe06-a661-4cfe-834d-cc0c0f73ed70 -> Assistant -> aaa2cba1-09a9-4470-b1b7-d9847cf69842 -> User -> 557b8e25-f737-466e-880c-7323000b11c9 -> Assistant -> aaa2ecf2-c237-44f1-a584-88b71182ed75 -> User -> 3c2727b5-66c7-4eab-bd7d-3c0c192b1b09 -> Assistant -> aaa272c5-3631-4746-a0f3-1619a476f340 -> User -> 5f2e0949-a723-4535-9ada-f9932c1a4bae -> Assistant -> aaa20811-98a3-494a-a4dc-3768de5c0e76 -> User -> 7bd61e3a-f994-446f-a4d0-8192038b381c -> Assistant
---
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