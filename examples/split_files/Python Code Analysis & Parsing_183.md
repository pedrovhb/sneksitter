# Assistant

{
  "file_id": "1239fdfa-f7ef-4d30-9dbb-5f6f61637677",
  "cell_type": "code",
  "and_run": true,
  "source": [
    "# Update the Function model's from_node method to correctly extract the 'name' and 'docstring'",
    "class Function(BaseModel):",
    "    name: str",
    "    parameters: List[Parameter]",
    "    return_type: Optional[str]",
    "    docstring: Optional[str]",
    "    body: Optional[str]",
    "    \n",
    "    @classmethod",
    "    def from_node(cls, node: Node) -> 'Function':",
    "        name_node = [child for child in node.children if child.type == 'identifier'][0]",
    "        name = name_node.text.decode('utf-8')",
    "        parameters_node = node.children_by_field_name('parameters')[0]",
    "        parsed_parameters = Parameter.from_node_parameters(parameters_node)",
    "        return_type_node = node.children_by_field_name('return_type')",
    "        return_type = None",
    "        if return_type_node:",
    "            return_type = extract_type(return_type_node[0])",
    "            if return_type is not None:",
    "                return_type = return_type.decode('utf-8')",
    "        block_node = [child for child in node.children if child.type == 'block'][0]",
    "        docstring_node = block_node.children[0] if block_node.children and block_node.children[0].type == 'string' else None",
    "        docstring = docstring_node.text.decode('utf-8') if docstring_node else None",
    "        body_node = block_node.children[1] if len(block_node.children) > 1 else None",
    "        body = body_node.text.decode('utf-8') if body_node else None",
    "        return cls(name=name, parameters=parsed_parameters, return_type=return_type, docstring=docstring, body=body)"
  ]
}

[child ⬇️](#87f5765d-1f04-4a00-a146-d1eb426ad577)

---

(main branch ⎇)
###### 87f5765d-1f04-4a00-a146-d1eb426ad577
[parent ⬆️](#f95544af-4f79-4bc4-b3b5-d63ebbaff27e)
