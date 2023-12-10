# Assistant

```python
# Re-importing the necessary module and initializing the parser and language objects
import tree_sitter_languages

# Getting the Python language and parser
py_language = tree_sitter_languages.get_language("python")
parser = tree_sitter_languages.get_parser("python")

# Parsing the sample code
sample_tree = parser.parse(bytes(sample_code, "utf8"))

# Constructing the query to find all definitions of classes or functions
query_str = """
(
  (function_definition) @function.def
  (class_definition) @class.def
)
"""

# Creating the query
query = py_language.query(query_str)

# Capturing the nodes
captures = query.captures(sample_tree.root_node)

# Displaying the captures
captures
```

[child ⬇️](#9d70c322-b251-4c2a-ad60-c8455265c8c8)

---

(other branch ⎇)
###### 9d70c322-b251-4c2a-ad60-c8455265c8c8
[parent ⬆️](#f3c079c2-4e8e-4cd8-80b3-2432cb15bd60)
