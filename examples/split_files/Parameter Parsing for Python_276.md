# Assistant

```python
# Writing the final working version of the code to a file on disk
final_code_path = '/mnt/data/final_parameter_parsing.py'

final_code_content = """
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
        node_snippet = ""
    else:
        tree_repr = tree_repr.ljust(40, " ")
        node_snippet = textwrap.shorten(node.text.decode(), 80 - depth * 2, placeholder="...")
    if not named_only or node.is_named:
        yield f"{tree_repr} | {node_snippet}"
    for child in node.children:
        yield from print_tree(child, depth + 1, named_only)

if __name__ == "__main__":
    import tree_sitter_languages

    parser = tree_sitter_languages.get_parser("python")
    tree = parser.parse(
        d(
            '''
            def foo(*vararg: str, x, y=1, /, f="a string default", *, z: int=5, w: Callable[P, T]=print, **kwargs) -> int:
                """This is a docstring.
            
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
                """
                return x + y
            '''
        )
        .encode()
        .strip()
    )
    console = rich.get_console()
    for ln in print_tree(tree.root_node, 0, True):
        console.print(ln)
    parameters_node = tree.root_node.children_by_field_name("function_definition")[0].children_by_field_name("parameters")[0]
    parsed_parameters = Parameter.from_node_parameters(parameters_node)
    parsed_parameters_data = [vars(param) for param in parsed_parameters]
    print(parsed_parameters_data)
"""

# Saving the code to disk
with open(final_code_path, 'w') as f:
    f.write(final_code_content)

final_code_path
```

[child ⬇️](#b5add1c5-0f06-4dee-b1e9-72a399bfe0d0)

---

(other branch ⎇)
###### b5add1c5-0f06-4dee-b1e9-72a399bfe0d0
[parent ⬆️](#f79ab3a5-e379-41eb-ba7e-bc9cfaabceb9)
