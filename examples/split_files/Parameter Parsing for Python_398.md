# Assistant

```python
# Redefining the entire code due to the state reset

from __future__ import annotations
from typing import Optional, Union, List
from pydantic import BaseModel, Field
from tree_sitter import Node

class Model(BaseModel):
    class Config:
        extra = "forbid"

class Parameter(Model):
    name: bytes = Field(..., description="The name (identifier) of the parameter.")
    type: Union[bytes, None] = Field(None, description="The type annotation of the parameter, the same as it was present in the code (if at all).")
    default: Union[bytes, None] = Field(None, description="The default value of the parameter, if any.")
    description: Union[str, None] = Field(None, description="The description of the parameter, from the docstring.")
    is_vararg: bool = Field(False, description="Whether the parameter is a vararg (e.g. *args).")
    is_kwarg: bool = Field(False, description="Whether the parameter is a kwarg (e.g. **kwargs).")
    is_positional_only: bool = Field(False, description="Whether the parameter is positional only (e.g. def foo(x, /, y)).")
    is_keyword_only: bool = Field(False, description="Whether the parameter is keyword only (e.g. def foo(*, x)).")

    @classmethod
    def from_node(cls, node: Node, description: str | None = None) -> Parameter:
        def extract_name(node: Node) -> Optional[bytes]:
            identifier_nodes = [child for child in node.children if child.type == 'identifier']
            return identifier_nodes[0].text if identifier_nodes else None

        def extract_type(node: Node) -> Optional[bytes]:
            type_nodes = [child for child in node.children if child.type == 'type']
            return type_nodes[0].text if type_nodes else None

        def extract_default(node: Node) -> Optional[bytes]:
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
    def from_node_parameters(cls, node: Node) -> List[Parameter]:
        parameters = []
        saw_positional_separator = False
        saw_keyword_separator = False

        relevant_child_nodes = [child for child in node.children if child.type not in ['(', ')', ',']]

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

# Testing the changes by parsing a sample function definition again
import tree_sitter_languages
from textwrap import dedent as d

parser = tree_sitter_languages.get_parser("python")
tree = parser.parse(d("""
    def foo(*vararg: str, x, y=1, /, f="a string default", *, z: int=5, w: Callable[P, T]=print, **kwargs) -> int:
        '''This is a docstring.

        Args:
            x: This is x
            z: This is z
            w: This is w

        Returns:
            The sum of x and y

        Raises:
            ValueError: If x is negative

        Examples:
            >>> foo(1, 2)
            3
        '''
        return x + y
""").encode().strip())

parameters_node = tree.root_node.children_by_field_name("function_definition")[0].children_by_field_name("parameters")[0]
parsed_parameters = Parameter.from_node_parameters(parameters_node)
parsed_parameters_data = [vars(param) for param in parsed_parameters]
parsed_parameters_data
```

[child ⬇️](#1613eac2-9f9d-4503-bc20-69e7dc7e4a8d)

---

(other branch ⎇)
###### 1613eac2-9f9d-4503-bc20-69e7dc7e4a8d
[parent ⬆️](#58a6a878-fee5-481b-aac7-15746ccf4e68)
