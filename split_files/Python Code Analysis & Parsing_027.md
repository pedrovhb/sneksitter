---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Code Analysis & Parsing.md
heading_stack: <root> -> 22b00ae7-9cb2-4df5-9eee-d07991dcb909 -> System -> 20ebaef2-02d6-4890-a642-e0f29f17805b -> System -> aaa2cafe-8b89-4a61-8a81-7ae5b849a3d4 -> User -> 9440ae93-53d9-4599-a08c-4f481da5db27 -> Assistant -> 57cd8fdb-661b-4e6a-89bc-77d3c8237b3f -> Tool -> 79181316-3c09-4844-8300-7e43ccd3f8a1 -> Assistant -> Cell 1 -> Cell 2 -> Observations: -> aaa2a124-a531-49d7-abf1-6bff71ae059e -> User -> f39d6ca7-8490-47d0-87ef-7295db56ee72 -> Assistant -> 4638e5fb-7316-4f3d-875b-e70772997c48 -> Tool -> c7d28657-3cf6-4f25-9465-6819041068f4 -> Assistant -> aaa21996-ce1a-4550-baea-bb77183194f1 -> User -> b2c70be9-2d0f-428b-be57-aef658e7da45 -> Assistant
---
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
