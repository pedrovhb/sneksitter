# User

Please complete the function body implementation:

from __future__ import annotations

from dataclasses import dataclass
from textwrap import dedent as d

import rich
import tree_sitter_languages
from pydantic import Field, BaseModel

from codecranker.code_editing.utils import print_tree


class Model(BaseModel):
    class Config:
        populate_by_name = True
        # Forbid extra fields
        extra = "forbid"


class Parameter(Model):
    name: bytes = Field(..., description="The name (identifier) of the parameter.")
    type: bytes | None = Field(
        None,
        description="The type annotation of the parameter, the same as it was present in the code (if at all).",
    )
    default: bytes | None = Field(
        None,
        description="The default value of the parameter, if any.",
    )
    description: str | None = Field(
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
        """Create a parameter from a Tree-sitter node."""

    @classmethod
    def from_node_parameters(cls, node: Node) -> list[Parameter]:
        """Create a list of parameters from a Tree-sitter node."""
        if not node.type == "parameters":
            raise ValueError(f"Expected node of type 'parameters', got {node.type}")


@dataclass
class Function:
    name: str
    parameters: list[str]
    return_type: str
    docstring: str
    code: str


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
    """
    module                                   | def foo(*vararg: str, x, y=1, /, f="a string default", *, z: int=5, w:...
     function_definition                     | def foo(*vararg: str, x, y=1, /, f="a string default", *, z: int=5, w:...
      identifier                             | foo
      parameters                             | (*vararg: str, x, y=1, /, f="a string default", *, z: int=5, w:...
       typed_parameter                       | *vararg: str
        list_splat_pattern                   | *vararg
         identifier                          | vararg
        type                                 | str
         identifier                          | str
       identifier                            | x
       default_parameter                     | y=1
        identifier                           | y
        integer                              | 1
       positional_separator                  | /
       default_parameter                     | f="a string default"
        identifier                           | f
        string                               | "a string default"
       keyword_separator                     | *
       typed_default_parameter               | z: int=5
        identifier                           | z
        type                                 | int
         identifier                          | int
        integer                              | 5
       typed_default_parameter               | w: Callable[P, T]=print
        identifier                           | w
        type                                 | Callable[P, T]
         subscript                           | Callable[P, T]
          identifier                         | Callable
          identifier                         | P
          identifier                         | T
        identifier                           | print
       dictionary_splat_pattern              | **kwargs
        identifier                           | kwargs
      type                                   | int
       identifier                            | int
      block                                  | '''This is a docstring. Args: x: This is x z: This is z w: This is w...
       expression_statement                  | '''This is a docstring. Args: x: This is x z: This is z w: This is w...
        string                               | '''This is a docstring. Args: x: This is x z: This is z w: This is w...
       return_statement                      | return x + y
        binary_operator                      | x + y
         identifier                          | x
         identifier                          | y
     """
    console = rich.get_console()

    for ln in print_tree(tree.root_node, 0, True):
        console.print(ln)
    parameters = tree.root_node.children_by_field_name("function_definition")[
        0
    ].children_by_field_name("parameters")[0]
    print(parameters)  # <Node type=parameters, start_point=(0, 7), end_point=(0, 102)>



[child ⬇️](#57f72327-baa2-4d25-9b9f-a877fb819b45)

---

(other branch ⎇)
###### 57f72327-baa2-4d25-9b9f-a877fb819b45
[parent ⬆️](#aaa2f9b6-b863-4dda-ba08-c7b20cbbbd63)
