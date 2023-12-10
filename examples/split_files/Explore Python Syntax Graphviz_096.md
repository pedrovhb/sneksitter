# Assistant

```python
import re

def generate_regex_and_example(rule, rules, depth=0, max_depth=5):
    """
    Generate a regular expression and an example string based on a given rule.
    
    Parameters:
    - rule: The current rule to process.
    - rules: Dictionary of all rules.
    - depth: Current depth of recursion.
    - max_depth: Maximum depth to prevent infinite recursion.
    
    Returns:
    - tuple: (regular expression, example string)
    """
    if depth > max_depth:
        return ("", "")

    regex = ""
    example = ""
    
    rule_type = rule.get("type")
    
    if rule_type == "SEQ":
        for member in rule.get("members", []):
            member_regex, member_example = generate_regex_and_example(member, rules, depth + 1, max_depth)
            regex += member_regex
            example += member_example
            
    elif rule_type == "CHOICE":
        # Just take the first choice for the example
        choice = rule.get("members", [{}])[0]
        regex = "(" + "|".join(generate_regex_and_example(member, rules, depth + 1, max_depth)[0] for member in rule.get("members", [])) + ")"
        example = generate_regex_and_example(choice, rules, depth + 1, max_depth)[1]
        
    elif rule_type == "STRING":
        regex = re.escape(rule.get("value", ""))
        example = rule.get("value", "")
        
    elif rule_type == "SYMBOL":
        symbol_name = rule.get("name")
        if symbol_name in rules:
            regex, example = generate_regex_and_example(rules[symbol_name], rules, depth + 1, max_depth)
            
    elif rule_type == "REPEAT":
        content = rule.get("content")
        content_regex, content_example = generate_regex_and_example(content, rules, depth + 1, max_depth)
        regex = f"{content_regex}*"
        example = ""  # Empty string is a valid example for a repeat
    
    return regex, example

# Generate regular expressions and example strings for a subset of SQLite rules
generated_data = {}
for rule_name, rule in list(sqlite_rules.items())[:10]:  # Limiting to first 10 rules for demonstration
    regex, example = generate_regex_and_example(rule, sqlite_rules)
    generated_data[rule_name] = {"regex": regex, "example": example}

generated_data
```

[child ⬇️](#c5ca7c25-cff8-4e1e-b810-1d25a11c0144)

---

(main branch ⎇)
###### c5ca7c25-cff8-4e1e-b810-1d25a11c0144
[parent ⬆️](#c59d6c32-a199-4fb0-8369-fa7be925d4ca)
