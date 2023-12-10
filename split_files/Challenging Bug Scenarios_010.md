---
file: /home/pedro/Documents/chatgpt_export/Markdown/Challenging Bug Scenarios.md
heading_stack: <root> -> 16b4f038-f461-4bea-aab3-f16d97102976 -> System -> f030f68c-1381-4970-ab86-0ddb5dbec373 -> System -> aaa2a9a6-bc09-4eb8-ade3-de667199f255 -> User -> 297b2268-6318-4cbd-8782-30c76dd52aa2 -> Assistant -> Scenario 1: Race Condition in Multithreading -> Scenario 2: Memory Leak
---
### Scenario 2: Memory Leak
A function that is supposed to remove an item from a list but instead causes a memory leak due to poor handling of object references.

```python
# Memory leak caused by not properly deleting references
cache = {}
def remove_item(item):
    if item in cache:
        del cache[item]
        # Missing code to properly clean up other references
        # leading to a memory leak

# Usage
cache['item1'] = [1, 2, 3]
remove_item('item1')  # Causes memory leak
```

