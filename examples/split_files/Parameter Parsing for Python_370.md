# Assistant

```python
# Third part of the code
final_code_content_part3 = textwrap.dedent("""
        name = extract_name(node)
        type_annotation = extract_type(node)
        default_value = extract_default(node)
        return cls(
            name=name,
            type=type_annotation,
            default=default_value,
            description=description,
        )

    @classmethod
    def from_node_parameters(cls, node: tree_sitter.Node) -> list[Parameter]:
        parameters = []
        saw_positional_separator = False
        saw_keyword_separator = False

        relevant_child_nodes = [
            child for child in node.children if child.type not in ['(', ')', ',']
        ]

        for child in relevant_child_nodes:
            if child.type == 'positional_separator':
                saw_positional_separator = True
                continue
            elif child.type == 'keyword_separator':
                saw_keyword_separator = True
                continue

            param = cls.from_node(child)

            if saw_positional_separator and not saw_keyword_separator:
                param.is_positional_only = True
            elif saw_keyword_separator:
                param.is_keyword_only = True
""")

# Appending the third part to disk
with open(final_code_path, 'a') as f:
    f.write(final_code_content_part3)

final_code_path
```

[child ⬇️](#07f7685a-2bea-4d4f-b9d4-5cb4b8b9b926)

---

(other branch ⎇)
###### 07f7685a-2bea-4d4f-b9d4-5cb4b8b9b926
[parent ⬆️](#0f89934d-77c7-4f4b-8749-f7dbb640f31b)
