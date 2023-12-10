# Also, the 'docstring' seems to be incorrect.
class Function(BaseModel):
    name: str
    parameters: List[Parameter]
    return_type: Optional[str]
    docstring: Optional[str]
    body: Optional[str]

    @classmethod
    def from_node(cls, node: Node) -> 'Function':
        name = extract_name(node.children_by_field_name('name')[0])
        if name is not None:
            name = name.decode('utf-8')
        parameters_node = node.children_by_field_name('parameters')[0]
        parsed_parameters = Parameter.from_node_parameters(parameters_node)
        return_type_node = node.children_by_field_name('return_type')
        return_type = None
        if return_type_node:
            return_type = extract_type(return_type_node[0])
            if return_type is not None:
                return_type = return_type.decode('utf-8')
        docstring_node = node.children_by_field_name('docstring')
        docstring = None
        if docstring_node:
            docstring = docstring_node[0].text
            if docstring is not None:
                docstring = docstring.decode('utf-8')
        body_node = node.children_by_field_name('body')[0]
        body = body_node.text if body_node else None
        if body is not None:
            body = body.decode('utf-8')
        return cls(name=name, parameters=parsed_parameters, return_type=return_type, docstring=docstring, body=body)


[child ⬇️](#c649201f-1195-41af-be28-44c1bc8fadbf)

---

(main branch ⎇)
###### c649201f-1195-41af-be28-44c1bc8fadbf
[parent ⬆️](#e563104f-ff7e-4ca5-9f86-7f8aba8a7e92)
