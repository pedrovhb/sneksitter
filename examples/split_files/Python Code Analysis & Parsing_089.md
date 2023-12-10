# Assistant

{
  "file_id": "1239fdfa-f7ef-4d30-9dbb-5f6f61637677",
  "cell_type": "code",
  "and_run": true,
  "source": [
    "# Update the Function model to correctly handle the fields",
    "from pydantic import BaseModel, Field",
    "from typing import List, Optional",
    "\n",
    "class Function(BaseModel):",
    "    name: str = Field(..., description='The name of the function')",
    "    parameters: List[Parameter] = Field(..., description='List of parameters')",
    "    return_type: Optional[str] = Field(None, description='The return type of the function')",
    "    docstring: Optional[str] = Field(None, description='The docstring of the function')",
    "    body: Optional[str] = Field(None, description='The body of the function')",
    "\n",
    "    @classmethod",
    "    def from_node(cls, node: Node) -> 'Function':",
    "        name = extract_name(node.children_by_field_name('name')[0])",
    "        parameters_node = node.children_by_field_name('parameters')[0]",
    "        parsed_parameters = Parameter.from_node_parameters(parameters_node)",
    "        return_type_node = node.children_by_field_name('return_type')",
    "        return_type = extract_type(return_type_node[0]) if return_type_node else None",
    "        docstring_node = node.children_by_field_name('docstring')",
    "        docstring = docstring_node[0].text if docstring_node else None",
    "        body_node = node.children_by_field_name('body')[0]",
    "        body = body_node.text if body_node else None",
    "        return cls(name=name, parameters=parsed_parameters, return_type=return_type, docstring=docstring, body=body)"
  ]
}

[child ⬇️](#87993161-9de5-4c83-949a-fa005d058508)

---

(main branch ⎇)
###### 87993161-9de5-4c83-949a-fa005d058508
[parent ⬆️](#bd2f1d81-825a-403b-ab28-9b0fea8f2f23)
