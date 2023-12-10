---
file: /home/pedro/Documents/chatgpt_export/Markdown/Keyword vs Positional Args.md
heading_stack: <root> -> 89d06fea-71c4-46b3-891c-ccd9208d9816 -> System -> 38373356-0b58-450b-8009-591826694a8e -> System -> aaa240dd-d2a9-4183-b5bb-a38a9b604834 -> User -> 4cc6abc0-6597-49e1-a391-bdb6919be3ec -> Assistant
---
# Assistant

### Keyword-Only Arguments

Keyword-only arguments in Python are arguments that can only be provided by explicitly naming them in the function call. You cannot provide values for keyword-only arguments using positional syntax. Keyword-only arguments are defined in the function signature after a single asterisk (`*`).

**Example:**

```python
def function_with_keyword_only(a, b, *, c, d):
    print(a, b, c, d)

function_with_keyword_only(1, 2, c=3, d=4)  # This is fine.
# function_with_keyword_only(1, 2, 3, 4)  # This will raise an error.
```

### Positional-Only Arguments

Positional-only arguments are the opposite of keyword-only arguments. They can only be provided by position, not by explicitly naming them in the function call. Positional-only arguments are defined in the function signature before a single forward slash (`/`).

**Example:**

```python
def function_with_positional_only(a, b, /, c, d):
    print(a, b, c, d)

function_with_positional_only(1, 2, 3, 4)  # This is fine.
# function_with_positional_only(1, 2, c=3, d=4)  # This will raise an error for 'c'.
```

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
