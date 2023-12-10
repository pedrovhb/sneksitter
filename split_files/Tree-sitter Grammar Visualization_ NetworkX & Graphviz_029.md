---
file: /home/pedro/Documents/chatgpt_export/Markdown/Tree-sitter Grammar Visualization_ NetworkX & Graphviz.md
heading_stack: <root> -> b871f517-1eff-4ce0-a351-f14ea50e2084 -> System -> 10bdd2ac-112a-465d-8a80-9a7e6b87ee8a -> System -> aaa26ed0-25be-4ce1-881e-13f438a81018 -> User -> 16f82114-8497-4426-bb51-62a94559597a -> Assistant -> NetworkX -> Graphviz -> Combining NetworkX and Graphviz for Tree-sitter Grammar Visualization -> The Challenge -> The Approach -> Creative Ideas -> Technical Implementation -> Potential Pitfalls -> Conclusion -> aaa26fc9-1f37-46e5-9259-458a8d55dd15 -> User -> 9c564aec-e677-44c1-a480-a6c57d293462 -> Assistant -> a3eb6e27-f341-4b7a-a3d2-34f4cc84ec17 -> Assistant -> c52b2616-0df0-48a9-9a0a-0953bfbd2965 -> Tool -> ae11aab9-6f35-454c-94b2-c2c53890111e -> Assistant -> ca2f2a60-b9a3-4f93-9754-5ebe5ba70517 -> Assistant
---
# Assistant

```python
# Function to recursively find unique types in the grammar rules
def find_unique_types(obj, unique_types_set):
    if isinstance(obj, dict):
        if 'type' in obj:
            unique_types_set.add(obj['type'])
        for key in obj:
            find_unique_types(obj[key], unique_types_set)
    elif isinstance(obj, list):
        for item in obj:
            find_unique_types(item, unique_types_set)

# Initialize a set to store unique types
unique_types = set()

# Search for unique types in the grammar data
find_unique_types(grammar_data, unique_types)

# Display the identified unique types
unique_types
```

[child ⬇️](#8fba5a35-e974-4d97-ae80-844eb75c9ac4)

---

(main branch ⎇)
###### 8fba5a35-e974-4d97-ae80-844eb75c9ac4
[parent ⬆️](#ca2f2a60-b9a3-4f93-9754-5ebe5ba70517)
