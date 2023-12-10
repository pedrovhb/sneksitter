# Assistant

```python
# Importing tree_sitter_languages and initializing a Python language and parser objects
from tree_sitter_languages import get_parser, get_language

# Initialize the Python parser and language objects
parser = get_parser("python")
language = get_language("python")

# Using dir() to see what's available in the public API of each object
parser_methods = dir(parser)
language_methods = dir(language)

# Example code to parse
example_code = """
def hello_world():
    print("Hello, world!")

hello_world()
"""

# Parse the example code to generate a tree and root node
tree = parser.parse(bytes(example_code, "utf8"))
root_node = tree.root_node

# Using dir() to see what's available in the public API of tree and node objects
tree_methods = dir(tree)
node_methods = dir(root_node)

# Function to visualize nodes as an indented tree
def visualize_tree(node, indent=0, text=None):
    """Recursively print the tree structure."""
    snippet = text[node.start_byte:node.end_byte][:10].decode("utf-8").replace("\n", "\\n")
    print("  " * indent + f"{node.type}: {snippet}")
    for child in node.children:
        visualize_tree(child, indent + 1, text)

# Visualizing the tree structure of the parsed example code
visualize_tree(root_node, text=bytes(example_code, "utf8"))

parser_methods, language_methods, tree_methods, node_methods
```

[child ⬇️](#9076544b-350f-4cf1-bfe4-b112e1c4c9e1)

---

(main branch ⎇)
###### 9076544b-350f-4cf1-bfe4-b112e1c4c9e1
[parent ⬆️](#c9e58270-2bdf-4b13-8995-7142dbb5ec9d)
