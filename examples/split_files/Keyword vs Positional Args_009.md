### Keyword-Only Arguments

Keyword-only arguments in Python are arguments that can only be provided by explicitly naming them in the function call. You cannot provide values for keyword-only arguments using positional syntax. Keyword-only arguments are defined in the function signature after a single asterisk (`*`).

**Example:**

```python
def function_with_keyword_only(a, b, *, c, d):
    print(a, b, c, d)

function_with_keyword_only(1, 2, c=3, d=4)  # This is fine.
# function_with_keyword_only(1, 2, 3, 4)  # This will raise an error.
```

