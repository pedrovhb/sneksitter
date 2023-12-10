# Assistant

Certainly, here's the code to define a `Function` model in the same style as the provided `Parameter` model and to extract it from Tree Sitter nodes:

```python
from __future__ import annotations
from typing import List, Optional, Union
from tree_sitter import Node
from pydantic import Field, BaseModel

class Function(Model):
    name: bytes = Field(..., description="The name (identifier) of the function.")
    parameters: List[Parameter] = Field(..., description="List of function parameters.")
    return_type: Optional[bytes] = Field(
        None,
        description="The return type annotation of the function, if any.",
    )
    docstring: Optional[str] = Field(
        None,
        description="The docstring associated with the function.",
    )

    @classmethod
    def from_node(
        cls,
        node: Node,
    ) -> Function:
        name_node = extract_name(node)
        parameters_node = node.children_by_field_name("parameters")[0]
        return_type = extract_return_type(node)
        docstring = extract_docstring(node)

        parameters = Parameter.from_node_parameters(parameters_node)

        return cls(
            name=name_node,
            parameters=parameters,
            return_type=return_type,
            docstring=docstring,
        )

def extract_return_type(node: Node) -> Optional[bytes]:
    return_type_nodes = [child for child in node.children if child.type == 'type']
    if return_type_nodes:
        return return_type_nodes[0].text
    return None

def extract_docstring(node: Node) -> Optional[str]:
    docstring_nodes = [child for child in node.children if child.type == 'string']
    if docstring_nodes:
        # Join multiple docstring parts into a single string
        docstring_parts = [child.text for child in docstring_nodes]
        return '\n'.join(docstring_parts)
    return None

# Example usage:
if __name__ == "__main__":
    # Parse the Python code
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

    # Extract function information
    function_node = tree.root_node.children_by_field_name("function_definition")[0]
    function_info = Function.from_node(function_node)
    print(vars(function_info))
```

This code defines a `Function` model and includes methods for extracting information from Tree Sitter nodes, including parameters as instances of the existing `Parameter` model.

[child 1 ⬇️](#aaa272c5-3631-4746-a0f3-1619a476f340) | [child 2 ⬇️](#aaa20811-98a3-494a-a4dc-3768de5c0e76)

---

(other branch ⎇)
###### aaa272c5-3631-4746-a0f3-1619a476f340
[parent ⬆️](#3c2727b5-66c7-4eab-bd7d-3c0c192b1b09)
