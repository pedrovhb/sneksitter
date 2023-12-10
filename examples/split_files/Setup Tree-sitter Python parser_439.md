# Assistant

```python
# I forgot to use the source_code variable. Let's define it and rerun the parsing logic.
source_code = b"""
@decorator1
@decorator2(arg1, arg2)
def function1(param1, param2):
    pass

@decorator3
def function2(param3):
    pass

def function3():
    pass
"""

# Re-run the parsing logic
parsed_functions = []

# Helper function to extract text from a node
extract_text = lambda node: source_code[node.start_byte:node.end_byte].decode()

# Iterate through the captures and populate the dataclasses
current_function = None
current_decorator = None

for node, capture in quantified_captures:
    if capture == 'function.name':
        if current_function:
            parsed_functions.append(current_function)
        current_function = FunctionInfo(name=extract_text(node), parameters=[])
    elif capture == 'parameter':
        if current_function:
            current_function.parameters.append(extract_text(node))
    elif capture == 'decorator':
        current_decorator = DecoratorInfo(name=extract_text(node))
        if current_function:
            current_function.decorators.append(current_decorator)

# Append the last function if any
if current_function:
    parsed_functions.append(current_function)

parsed_functions
```

[child ⬇️](#ecd3b651-24db-4a94-a3ab-f6c4da730f18)

---

(main branch ⎇)
###### ecd3b651-24db-4a94-a3ab-f6c4da730f18
[parent ⬆️](#5ac754dd-a6c9-4af0-a472-5dc98a71d8d2)
