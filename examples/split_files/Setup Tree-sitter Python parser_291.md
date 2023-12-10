# Assistant

```python
# Recreating the language and parser objects
py_language = tree_sitter_languages.get_language("python")
parser = tree_sitter_languages.get_parser("python")

# Parsing the sample code again
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

captures
```

[child ⬇️](#57f17960-e10e-40ad-9ddf-034f410a7662)

---

(other branch ⎇)
###### 57f17960-e10e-40ad-9ddf-034f410a7662
[parent ⬆️](#1498a97f-f5ce-423f-a134-4f0eb4a80e87)
