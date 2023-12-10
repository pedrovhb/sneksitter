# Assistant

```python
# Importing the necessary module and initializing the parser and language objects
import tree_sitter_languages

# Sample code with different types of function definitions, methods, closures, with/without decorators
sample_code = b"""
def simple_function():
    pass

def function_with_args(x, y):
    return x + y

@decorator
def decorated_function():
    pass

class MyClass:
    def method(self):
        pass

def outer_function():
    def inner_function():
        pass
    return inner_function
"""

# Getting the Python language and parser
py_language = tree_sitter_languages.get_language("python")
parser = tree_sitter_languages.get_parser("python")

# Parsing the sample code
sample_tree = parser.parse(bytes(sample_code, "utf8"))

# Constructing the query to find all definitions of classes or functions
query_str = """
(
  (function_definition) @function.def
)
"""

# Creating the query
query = py_language.query(query_str)

# Capturing the nodes
captures = query.captures(sample_tree.root_node)

# Displaying the captures
captures
```

[child ⬇️](#03332a3e-f746-43bf-a6b9-34359dac7e4b)

---

(main branch ⎇)
###### 03332a3e-f746-43bf-a6b9-34359dac7e4b
[parent ⬆️](#5248916b-dcde-4011-8317-2290e1d80621)
