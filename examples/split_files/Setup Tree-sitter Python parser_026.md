# Assistant

```python
# Initialize the query using the parser's language
query = parser.language.query("""
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

[child ⬇️](#da744ba2-ecd2-4dc0-8655-fa8aaee2bf9b)

---

(main branch ⎇)
###### da744ba2-ecd2-4dc0-8655-fa8aaee2bf9b
[parent ⬆️](#99984851-9314-483f-a2a3-126c895dec19)
