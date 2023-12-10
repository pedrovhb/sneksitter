# Assistant

```python
# Import the required modules and functions
from tree_sitter import Node
from typing import Iterator
import textwrap

# Get the Python language and parser objects using tree_sitter_languages
PY_LANGUAGE = tsl.get_language("python")
parser = tsl.get_parser("python")

# Define the sample Python code
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

# Parse the sample code to generate a syntax tree
sample_tree = parser.parse(bytes(sample_code, "utf8"))

# Define the function to visualize the tree
def print_tree_generator(node: Node, depth: int, named_only: bool=False) -> Iterator[str]:
    tree_repr = " " * depth + f"{node.type}"
    if node.type == node.text.decode():
        node_snippet = ""
    else:
        tree_repr = tree_repr.ljust(40, " ")
        node_snippet = textwrap.shorten(node.text.decode(), 80 - depth * 2, placeholder="...")
    if not named_only or node.is_named:
        yield f"{tree_repr} | {node_snippet}"
    for child in node.children:
        yield from print_tree_generator(child, depth + 1, named_only)

def print_tree(node: Node, named_only: bool=False) -> None:
    for ln in print_tree_generator(node, 0, named_only):
        print(ln)

# Constructing a query to find all definitions of classes or functions
query_str = """
(
  (function_definition) @function.def
  (class_definition) @class.def
)
"""

# Creating the query
query = PY_LANGUAGE.query(query_str)

# Capturing the nodes
captures = query.captures(sample_tree.root_node)

# Displaying the captures
captures
```

[child ⬇️](#169e7161-70a8-48c2-b334-f5c9ea134db1)

---

(other branch ⎇)
###### 169e7161-70a8-48c2-b334-f5c9ea134db1
[parent ⬆️](#4753c326-09bf-4430-bfa4-3998a70788d4)
