# Assistant

```python
# Revised query to include decorators and their arguments if any.
# The revised query includes a nested pattern for decorator arguments to capture them separately.
incremental_query_with_decorator_args = py_language.query("""
    (function_definition
        name: (identifier) @function_name
        parameters: (parameters) @function_parameters
        (decorator 
            (identifier) @function_decorator
            (argument_list (expression (identifier) @decorator_arg_identifier))*
        )?
    )
""")

# Test capturing the results to see if this part works
incremental_captures_with_decorator_args = incremental_query_with_decorator_args.captures(sample_tree.root_node)

# Parse the captures into dataclasses
function_infos_with_decorators = []
current_function = None

for node, capture in incremental_captures_with_decorator_args:
    if capture == 'function_name':
        if current_function:
            function_infos_with_decorators.append(current_function)
        current_function = FunctionInfo(name=extract_text(node), parameters='', decorators=[])
    elif capture == 'function_parameters':
        if current_function:
            current_function.parameters = extract_text(node)
    elif capture == 'function_decorator':
        if current_function:
            current_function.decorators.append(extract_text(node))
    elif capture == 'decorator_arg_identifier':
        if current_function:
            current_function.decorators[-1] += f"({extract_text(node)})"  # Append arguments to the last decorator

# Append the last function if any
if current_function:
    function_infos_with_decorators.append(current_function)

function_infos_with_decorators
```

[child ⬇️](#d1a09700-9604-4825-af2f-5f6faa6d8a50)

---

(main branch ⎇)
###### d1a09700-9604-4825-af2f-5f6faa6d8a50
[parent ⬆️](#abe0b9ca-413f-4cef-87b8-81b58fc120e7)
