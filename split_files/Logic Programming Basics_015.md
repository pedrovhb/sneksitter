---
file: /home/pedro/Documents/chatgpt_export/Markdown/Logic Programming Basics.md
heading_stack: <root> -> aae83d65-0c6b-4610-b472-2aec0cdb80b3 -> System -> cd5f65ce-2de1-48c1-aa94-c4163a6f79bd -> System -> aaa22cbb-606f-41d0-b4ae-e591f21bb854 -> User -> e29cce05-dbd4-4728-8c1b-c03f43a7b92e -> Assistant -> Core Components -> How It Works -> Execution Flow: -> aaa2ae6d-a9b8-41f7-87e8-a93920624bd0 -> User -> a699099e-00cf-49be-8eb0-38733c577fa0 -> Assistant
---
# Assistant

```python
# Let's use Python to simulate a simple logic programming environment to illustrate how it works.
# We'll use dictionaries and lists to represent facts, rules, and queries.

# Define some facts
facts = [
    {"predicate": "father", "args": ["John", "Jim"]},
    {"predicate": "father", "args": ["Jim", "Jack"]},
    {"predicate": "mother", "args": ["Marry", "Jim"]},
]

# Define some rules
rules = [
    {"predicate": "parent", "args": ["X", "Y"], "conditions": [{"predicate": "father", "args": ["X", "Y"]}]},
    {"predicate": "parent", "args": ["X", "Y"], "conditions": [{"predicate": "mother", "args": ["X", "Y"]}]},
    {"predicate": "ancestor", "args": ["X", "Y"], "conditions": [{"predicate": "parent", "args": ["X", "Y"]}]},
    {"predicate": "ancestor", "args": ["X", "Y"], "conditions": [{"predicate": "parent", "args": ["X", "Z"]}, {"predicate": "ancestor", "args": ["Z", "Y"]}]}
]

# Function to unify two terms
def unify(term1, term2, subst):
    if subst is None:
        return None
    elif term1 == term2:
        return subst
    elif isinstance(term1, str) and term1.isupper():
        return unify_var(term1, term2, subst)
    elif isinstance(term2, str) and term2.isupper():
        return unify_var(term2, term1, subst)
    elif isinstance(term1, list) and isinstance(term2, list):
        return unify(term1[1:], term2[1:], unify(term1[0], term2[0], subst))
    return None

# Function to unify variable
def unify_var(var, x, subst):
    if var in subst:
        return unify(subst[var], x, subst)
    elif x in subst:
        return unify(var, subst[x], subst)
    else:
        subst[var] = x
        return subst

# Function to query
def query(goal, facts, rules, subst={}):
    for fact in facts:
        if fact['predicate'] == goal['predicate']:
            new_subst = unify(fact['args'], goal['args'], subst.copy())
            if new_subst is not None:
                yield new_subst

    for rule in rules:
        if rule['predicate'] == goal['predicate']:
            new_subst = unify(rule['args'], goal['args'], subst.copy())
            if new_subst is not None:
                for subgoals in query_all(rule['conditions'], facts, rules, new_subst):
                    yield subgoals

# Function to query all conditions
def query_all(conditions, facts, rules, subst):
    if not conditions:
        yield subst
    else:
        first, *rest = conditions
        for new_subst in query(first, facts, rules, subst):
            yield from query_all(rest, facts, rules, new_subst)

# Example queries
list(query_all([{"predicate": "ancestor", "args": ["John", "Y"]}], facts, rules, {}))
```

[child ⬇️](#ac90bca6-5a7a-4d60-9a92-0a011029e761)

---

(main branch ⎇)
###### ac90bca6-5a7a-4d60-9a92-0a011029e761
[parent ⬆️](#a699099e-00cf-49be-8eb0-38733c577fa0)
