# User

Please set this up and initialize a tree sitter Python language and parser.

Since this is an offline environment, you'll do things a bit different and get a tree sitter parser for any language (e.g. Python, Markdown, Prolog) via the following:

```
import tree_sitter_languages

parser = tree_sitter_languages.get_parser("python")
...  # use as normal, e.g. tree = parser.parse(...), cursor = tree.walk(), cursor.go to first child, parent, next sibling, etc)
```

[child ⬇️](#65ebe623-cb59-4071-a891-b0ecac4a7299)

---

(main branch ⎇)
###### 65ebe623-cb59-4071-a891-b0ecac4a7299
[parent ⬆️](#aaa2b2b9-a972-49a4-8072-387253454bc2)
