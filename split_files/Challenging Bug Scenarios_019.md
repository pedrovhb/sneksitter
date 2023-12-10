---
file: /home/pedro/Documents/chatgpt_export/Markdown/Challenging Bug Scenarios.md
heading_stack: <root> -> 16b4f038-f461-4bea-aab3-f16d97102976 -> System -> f030f68c-1381-4970-ab86-0ddb5dbec373 -> System -> aaa2a9a6-bc09-4eb8-ade3-de667199f255 -> User -> 297b2268-6318-4cbd-8782-30c76dd52aa2 -> Assistant -> Scenario 1: Race Condition in Multithreading -> Scenario 2: Memory Leak -> Scenario 3: Heisenbug (Behavior changes under observation) -> Scenario 4: Non-Deterministic Behavior -> aaa2da28-e469-4aab-accc-b52d7aa18433 -> User -> 24b2a49b-4ec7-4808-8cb2-7a985f77921f -> Assistant -> Scenario 1: Nested Async Calls Hiding a Deadlock -> Scenario 2: Data Corruption due to Inconsistent Global State -> Scenario 3: Intermittent Failure due to Uninitialized Variable
---
### Scenario 3: Intermittent Failure due to Uninitialized Variable

This example calculates the total price for a list of products. A bug occurs due to an uninitialized variable, but the program masks it by catching the exception and continuing the loop.

```python
products = [
    {'name': 'apple', 'price': 1.0},
    {'name': 'banana', 'price': 0.5},
    {'name': 'cherry', 'price': 2.0},
]

def calculate_total(products):
    try:
        for product in products:
            total += product['price']  # 'total' is not initialized
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    return total

print(f"Total price: {calculate_total(products)}")
```

