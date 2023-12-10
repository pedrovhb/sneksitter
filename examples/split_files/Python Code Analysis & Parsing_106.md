# Assistant

{
  "file_id": "1239fdfa-f7ef-4d30-9dbb-5f6f61637677",
  "cell_type": "code",
  "and_run": true,
  "source": [
    "# Update the Function model's from_node method to fix the issues",
    "class Function(Model):",
    "    @classmethod",
    "    def from_node(cls, node: Node) -> Function:",
    "        name = extract_name(node.children_by_field_name('name')[0]).decode('utf-8')",
    "        parameters_node = node.children_by_field_name('parameters')[0]",
    "        parsed_parameters = Parameter.from_node_parameters(parameters_node)",
    "        return_type_node = node.children_by_field_name('return_type')",
    "        return_type = extract_type(return_type_node[0]).decode('utf-8') if return_type_node else None",
    "        docstring_node = node.children_by_field_name('docstring')",
    "        docstring = docstring_node[0].text.decode('utf-8') if docstring_node else None",
    "        body_node = node.children_by_field_name('body')[0]",
    "        body = body_node.text.decode('utf-8') if body_node else None",
    "        return cls(name=name, parameters=parsed_parameters, return_type=return_type, docstring=docstring, body=body)"
  ]
}

[child ⬇️](#8fea60c4-dff5-47d4-afdc-b40fc6e790b1)

---

(main branch ⎇)
###### 8fea60c4-dff5-47d4-afdc-b40fc6e790b1
[parent ⬆️](#05d2ac9c-2bd2-4ca9-8d69-6fb49ffc24db)
