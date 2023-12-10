# Update the Function model to correctly handle the fields
from pydantic import BaseModel, Field
from typing import List, Optional

class Function(BaseModel):
    name: str = Field(..., description='The name of the function')
    parameters: List[Parameter] = Field(..., description='List of parameters')
    return_type: Optional[str] = Field(None, description='The return type of the function')
    docstring: Optional[str] = Field(None, description='The docstring of the function')
    body: Optional[str] = Field(None, description='The body of the function')

    @classmethod
    def from_node(cls, node: Node) -> 'Function':
        name = extract_name(node.children_by_field_name('name')[0])
        parameters_node = node.children_by_field_name('parameters')[0]
        parsed_parameters = Parameter.from_node_parameters(parameters_node)
        return_type_node = node.children_by_field_name('return_type')
        return_type = extract_type(return_type_node[0]) if return_type_node else None
        docstring_node = node.children_by_field_name('docstring')
        docstring = docstring_node[0].text if docstring_node else None
        body_node = node.children_by_field_name('body')[0]
        body = body_node.text if body_node else None
        return cls(name=name, parameters=parsed_parameters, return_type=return_type, docstring=docstring, body=body)


[child ⬇️](#02dc68b7-ca2f-49dd-bb6c-9316d2f77b27)

---

(main branch ⎇)
###### 02dc68b7-ca2f-49dd-bb6c-9316d2f77b27
[parent ⬆️](#87993161-9de5-4c83-949a-fa005d058508)
