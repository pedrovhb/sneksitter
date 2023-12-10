# Assistant

```python
# Building the query to find all definitions of classes or functions, their names, and parameters
query = py_language.query("""
    (function_definition
        name: (identifier) @function_name
        parameters: (parameters) @function_parameters)

    (class_definition
        name: (identifier) @class_name)
""")

# Capturing the results
captures = query.captures(sample_tree.root_node)

# Processing and displaying the captures
capture_data = []

for node, capture_name in captures:
    if capture_name in ['function_name', 'class_name']:
        capture_type = 'Function' if capture_name == 'function_name' else 'Class'
        name = sample_code[node.start_byte:node.end_byte]
        capture_data.append({'Type': capture_type, 'Name': name})

    elif capture_name == 'function_parameters':
        params = sample_code[node.start_byte:node.end_byte]
        if capture_data[-1]['Type'] == 'Function':  # Safety check
            capture_data[-1]['Parameters'] = params

capture_data
```

[child ⬇️](#b773bbef-d919-438e-be35-b26425056695)

---

(main branch ⎇)
###### b773bbef-d919-438e-be35-b26425056695
[parent ⬆️](#d54b23d7-a3db-46e8-812b-f54163b123df)
