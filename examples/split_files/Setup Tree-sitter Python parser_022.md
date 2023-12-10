# Tool

```python
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[3], line 12
      9 tree = parser.parse(bytes(source_code, "utf8"))
     11 # Create a query for pattern matching
---> 12 query = tree_sitter_languages.PY_LANGUAGE.query("""
     13 (function_definition
     14   name: (identifier) @function.def)
     15 
     16 (call
     17   function: (identifier) @function.call)
     18 """)
     20 # Execute the query and get the captures
     21 captures = query.captures(tree.root_node)

AttributeError: module 'tree_sitter_languages' has no attribute 'PY_LANGUAGE'

```

[child ⬇️](#4dc004ce-1401-4ffc-871d-bd967d2f63a9)

---

(main branch ⎇)
###### 4dc004ce-1401-4ffc-871d-bd967d2f63a9
[parent ⬆️](#9f67d0a5-d0f4-44e9-8fa7-40963c60e88f)
