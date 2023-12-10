# Assistant

```python
# Consolidating the code and task description into a single Python script for easier future exploration.

task_description = """
# Task Description
The goal is to create a Python program that utilizes Tree-sitter to parse Python source code and extract useful information about functions and classes. Specifically, the program should identify:
- Function definitions along with their names and parameters.
- Class definitions, their names, and methods.
- Decorators for both functions and classes, capturing arguments if any.

# Challenges
- The Tree-sitter query API's "captures" do not seem to accurately capture the nodes tied to function names, parameters, and decorators.

# Future Steps
1. Refine the Tree-sitter query to accurately capture function names, parameters, and decorators.
2. Use the captures to populate Python dataclasses representing the function information.
3. Extend the functionality to capture class information.
"""

# Save the task description and existing code into a Python script
consolidated_code = """
# Import required libraries
from tree_sitter import Language, Parser, Node
from dataclasses import dataclass, field
from typing import List, Optional

# Dataclass definitions
@dataclass
class FunctionInfo:
    name: str
    parameters: List[str]
    decorators: List['DecoratorInfo'] = field(default_factory=list)

@dataclass
class DecoratorInfo:
    name: str
    args: Optional[str] = None

# Initialize Tree-sitter parser and language
LANGUAGE = Language('build/my-languages.so', 'python')
PARSER = Parser()
PARSER.set_language(LANGUAGE)

# Sample Python code to be parsed
source_code = b\"\"\"
@decorator1
@decorator2(arg1, arg2)
def function1(param1, param2):
    pass

@decorator3
def function2(param3):
    pass

def function3():
    pass
\"\"\"

# Parse the source code
tree = PARSER.parse(source_code)

# Function to print the tree structure for debugging
def print_tree(node, indent=0):
    print(' ' * indent + node.type)
    for child in node.children:
        print_tree(child, indent + 2)

# Debug print
print_tree(tree.root_node)

# Tree-sitter query to capture function information and decorators
query = LANGUAGE.query(
    \\"""
    (function_definition
        name: (identifier) @function.name
        (parameters
            (identifier) @parameter))

    (decorator
        (dotted_name (identifier) @decorator))
    \\"""
)

# Execute the query
captures = query.captures(tree.root_node)

# Populate dataclasses with the captured information
parsed_functions = []
current_function = None
current_decorator = None
for node, capture in captures:
    if capture == 'function.name':
        if current_function:
            parsed_functions
```

---
