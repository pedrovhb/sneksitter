# Assistant

```python
# Import get_language from tree_sitter_languages
from tree_sitter_languages import get_language

# Get the language for Python
py_language = get_language("python")

# Create the query using the acquired language
query = py_language.query("""
(function_definition
  name: (identifier) @function.def)

(call
  function: (identifier) @function.call)
""")

# Execute the query to get the captures
captures = query.captures(tree.root_node)

# Validate the captures
len_captures = len(captures)
assert len_captures == 2

function_name_node = captures[0][0]
assert captures[0][1] == "function.def"

len_captures, captures[0][0].type, captures[0][1], captures[1][0].type, captures[1][1]
```

[child ⬇️](#4cdff389-2396-4ab1-be1d-8b1b82078b94)

---

(main branch ⎇)
###### 4cdff389-2396-4ab1-be1d-8b1b82078b94
[parent ⬆️](#de6b35bd-5bff-4de0-95b8-221d8d435c40)
