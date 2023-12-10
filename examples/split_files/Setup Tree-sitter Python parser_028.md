# Tool

```python
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[4], line 1
----> 1 query = parser.language.query("""
      2 (function_definition
      3   name: (identifier) @function.def)
      4 
      5 (call
      6   function: (identifier) @function.call)
      7 """)
      9 # Execute the query to get the captures
     10 captures = query.captures(tree.root_node)

AttributeError: 'tree_sitter.Parser' object has no attribute 'language'

```

[child ⬇️](#15f61e74-54fd-47d9-8008-f0d889bf12b7)

---

(main branch ⎇)
###### 15f61e74-54fd-47d9-8008-f0d889bf12b7
[parent ⬆️](#da744ba2-ecd2-4dc0-8655-fa8aaee2bf9b)
