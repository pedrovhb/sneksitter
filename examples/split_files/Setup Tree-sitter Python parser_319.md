# Assistant

```python
# Correcting the query syntax and trying again
corrected_query_with_decorators = py_language.query("""
    (function_definition
        name: (identifier) @function_name
        parameters: (parameters) @function_parameters
        (decorator (identifier) @function_decorator (argument_list) @decorator_args?))

    (class_definition
        name: (identifier) @class_name
        (decorator (identifier) @class_decorator (argument_list) @decorator_args?))
""")

# Capturing the results
captures_with_decorators = corrected_query_with_decorators.captures(sample_tree.root_node)

# Processing and displaying the captures
capture_data_with_decorators = []

for node, capture_name in captures_with_decorators:
    node_text = sample_code[node.start_byte:node.end_byte].decode()

    # Class and Function Names
    if capture_name in ['function_name', 'class_name']:
        capture_type = 'Function' if capture_name == 'function_name' else 'Class'
        capture_data_with_decorators.append({'Type': capture_type, 'Name': node_text})

    # Parameters
    elif capture_name == 'function_parameters':
        if capture_data_with_decorators[-1]['Type'] == 'Function':  # Safety check
            capture_data_with_decorators[-1]['Parameters'] = node_text

    # Decorators
    elif capture_name in ['function_decorator', 'class_decorator']:
        capture_type = 'Function' if capture_name == 'function_decorator' else 'Class'
        if 'Decorators' not in capture_data_with_decorators[-1]:
            capture_data_with_decorators[-1]['Decorators'] = []
        capture_data_with_decorators[-1]['Decorators'].append({'Name': node_text})

    # Decorator Arguments
    elif capture_name == 'decorator_args':
        last_decorator = capture_data_with_decorators[-1]['Decorators'][-1]
        last_decorator['Arguments'] = node_text

capture_data_with_decorators
```

[child ⬇️](#50ff0282-d598-4ded-a536-a844db547e69)

---

(main branch ⎇)
###### 50ff0282-d598-4ded-a536-a844db547e69
[parent ⬆️](#759b9eed-ec84-4c9a-ac86-69b0324b68c7)
