# It appears that the 'name' and 'return_type' fields are not being extracted correctly.
class Function(Model):
    @classmethod
    def from_node(cls, node: Node) -> Function:
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


[child ⬇️](#c0b2fed6-0fe7-4952-a701-180e261cffd1)

---

(main branch ⎇)
###### c0b2fed6-0fe7-4952-a701-180e261cffd1
[parent ⬆️](#7ce330cf-198f-4c4c-b682-b71b191c27d3)
