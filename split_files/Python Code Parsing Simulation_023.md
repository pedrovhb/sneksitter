---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Code Parsing Simulation.md
heading_stack: <root> -> c4eae637-232c-4496-bc70-753ddd81ba96 -> System -> c5df0cbc-e9fb-4d62-aeed-bcacaa85e110 -> System -> aaa2117c-13e4-4cb9-ba7c-ceab891c0d9c -> User -> Importing the necessary module and initializing the parser and language objects -> Getting the Python language and parser -> Parsing the sample code -> Constructing the query to find all definitions of classes or functions -> Creating the query -> Capturing the nodes -> Displaying the captures -> 8e3bd3ee-59e8-4e34-828c-20572fbdd435 -> Assistant -> aaa2be76-f4f3-4cf3-954a-244cca89494f -> User -> 11dd3286-c68d-4052-98e8-b647a7700959 -> Assistant -> aaa23fcd-fff2-4fd9-912d-55d6c15420b1 -> User -> 5248916b-dcde-4011-8317-2290e1d80621 -> Assistant
---
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
