---
file: /home/pedro/Documents/chatgpt_export/Markdown/Keyword vs Positional Args.md
heading_stack: <root> -> 89d06fea-71c4-46b3-891c-ccd9208d9816 -> System -> 38373356-0b58-450b-8009-591826694a8e -> System -> aaa240dd-d2a9-4183-b5bb-a38a9b604834 -> User -> 4cc6abc0-6597-49e1-a391-bdb6919be3ec -> Assistant -> Keyword-Only Arguments
---
### Keyword-Only Arguments

Keyword-only arguments in Python are arguments that can only be provided by explicitly naming them in the function call. You cannot provide values for keyword-only arguments using positional syntax. Keyword-only arguments are defined in the function signature after a single asterisk (`*`).

**Example:**

```python
def function_with_keyword_only(a, b, *, c, d):
    print(a, b, c, d)

function_with_keyword_only(1, 2, c=3, d=4)  # This is fine.
# function_with_keyword_only(1, 2, 3, 4)  # This will raise an error.
```

