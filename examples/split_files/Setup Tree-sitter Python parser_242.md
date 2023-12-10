# User

That still kind of blows. I had to fetch the code I already had. How could I have instructed you better to create something like this?

Here's another bone - 

def print_tree_generator(node: Node, depth: int, named_only: bool=False) -> Iterator[str]:

    tree_repr = " " * depth + f"{node.type}"
    if node.type == node.text.decode():
        node_snippet = ""
    else:
        tree_repr = tree_repr.ljust(40, " ")
        node_snippet = textwrap.shorten(node.text.decode(), 80 - depth * 2, placeholder="...")

    if not named_only or node.is_named:
        # Print the node type and its snippet
        yield f"{tree_repr} | {node_snippet}"

    for child in node.children:
        yield from print_tree(child, depth + 1, named_only)

def print_tree(node: Node, named_only: bool=False) -> None:
    for ln in print_tree(node, 0, named_only):
        print(ln)

[child ⬇️](#88717108-02ce-4e3f-aaeb-f0f85f8008ec)

---

(other branch ⎇)
###### 88717108-02ce-4e3f-aaeb-f0f85f8008ec
[parent ⬆️](#aaa26191-9f9e-4267-bb3f-8dde3c0082cc)
