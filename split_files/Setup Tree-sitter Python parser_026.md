---
file: /home/pedro/Documents/chatgpt_export/Markdown/Setup Tree-sitter Python parser.md
heading_stack: <root> -> 48404b29-4887-462e-acd5-c1ecf0317fbf -> System -> 116c69b9-0217-4c43-bedc-42dcbf0f826d -> System -> aaa2b2b9-a972-49a4-8072-387253454bc2 -> User -> 65ebe623-cb59-4071-a891-b0ecac4a7299 -> Assistant -> 3b9d8f44-31ea-4a18-a85c-2144c2c1c659 -> Tool -> 74a3cf29-c1fc-4242-817b-f8e9f83315ef -> Assistant -> 8801ae9a-ded1-475a-a3e9-bd817697ad99 -> Tool -> 133fb8b4-7853-4484-b203-3efbc6ed24b1 -> Assistant -> aaa293e9-a16a-4dcb-bf1e-e1a857731e97 -> User -> 953ccdca-be2f-4765-bdf5-13151dff1986 -> Assistant -> 9f67d0a5-d0f4-44e9-8fa7-40963c60e88f -> Tool -> 4dc004ce-1401-4ffc-871d-bd967d2f63a9 -> Assistant -> 99984851-9314-483f-a2a3-126c895dec19 -> Assistant
---
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
