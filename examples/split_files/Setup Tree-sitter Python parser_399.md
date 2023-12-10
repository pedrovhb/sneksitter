# Assistant

```python
from dataclasses import dataclass, field
from typing import List, Optional, Union

@dataclass
class Decorator:
    name: str
    arguments: Optional[List[Union[str, int]]] = field(default_factory=list)

@dataclass
class FunctionDefinition:
    name: str
    decorators: List[Decorator] = field(default_factory=list)
    parameters: List[str] = field(default_factory=list)

def parse_decorators(decorated_def_node):
    decorators = []
    for child in decorated_def_node.children:
        if child.type == 'decorator':
            decorator_name = None
            decorator_args = []
            for decorator_child in child.children:
                if decorator_child.type == 'identifier':
                    decorator_name = decorator_child.text.decode()
                elif decorator_child.type == 'argument_list':
                    for arg in decorator_child.children:
                        if arg.type == 'string':
                            decorator_args.append(arg.text.decode().strip('"'))
                        elif arg.type == 'integer':
                            decorator_args.append(int(arg.text.decode()))
            if decorator_name:
                decorators.append(Decorator(name=decorator_name, arguments=decorator_args))
    return decorators

def parse_function_definition(node):
    function_name = None
    parameters = []
    for child in node.children:
        if child.type == 'identifier':
            function_name = child.text.decode()
        elif child.type == 'parameters':
            for param in child.children:
                if param.type == 'identifier':
                    parameters.append(param.text.decode())
    return FunctionDefinition(name=function_name, parameters=parameters)

def extract_function_info(tree_root):
    functions = []
    query = py_language.query("""
    (decorated_definition
        (decorator (identifier) @decorator.name (argument_list)? @decorator.args)
        (function_definition
            name: (identifier) @function.name
            (parameters (identifier) @param.name)
        )
    )
    """)
    captures = query.captures(tree_root)
    decorated_def_node = None
    for node, capture_name in captures:
        if capture_name == 'decorator.name' or capture_name == 'decorator.args':
            continue  # Handled together in parse_decorators
        if capture_name == 'function.name':
            if decorated_def_node:
                decorators = parse_decorators(decorated_def_node)
            else:
                decorators = []
            function_info = parse_function_definition(node.parent)
            function_info.decorators = decorators
            functions.append(function_info)
            decorated_def_node = None
        elif node.parent.type == 'decorated_definition':
            decorated_def_node = node.parent
    return functions

# Parse the function information from the previously parsed tree of the sample code
extracted_functions = extract_function_info(decorator_sample_tree.root_node)
extracted_functions
```

[child ⬇️](#63cffa66-b22d-45bc-8474-a83b28a86830)

---

(main branch ⎇)
###### 63cffa66-b22d-45bc-8474-a83b28a86830
[parent ⬆️](#52076f6a-1e4c-477e-8092-d88ffa4b8865)
