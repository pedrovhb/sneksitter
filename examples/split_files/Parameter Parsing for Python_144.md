# User

Here's another bone - 

def print_tree(node: Node, depth: int, named_only: bool=False) -> Iterator[str]:

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


(use as:


    for ln in print_tree(tree.root_node, 0, True):
        print(ln)

[child ⬇️](#fd2bcbd7-d371-4e07-b328-a3479485a8c6)

---

(main branch ⎇)
###### fd2bcbd7-d371-4e07-b328-a3479485a8c6
[parent ⬆️](#aaa2993a-f7d3-40b4-9bd0-b7c2885e48a1)
