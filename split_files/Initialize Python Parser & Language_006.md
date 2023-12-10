---
file: /home/pedro/Documents/chatgpt_export/Markdown/Initialize Python Parser & Language.md
heading_stack: <root> -> 7deaf15e-dcb4-475b-bbae-9fde5f9b50d7 -> System -> 5a6cae08-3bad-4a1b-92fc-266c59c03560 -> System -> aaa2ddfa-521c-405d-b9e3-227ffc2bcaac -> User
---
# User

```
import tree_sitter_languages

parser = tree_sitter_languages.get_parser("python")
...  # use as normal, e.g. tree = parser.parse(...), cursor = tree.walk(), cursor.go to first child, parent, next sibling, etc)
language = tree_sitter_languages.get_lnguage("python")
sample_code = b'''<...>'''
query = language.query((function_definition name: (identifier) @function.name)").capt...
```

---

Please create a notebook, %pip install -q tree_sitter_languages networkx, and initialize a Python parser and language as per the example above.

[child ⬇️](#6d8915d9-494c-4acc-8597-98c9519f6c8f)

---

(main branch ⎇)
###### 6d8915d9-494c-4acc-8597-98c9519f6c8f
[parent ⬆️](#aaa2ddfa-521c-405d-b9e3-227ffc2bcaac)
