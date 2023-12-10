---
file: /home/pedro/Documents/chatgpt_export/Markdown/LibCST Helper Demonstration.md
heading_stack: <root> -> 18c0f1ba-374d-4172-b284-62c0ac0825f8 -> System -> 28b397c4-d269-4da8-98b4-b7dd276704c0 -> System -> aaa2665f-1e84-4cfd-921d-9a9e022a20dd -> User -> 64222186-7076-4ab1-ac82-a592c46aaf7d -> Assistant -> 0722e61c-10d6-4ddc-8d65-2687e32de790 -> Tool -> eaadfc85-96ad-46b5-890b-9577e8be73ea -> Assistant -> ab2d4700-7b84-4859-b220-f4e5454f730c -> Assistant
---
# Assistant

```python
# Importing the required functions and classes from libcst
from libcst import Module, Name, SimpleString, PartialParserConfig
from libcst.helpers import (
    parse_template_module,
    parse_template_expression,
    parse_template_statement,
    insert_header_comments,
    get_full_name_for_node,
    get_full_name_for_node_or_raise,
    ensure_type,
)

# 1. Construction Helpers
# 1.1 parse_template_module
module = parse_template_module("from {mod} import Foo\n", mod=Name("bar"))
print(f"parse_template_module: {module}")

# 1.2 parse_template_expression
expression = parse_template_expression("x + {foo}", foo=Name("y"))
print(f"parse_template_expression: {expression}")

# 1.3 parse_template_statement
statement = parse_template_statement("assert x > 0, {msg}", msg=SimpleString('"Uh oh!"'))
print(f"parse_template_statement: {statement}")
```

[child ⬇️](#977264ba-ab27-46ce-828a-8f286e18f2f2)

---

(main branch ⎇)
###### 977264ba-ab27-46ce-828a-8f286e18f2f2
[parent ⬆️](#ab2d4700-7b84-4859-b220-f4e5454f730c)
