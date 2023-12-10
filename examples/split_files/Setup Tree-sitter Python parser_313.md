# Assistant

```python
# Extending the query to capture decorators and their arguments for classes and functions
query_with_decorators = py_language.query("""
    (function_definition
        name: (identifier) @function_name
        parameters: (parameters) @function_parameters
        (decorator (identifier) @function_decorator (argument_list)? @decorator_args?))

    (class_definition
        name: (identifier) @class_name
        (decorator (identifier) @class_decorator (argument_list)? @decorator_args?))
""")

# Capturing the results
captures_with_decorators = query_with_decorators.captures(sample_tree.root_node)

# Processing and displaying the captures
capture_data_with_decorators = []

for node, capture_name in captures_with_decorators:
    node_text = sample_code[node.start_byte:node.end_byte]

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

[child ⬇️](#372a7e4f-a314-4df5-989e-ff73484c4792)

---

(main branch ⎇)
###### 372a7e4f-a314-4df5-989e-ff73484c4792
[parent ⬆️](#e4c5477e-6aa2-40e0-bd49-88ec2a16a033)
