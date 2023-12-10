# Assistant

```python
# Reconstructing the final code content and dedenting it
final_code_content_fixed = textwrap.dedent("""
from __future__ import annotations
from dataclasses import dataclass
from textwrap import dedent as d
from typing import Union, Optional, Iterator
import textwrap
import rich
import tree_sitter
from pydantic import BaseModel, Field

class Model(BaseModel):
    class Config:
        extra = "forbid"

class Parameter(Model):
    name: bytes = Field(..., description="The name (identifier) of the parameter.")
    type: Union[bytes, None] = Field(
        None,
        description="The type annotation of the parameter, the same as it was present in the code (if at all).",
    )
    default: Union[bytes, None] = Field(
        None,
        description="The default value of the parameter, if any.",
    )
    description: Union[str, None] = Field(
        None,
        description="The description of the parameter, from the docstring.",
    )
    is_vararg: bool = Field(
        False,
        description="Whether the parameter is a vararg (e.g. *args).",
    )
    is_kwarg: bool = Field(
        False,
        description="Whether the parameter is a kwarg (e.g. **kwargs).",
    )
    is_positional_only: bool = Field(
        False,
        description="Whether the parameter is positional only (e.g. def foo(x, /, y)).",
    )
    is_keyword_only: bool = Field(
        False,
        description="Whether the parameter is keyword only (e.g. def foo(*, x)).",
    )

    @classmethod
    def from_node(
        cls,
        node: tree_sitter.Node,
        description: Union[str, None] = None,
    ) -> Parameter:
        def extract_name(node: tree_sitter.Node) -> bytes:
            identifier_nodes = [child for child in node.children if child.type == 'identifier']
            return identifier_nodes[0].text if identifier_nodes else None

        def extract_type(node: tree_sitter.Node) -> Union[bytes, None]:
            type_nodes = [child for child in node.children if child.type == 'type']
            return type_nodes[0].text if type_nodes else None

        def extract_default(node: tree_sitter.Node) -> Union[bytes, None]:
            if node.type in ['default_parameter', 'typed_default_parameter']:
                actual_default_nodes = [child for i, child in enumerate(node.children) if child.type not in ['identifier', ':', '='] or (i > 0 and child.type == 'identifier')]
                if actual_default_nodes:
                    return actual_default_nodes[-1].text
            else:
                default_nodes = [child for child in node.children if child.type == 'default_parameter' or child.type == 'typed_default_parameter']
                if default_nodes:
                    actual_default_nodes = [child for i, child in enumerate(default_nodes[0].children) if child.type not in ['identifier', ':', '='] or (i > 0 and child.type == 'identifier')]
                    if actual_default_nodes:
                        return actual_default_nodes[-1].text
            return None

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
    def from_node_parameters(cls, node: tree_sitter.Node) -> list[Parameter]:
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

def print_tree(node: tree_sitter.Node, depth: int, named_only: bool=False) -> Iterator[str]:
    tree_repr = " " * depth + f"{node.type}"
    if node.type == node.text.decode():
        node_snippet
```

[child ⬇️](#dd5c107e-104e-47c8-a5d6-0c97865621df)

---

(other branch ⎇)
###### 80e4d4bb-cc26-4d75-8ea8-c3c7b6ef11aa
[parent ⬆️](#aaa2888c-83fa-41af-b915-d378cf78013a)
### System

[child ⬇️](#c04d4f5a-21f3-4701-b5c4-4283fbe8689f)

---

(other branch ⎇)
###### c04d4f5a-21f3-4701-b5c4-4283fbe8689f
[parent ⬆️](#80e4d4bb-cc26-4d75-8ea8-c3c7b6ef11aa)
