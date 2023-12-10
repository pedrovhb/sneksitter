### Combining Keyword-Only and Positional-Only Arguments

You can combine keyword-only and positional-only arguments in a function definition. The positional-only arguments should come first, followed by positional-or-keyword arguments, the single asterisk, and then keyword-only arguments.

**Example:**

```python
def combined_function(a, b, /, c, *, d, e):
    print(a, b, c, d, e)

combined_function(1, 2, 3, d=4, e=5)  # This is fine.
# combined_function(1, 2, c=3, d=4, e=5)  # This will raise an error for 'c'.
# combined_function(1, 2, 3, 4, 5)  # This will raise an error for 'd' and 'e'.
```

In the `combined_function`, `a` and `b` are positional-only arguments, `c` is a positional-or-keyword argument, and `d` and `e` are keyword-only arguments.

---
