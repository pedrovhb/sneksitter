# Assistant

```python
# Installing required packages (for demonstration purposes, as the packages can't actually be installed in this environment)
# !pip install problog
# !pip install tree-sitter

# Importing required modules (pseudo-imports for demonstration)
# from problog.program import SimpleProgram
# from problog import get_evaluatable
# from tree_sitter import Language, Parser

# For demonstration, let's assume we have a simplified AST as a Python dict
ast_dict = {
    "type": "program",
    "children": [
        {
            "type": "function_declaration",
            "name": "add",
            "parameters": ["a", "b"]
        },
        {
            "type": "function_declaration",
            "name": "subtract",
            "parameters": ["a", "b"]
        }
    ]
}

# Function to convert AST dict to Problog facts
def ast_to_problog_facts(ast):
    facts = []
    for child in ast['children']:
        if child['type'] == 'function_declaration':
            facts.append(f'function({child["name"]}, {child["parameters"]}).')
    return facts

# Convert AST to Problog facts
problog_facts = ast_to_problog_facts(ast_dict)

# Add facts to Problog program
# p = SimpleProgram()
# for fact in problog_facts:
#     p += fact

# Run query (pseudo code)
# query_result = get_evaluatable().create_from(p).evaluate()

# Assuming query_result would be something like:
# query_result = {'function(add, [a, b])': 1.0, 'function(subtract, [a, b])': 1.0}

# Display Problog facts and hypothetical query result
problog_facts  #, query_result
```

[child ⬇️](#9978cbbc-5a73-4355-b7a2-bfe5ad157a2a)

---

(main branch ⎇)
###### 9978cbbc-5a73-4355-b7a2-bfe5ad157a2a
[parent ⬆️](#6cdbec38-13cd-4dd5-8040-93187532675b)
