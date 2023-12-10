# Assistant

```python
# Importing required modules
from typing import Iterator
import textwrap
from tree_sitter import Node

# Function to generate the tree representation line by line
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
        yield from print_tree_generator(child, depth + 1, named_only)

# Function to print the tree
def print_tree(node: Node, named_only: bool=False) -> None:
    for ln in print_tree_generator(node, 0, named_only):
        print(ln)

# Sample Python code exploring a variety of syntax and features
sample_code = '''
# This is a comment
import os, sys
from math import sqrt

def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n-1)

class Sample:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def static_method():
        print("Static Method")

def main():
    # Lambda function
    square = lambda x: x ** 2
    print(square(4))

    # List comprehension
    even_numbers = [x for x in range(10) if x % 2 == 0]

    # Dict comprehension
    square_dict = {x: x ** 2 for x in range(5)}

if __name__ == "__main__":
    main()
'''

# Parsing the sample code
sample_tree = parser.parse(bytes(sample_code, "utf8"))

# Printing the tree
print_tree(sample_tree.root_node, named_only=True)
```

[child ⬇️](#01825802-2f92-4fc1-9bef-89687e0f4d61)

---

(main branch ⎇)
###### 01825802-2f92-4fc1-9bef-89687e0f4d61
[parent ⬆️](#9a5e885a-41d2-4136-9134-37555921bc14)
