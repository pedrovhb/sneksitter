---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Function Model Fields.md
heading_stack: <root> -> fc21465c-83b3-4590-acfe-f9d5a0b572a2 -> System -> cb3c4449-2fc8-4ce1-92fe-9a4f04da2133 -> System -> aaa21556-5253-4a46-a033-9f889d8f4fe6 -> User -> d61e28b4-86e0-47ae-a9f7-3ac02d241d40 -> Assistant -> aaa23a57-506a-4481-9176-60c22bd16ebf -> User -> 80d1fe06-a661-4cfe-834d-cc0c0f73ed70 -> Assistant -> aaa2cba1-09a9-4470-b1b7-d9847cf69842 -> User -> 557b8e25-f737-466e-880c-7323000b11c9 -> Assistant
---
# Assistant

Certainly, here's the code for creating a `Function` model and extracting it from the Tree Sitter nodes:

```python
from __future__ import annotations
from typing import Optional, List, Union
from dataclasses import dataclass, field
from tree_sitter import Node

@dataclass
class Parameter:
    name: bytes
    type: Optional[bytes] = None
    default: Optional[bytes] = None
    description: Optional[str] = None
    is_vararg: bool = False
    is_kwarg: bool = False
    is_positional_only: bool = False
    is_keyword_only: bool = False

@dataclass
class Function:
    name: bytes
    parameters: List[Parameter]
    return_type: Optional[bytes] = None
    docstring: Optional[str] = None

    @classmethod
    def from_node(cls, node: Node) -> Function:
        name = extract_name(node)
        parameters_node = node.children_by_field_name("parameters")[0]
        parsed_parameters = Parameter.from_node_parameters(parameters_node)
        return_type = extract_return_type(node)
        docstring = extract_docstring(node)
        return cls(name, parsed_parameters, return_type, docstring)

def extract_name(node: Node) -> bytes:
    name_nodes = [child for child in node.children if child.type == 'identifier']
    if name_nodes:
        return name_nodes[0].text
    return b""

def extract_return_type(node: Node) -> Optional[bytes]:
    return_type_nodes = [child for child in node.children if child.type == 'type']
    if return_type_nodes:
        return return_type_nodes[0].text
    return None

def extract_docstring(node: Node) -> Optional[str]:
    docstring_nodes = [child for child in node.children if child.type == 'string']
    if docstring_nodes:
        # Extract the text content within the docstring nodes
        docstring_content = b"".join(child.text for child in docstring_nodes)
        # Remove leading/trailing triple-quotes and decode as UTF-8
        return docstring_content[3:-3].decode("utf-8")
    return None

# Example usage:
if __name__ == "__main__":
    # Assuming you already have the 'tree' variable from your previous code
    function_node = tree.root_node.children_by_field_name("function_definition")[0]
    parsed_function = Function.from_node(function_node)
    print(parsed_function)
```

This code defines a `Parameter` class and a `Function` class, along with methods for extracting relevant information from Tree Sitter nodes. You can use the `Function.from_node()` method to create a `Function` instance from a function node in the Tree Sitter tree.

---

(main branch ⎇)
###### aaa2ecf2-c237-44f1-a584-88b71182ed75
[parent ⬆️](#d61e28b4-86e0-47ae-a9f7-3ac02d241d40)
