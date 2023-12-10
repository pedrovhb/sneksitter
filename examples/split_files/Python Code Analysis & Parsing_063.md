# Assistant

{
  "file_id": "1239fdfa-f7ef-4d30-9dbb-5f6f61637677",
  "cell_type": "code",
  "source": [
    "# Update the Function model's from_node method to fix the issues",
    "class Function(Model):",
    "    @classmethod",
    "    def from_node(cls, node: Node) -> Function:",
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

[child ⬇️](#7e8c3231-0fb3-41bc-b556-039781e70f40)

---

(main branch ⎇)
###### 7e8c3231-0fb3-41bc-b556-039781e70f40
[parent ⬆️](#3e77e6e6-4ea4-4713-91b0-a7320224d3f5)
