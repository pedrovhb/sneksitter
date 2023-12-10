# Assistant

```python
from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional
from tree_sitter import Node

class Model:
    class Config:
        extra = "forbid"

# Utility functions for extracting parameter attributes from tree_sitter Node objects
def extract_name(node: Node) -> bytes:
    if node.type in ['typed_parameter', 'default_parameter', 'typed_default_parameter']:
        special_pattern_nodes = [child for child in node.children if child.type in ['list_splat_pattern', 'dictionary_splat_pattern']]
        if special_pattern_nodes:
            return extract_name(special_pattern_nodes[0])
        else:
            identifier_nodes = [child for child in node.named_children if child.type == 'identifier']
            if identifier_nodes:
                return identifier_nodes[0].text
    elif node.type == 'list_splat_pattern' or node.type == 'dictionary_splat_pattern':
        identifier_nodes = [child for child in node.named_children if child.type == 'identifier']
        if identifier_nodes:
            return identifier_nodes[0].text
    return node.text if node.type == 'identifier' else b""

def extract_type(node: Node) -> Optional[bytes]:
    type_nodes = [child for child in node.children if child.type == 'type']
    if type_nodes:
        return type_nodes[0].text
    return None

def extract_default(node: Node) -> Optional[bytes]:
    if node.type in ['default_parameter', 'typed_default_parameter']:
        actual_default_nodes = [child for child in node.children if child.type not in ['identifier', ':', '=', 'type']]
        if actual_default_nodes:
            return actual_default_nodes[0].text
    else:
        default_nodes = [child for child in node.children if child.type == 'default_parameter' or child.type == 'typed_default_parameter']
        if default_nodes:
            actual_default_nodes = [child for child in default_nodes[0].children if child.type not in ['identifier', ':', '=', 'type']]
            if actual_default_nodes:
                return actual_default_nodes[0].text
    return None

# Parameter class definition
class Parameter(Model):
    name: bytes
    type: Optional[bytes] = None
    default: Optional[bytes] = None
    description: Optional[str] = None
    is_vararg: bool = False
    is_kwarg: bool = False
    is_positional_only: bool = False
    is_keyword_only: bool = False

    @classmethod
    def from_node(
        cls,
        node: Node,
        description: Optional[str] = None,
    ) -> Parameter:
        name = extract_name(node)
        type_annotation = extract_type(node)
        default_value = extract_default(node)
        return cls(
            name=name,
            type=type_annotation,
            default=default_value,
            description=description,
        )

    @classmethod
    def from_node_parameters(cls, node: Node) -> List[Parameter]:
        parameters = []
        saw_positional_separator = False
        saw_keyword_separator = False

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
```

[child ⬇️](#011485bb-e797-4127-802a-e6b41124a7c7)

---

(main branch ⎇)
###### 011485bb-e797-4127-802a-e6b41124a7c7
[parent ⬆️](#b0133221-151c-40f0-b0fc-c23ef3034cef)
