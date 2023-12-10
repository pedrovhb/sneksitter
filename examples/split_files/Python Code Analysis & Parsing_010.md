# Tool

Notebook ID: 1239fdfa-f7ef-4d30-9dbb-5f6f61637677
Notebook Name: Tree sitter reconstruction.ipynb

==== Cell ID: 88e978fe
Cell Type: code
Cell State: finished_with_no_error
== Source ==
%pip install pydantic tree_sitter_languages -q

== Output ==
Note: you may need to restart the kernel to use updated packages.

==== Cell ID: a65f53d1-0b95-4f23-a1f9-af5d4ad46047
Cell Type: code
Cell State: finished_with_no_error
== Source ==
from __future__ import annotations
from dataclasses import dataclass
from textwrap import dedent as d
from typing import Optional, Union, List
import rich
import tree_sitter_languages
from pydantic import Field, BaseModel
from tree_sitter import Node

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
        node: Node,
        description: str | None = None,
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
    def from_node_parameters(cls, node: Node) -> list[Parameter]:
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

def extract_name(node: Node) -> bytes:
    name_nodes = [child for child in node.children if child.type == 'identifier']
    if name_nodes:
        return name_nodes[0].text
    return b""

def extract_type(node: Node) -> Optional[bytes]:
    type_nodes = [child for child in node.children if child.type == 'type']
    if type_nodes:
        return type_nodes[0].text
    return None

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

if __name__ == "__main__":
    parser = tree_sitter_languages.get_parser("python")
    tree = parser.parse(
        d(
            """
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
            """
        )
        .encode()
        .strip()
    )

    parameters_node = tree.root_node.children_by_field_name("function_definition")[0].children_by_field_name("parameters")[0]
    parsed_parameters = Parameter.from_node_parameters(parameters_node)
    parsed_parameters_data = [vars(param) for param in parsed_parameters]
    print(parsed_parameters_data)

== Output ==
[{'name': b'', 'type': b'str', 'default': None, 'description': None, 'is_vararg': True, 'is_kwarg': False, 'is_positiona
l_only': False, 'is_keyword_only': False}, {'name': b'', 'type': None, 'default': None, 'description': None, 'is_vararg'
: False, 'is_kwarg': False, 'is_positional_only': False, 'is_keyword_only': False}, {'name': b'y', 'type': None, 'defaul
t': b'1', 'description': None, 'is_vararg': False, 'is_kwarg': False, 'is_positional_only': False, 'is_keyword_only': Fa
lse}, {'name': b'f', 'type': None, 'default': b'"a string default"', 'description': None, 'is_vararg': False, 'is_kwarg'
: False, 'is_positional_only': True, 'is_keyword_only': False}, {'name': b'z', 'type': b'int', 'default': b'5', 'descrip
tion': None, 'is_vararg': False, 'is_kwarg': False, 'is_positional_only': False, 'is_keyword_only': True}, {'name': b'w'
, 'type': b'Callable[P, T]', 'default': b'print', 'description': None, 'is_vararg': False, 'is_kwarg': False, 'is_positi
onal_only': False, 'is_keyword_only': True}, {'name': b'kwargs', 'type': None, 'default': None, 'description': None, 'is
_vararg': False, 'is_kwarg': True, 'is_positional_only': False, 'is_keyword_only': True}]

Kernel State: idle (Kernel is ready for input)


[child ⬇️](#79181316-3c09-4844-8300-7e43ccd3f8a1)

---

(main branch ⎇)
###### 79181316-3c09-4844-8300-7e43ccd3f8a1
[parent ⬆️](#57cd8fdb-661b-4e6a-89bc-77d3c8237b3f)
