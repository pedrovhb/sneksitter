---
file: /home/pedro/Documents/chatgpt_export/Markdown/Setup Tree-sitter Python parser.md
heading_stack: <root> -> 48404b29-4887-462e-acd5-c1ecf0317fbf -> System -> 116c69b9-0217-4c43-bedc-42dcbf0f826d -> System -> aaa2b2b9-a972-49a4-8072-387253454bc2 -> User -> 65ebe623-cb59-4071-a891-b0ecac4a7299 -> Assistant -> 3b9d8f44-31ea-4a18-a85c-2144c2c1c659 -> Tool -> 74a3cf29-c1fc-4242-817b-f8e9f83315ef -> Assistant -> 8801ae9a-ded1-475a-a3e9-bd817697ad99 -> Tool -> 133fb8b4-7853-4484-b203-3efbc6ed24b1 -> Assistant -> aaa293e9-a16a-4dcb-bf1e-e1a857731e97 -> User -> 953ccdca-be2f-4765-bdf5-13151dff1986 -> Assistant -> 9f67d0a5-d0f4-44e9-8fa7-40963c60e88f -> Tool -> 4dc004ce-1401-4ffc-871d-bd967d2f63a9 -> Assistant -> 99984851-9314-483f-a2a3-126c895dec19 -> Assistant -> da744ba2-ecd2-4dc0-8655-fa8aaee2bf9b -> Tool -> 15f61e74-54fd-47d9-8008-f0d889bf12b7 -> Assistant -> aaa2d60b-338e-4152-9e50-83b6a20eff30 -> User -> de6b35bd-5bff-4de0-95b8-221d8d435c40 -> Assistant
---
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