---
file: /home/pedro/Documents/chatgpt_export/Markdown/Challenging Bug Scenarios.md
heading_stack: <root> -> 16b4f038-f461-4bea-aab3-f16d97102976 -> System -> f030f68c-1381-4970-ab86-0ddb5dbec373 -> System -> aaa2a9a6-bc09-4eb8-ade3-de667199f255 -> User -> 297b2268-6318-4cbd-8782-30c76dd52aa2 -> Assistant -> Scenario 1: Race Condition in Multithreading -> Scenario 2: Memory Leak -> Scenario 3: Heisenbug (Behavior changes under observation) -> Scenario 4: Non-Deterministic Behavior -> aaa2da28-e469-4aab-accc-b52d7aa18433 -> User -> 24b2a49b-4ec7-4808-8cb2-7a985f77921f -> Assistant -> Scenario 1: Nested Async Calls Hiding a Deadlock -> Scenario 2: Data Corruption due to Inconsistent Global State
---
### Scenario 2: Data Corruption due to Inconsistent Global State

The following program simulates a basic inventory system. A bug occurs where the global state becomes inconsistent, leading to data corruption. However, the bug is masked by a seemingly functional logging mechanism.

```python
inventory = {}

def add_item(item, quantity):
    global inventory
    inventory[item] = inventory.get(item, 0) + quantity

def remove_item(item, quantity):
    global inventory
    if item in inventory and inventory[item] >= quantity:
        inventory[item] -= quantity

def log_inventory():
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def process_order(item, quantity):
    add_item(item, quantity)
    log_inventory()
    remove_item(item, quantity // 2)  # Bug: Should be 'quantity'
    log_inventory()

process_order('apple', 10)
process_order('banana', 5)
```

