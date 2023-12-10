# Assistant

```python
# Importing the necessary module and initializing the parser and language objects
import tree_sitter_languages

# Sample code demonstrating different types of function definitions, methods, closures, with/without decorators, etc.
sample_code = b"""
def simple_function():
    pass

def function_with_args(a, b):
    return a + b

@staticmethod
def static_method():
    return "I'm static!"

@classmethod
def class_method(cls):
    return "I'm a class method!"

class SampleClass:
    def class_function(self):
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
sample_tree = parser.parse(sample_code)

# Printing the structure
print(sample_tree.root_node.sexp())

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

[child ⬇️](#79c0cb78-cd7a-49be-a928-4d619fa5b831)

---

(main branch ⎇)
###### 79c0cb78-cd7a-49be-a928-4d619fa5b831
[parent ⬆️](#b3df5168-e046-4ffc-8d28-3933f74f6eb9)
