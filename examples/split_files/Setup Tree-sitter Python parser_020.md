# Assistant

```python
# Create a Python source code string to be parsed
source_code = """
def my_function():
    pass

my_function()
"""

# Parse the source code using the initialized parser
tree = parser.parse(bytes(source_code, "utf8"))

# Create a query for pattern matching
query = tree_sitter_languages.PY_LANGUAGE.query("""
(function_definition
  name: (identifier) @function.def)

(call
  function: (identifier) @function.call)
""")

# Execute the query and get the captures
captures = query.captures(tree.root_node)

# Check the length of captures and the properties of captured nodes
len_captures = len(captures)
assert len_captures == 2

function_name_node = captures[0][0]
assert captures[0][1] == "function.def"

len_captures, captures[0][0].type, captures[0][1], captures[1][0].type, captures[1][1]
```

[child ⬇️](#9f67d0a5-d0f4-44e9-8fa7-40963c60e88f)

---

(main branch ⎇)
###### 9f67d0a5-d0f4-44e9-8fa7-40963c60e88f
[parent ⬆️](#953ccdca-be2f-4765-bdf5-13151dff1986)
