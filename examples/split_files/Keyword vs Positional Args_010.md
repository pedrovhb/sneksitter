### Positional-Only Arguments

Positional-only arguments are the opposite of keyword-only arguments. They can only be provided by position, not by explicitly naming them in the function call. Positional-only arguments are defined in the function signature before a single forward slash (`/`).

**Example:**

```python
def function_with_positional_only(a, b, /, c, d):
    print(a, b, c, d)

function_with_positional_only(1, 2, 3, 4)  # This is fine.
# function_with_positional_only(1, 2, c=3, d=4)  # This will raise an error for 'c'.
```

