# Assistant

{
  "file_id": "1239fdfa-f7ef-4d30-9dbb-5f6f61637677",
  "cell_type": "code",
  "source": [
    "from typing import List, Optional, Union",
    "from pydantic import BaseModel, Field",
    "from tree_sitter import Node",
    "\n",
    "class Function(Model):",
    "    name: bytes = Field(..., description=\"The name of the function.\")",
    "    parameters: List[Parameter] = Field(..., description=\"List of parameters for the function.\")",
    "    return_type: Union[bytes, None] = Field(None, description=\"The return type of the function, if specified.\")",
    "    docstring: Union[str, None] = Field(None, description=\"The docstring of the function, if present.\")",
    "    body: bytes = Field(..., description=\"The body of the function.\")",
    "\n",
    "    @classmethod",
    "    def from_node(cls, node: Node) -> Function:",
    "        name = extract_name(node.children_by_field_name('name')[0])",
    "        parameters_node = node.children_by_field_name('parameters')[0]",
    "        parsed_parameters = Parameter.from_node_parameters(parameters_node)",
    "        return_type_node = node.children_by_field_name('return_type')",
    "        return_type = extract_type(return_type_node[0]) if return_type_node else None",
    "        docstring_node = node.children_by_field_name('docstring')",
    "        docstring = docstring_node[0].text if docstring_node else None",
    "        body = node.children_by_field_name('body')[0].text",
    "        return cls(name=name, parameters=parsed_parameters, return_type=return_type, docstring=docstring, body=body)"
  ]
}

[child ⬇️](#c4c27846-6e0a-47d8-8aab-ab14fbda0d8c)

---

(main branch ⎇)
###### c4c27846-6e0a-47d8-8aab-ab14fbda0d8c
[parent ⬆️](#b2c70be9-2d0f-428b-be57-aef658e7da45)
