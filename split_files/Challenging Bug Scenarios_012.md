---
file: /home/pedro/Documents/chatgpt_export/Markdown/Challenging Bug Scenarios.md
heading_stack: <root> -> 16b4f038-f461-4bea-aab3-f16d97102976 -> System -> f030f68c-1381-4970-ab86-0ddb5dbec373 -> System -> aaa2a9a6-bc09-4eb8-ade3-de667199f255 -> User -> 297b2268-6318-4cbd-8782-30c76dd52aa2 -> Assistant -> Scenario 1: Race Condition in Multithreading -> Scenario 2: Memory Leak -> Scenario 3: Heisenbug (Behavior changes under observation) -> Scenario 4: Non-Deterministic Behavior
---
### Scenario 4: Non-Deterministic Behavior
A program using a dictionary where the order of keys affects the output, but the dictionary is not ordered.

```python
# Non-deterministic behavior due to unordered keys in Python < 3.7
def calculate_sum(data):
    total = 0
    for key in data.keys():
        total += data[key]
    return total

data = {'a': 1, 'b': 2, 'c': 3}
print(calculate_sum(data))
# Output varies between runs in Python < 3.7
```

These are simplified examples, but in a real-world application, such issues can be much more elusive and challenging to identify and fix.

[child ⬇️](#aaa2da28-e469-4aab-accc-b52d7aa18433)

---

(main branch ⎇)
###### aaa2da28-e469-4aab-accc-b52d7aa18433
[parent ⬆️](#297b2268-6318-4cbd-8782-30c76dd52aa2)
