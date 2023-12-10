---
file: /home/pedro/Documents/chatgpt_export/Markdown/Setup Tree-sitter Python parser.md
heading_stack: <root> -> 48404b29-4887-462e-acd5-c1ecf0317fbf -> System -> 116c69b9-0217-4c43-bedc-42dcbf0f826d -> System -> aaa2b2b9-a972-49a4-8072-387253454bc2 -> User -> 65ebe623-cb59-4071-a891-b0ecac4a7299 -> Assistant -> 3b9d8f44-31ea-4a18-a85c-2144c2c1c659 -> Tool -> 74a3cf29-c1fc-4242-817b-f8e9f83315ef -> Assistant -> 8801ae9a-ded1-475a-a3e9-bd817697ad99 -> Tool -> 133fb8b4-7853-4484-b203-3efbc6ed24b1 -> Assistant -> aaa293e9-a16a-4dcb-bf1e-e1a857731e97 -> User -> 953ccdca-be2f-4765-bdf5-13151dff1986 -> Assistant -> 9f67d0a5-d0f4-44e9-8fa7-40963c60e88f -> Tool
---
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
