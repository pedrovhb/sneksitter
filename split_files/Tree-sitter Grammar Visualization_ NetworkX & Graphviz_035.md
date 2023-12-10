---
file: /home/pedro/Documents/chatgpt_export/Markdown/Tree-sitter Grammar Visualization_ NetworkX & Graphviz.md
heading_stack: <root> -> b871f517-1eff-4ce0-a351-f14ea50e2084 -> System -> 10bdd2ac-112a-465d-8a80-9a7e6b87ee8a -> System -> aaa26ed0-25be-4ce1-881e-13f438a81018 -> User -> 16f82114-8497-4426-bb51-62a94559597a -> Assistant -> NetworkX -> Graphviz -> Combining NetworkX and Graphviz for Tree-sitter Grammar Visualization -> The Challenge -> The Approach -> Creative Ideas -> Technical Implementation -> Potential Pitfalls -> Conclusion -> aaa26fc9-1f37-46e5-9259-458a8d55dd15 -> User -> 9c564aec-e677-44c1-a480-a6c57d293462 -> Assistant -> a3eb6e27-f341-4b7a-a3d2-34f4cc84ec17 -> Assistant -> c52b2616-0df0-48a9-9a0a-0953bfbd2965 -> Tool -> ae11aab9-6f35-454c-94b2-c2c53890111e -> Assistant -> ca2f2a60-b9a3-4f93-9754-5ebe5ba70517 -> Assistant -> 8fba5a35-e974-4d97-ae80-844eb75c9ac4 -> Tool -> 6d10afb6-8dde-460d-9bad-821eb823350a -> Assistant -> cfa78ec0-6094-4895-a72e-3a426f4b264f -> Assistant
---
# Assistant

```python
from collections import defaultdict

# Function to recursively map rule relationships
def map_rule_relationships(obj, rule_name, rule_relations):
    if isinstance(obj, dict):
        if 'name' in obj and 'content' in obj:
            sub_rule = obj['content'].get('name', obj['content'].get('value', None))
            if sub_rule:
                rule_relations[rule_name].add(sub_rule)
        for key in obj:
            map_rule_relationships(obj[key], rule_name, rule_relations)
    elif isinstance(obj, list):
        for item in obj:
            map_rule_relationships(item, rule_name, rule_relations)

# Initialize a defaultdict to store rule relationships
rule_relations = defaultdict(set)

# Map relationships for each rule in the grammar data
for rule in grammar_data.get('rules', {}):
    map_rule_relationships(grammar_data['rules'][rule], rule, rule_relations)

# Display a snippet of the rule relationships mapping
dict(list(rule_relations.items())[:10])
```

[child ⬇️](#873bf5b9-8358-4f4b-828c-bc6c8c8b0cb2)

---

(main branch ⎇)
###### 873bf5b9-8358-4f4b-828c-bc6c8c8b0cb2
[parent ⬆️](#cfa78ec0-6094-4895-a72e-3a426f4b264f)
