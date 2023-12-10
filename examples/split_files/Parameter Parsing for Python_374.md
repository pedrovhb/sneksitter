# Assistant

```python
# Fourth part of the code
final_code_content_part4 = textwrap.dedent("""
            if child.type == 'list_splat_pattern' or (child.type == 'typed_parameter' and any(c.type == 'list_splat_pattern' for c in child.children)):
                param.is_vararg = True
            elif child.type == 'dictionary_splat_pattern' or (child.type == 'typed_parameter' and any(c.type == 'dictionary_splat_pattern' for c in child.children)):
                param.is_kwarg = True

            parameters.append(param)

        return parameters

def print_tree(node: tree_sitter.Node, depth: int, named_only: bool=False) -> Iterator[str]:
    tree_repr = " " * depth + f"{node.type}"
    if node.type == node.text.decode():
        node_snippet = ""
    else:
        tree_repr = tree_repr.ljust(40, " ")
        node_snippet = textwrap.shorten(node.text.decode(), 80 - depth * 2, placeholder="...")
    if not named_only or node.is_named:
        yield f"{tree_repr} | {node_snippet}"
    for child in node.children:
        yield from print_tree(child, depth + 1, named_only)

if __name__ == '__main__':
    import tree_sitter_languages

    parser = tree_sitter_languages.get_parser('python')
    tree = parser.parse(
        d(
            '''
            def foo(*vararg: str, x, y=1, /, f="a string default", *, z: int=5, w: Callable[P, T]=print, **kwargs) -> int:
                """This is a docstring.

                Args:
                    x: This is x
                    z: This is z
                    w: This is w

                Returns:
                    The sum of x and y

                Raises:
                    ValueError: If x is negative

                Examples:
                    >>> foo(1, 2)
                    3
                """
                return x + y
            '''
        )
        .encode()
        .strip()
    )
    console = rich.get_console()
    for ln in print_tree(tree.root_node, 0, True):
        console.print(ln)
    parameters_node = tree.root_node.children_by_field_name('function_definition')[0].children_by_field_name('parameters')[0]
    parsed_parameters = Parameter.from_node_parameters(parameters_node)
    parsed_parameters_data = [vars(param) for param in parsed_parameters]
    print(parsed_parameters_data)
""")

# Appending the fourth part to disk
with open(final_code_path, 'a') as f:
    f.write(final_code_content_part4)

# Verifying that the code is complete and runnable
%run $final_code_path

final_code_path
```

[child ⬇️](#09512ad5-bcf8-4d81-aac8-07d0ef8778fe)

---

(other branch ⎇)
###### 09512ad5-bcf8-4d81-aac8-07d0ef8778fe
[parent ⬆️](#22aab3ee-3738-42a5-804a-ec953672c036)
