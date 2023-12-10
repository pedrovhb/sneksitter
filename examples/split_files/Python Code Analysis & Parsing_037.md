# Tool

==== Cell ID: 6ed807e1-5a08-429d-ba11-aafcec31a39a
Cell Type: code
Cell State: finished_with_no_error
== Source ==
from typing import List, Optional, Union
from pydantic import BaseModel, Field
from tree_sitter import Node

class Function(Model):
    name: bytes = Field(..., description="The name of the function.")
    parameters: List[Parameter] = Field(..., description="List of parameters for the function.")
    return_type: Union[bytes, None] = Field(None, description="The return type of the function, if specified.")
    docstring: Union[str, None] = Field(None, description="The docstring of the function, if present.")
    body: bytes = Field(..., description="The body of the function.")

    @classmethod
    def from_node(cls, node: Node) -> Function:
        name = extract_name(node.children_by_field_name('name')[0])
        parameters_node = node.children_by_field_name('parameters')[0]
        parsed_parameters = Parameter.from_node_parameters(parameters_node)
        return_type_node = node.children_by_field_name('return_type')
        return_type = extract_type(return_type_node[0]) if return_type_node else None
        docstring_node = node.children_by_field_name('docstring')
        docstring = docstring_node[0].text if docstring_node else None
        body = node.children_by_field_name('body')[0].text
        return cls(name=name, parameters=parsed_parameters, return_type=return_type, docstring=docstring, body=body)


[child ⬇️](#b6950cd6-4256-4e9b-9ab2-ca473b944965)

---

(main branch ⎇)
###### b6950cd6-4256-4e9b-9ab2-ca473b944965
[parent ⬆️](#c88ab4d2-a949-405a-8f74-6e29ce5f2dfc)
