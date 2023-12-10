---
file: /home/pedro/Documents/chatgpt_export/Markdown/Challenging Bug Scenarios.md
heading_stack: <root> -> 16b4f038-f461-4bea-aab3-f16d97102976 -> System -> f030f68c-1381-4970-ab86-0ddb5dbec373 -> System -> aaa2a9a6-bc09-4eb8-ade3-de667199f255 -> User -> 297b2268-6318-4cbd-8782-30c76dd52aa2 -> Assistant -> Scenario 1: Race Condition in Multithreading -> Scenario 2: Memory Leak -> Scenario 3: Heisenbug (Behavior changes under observation) -> Scenario 4: Non-Deterministic Behavior -> aaa2da28-e469-4aab-accc-b52d7aa18433 -> User -> 24b2a49b-4ec7-4808-8cb2-7a985f77921f -> Assistant
---
# Assistant

Certainly. Here are more elaborate examples with added complexity to mask the context, making the bugs even trickier to find and reproduce.

### Scenario 1: Nested Async Calls Hiding a Deadlock

This example uses `asyncio` to make asynchronous calls. A deadlock occurs due to improper handling of the event loop, but it's masked by seemingly unrelated API calls.

```python
import asyncio

async def fetch_data():
    await asyncio.sleep(2)
    return "data"

async def process_data():
    data = await fetch_data()
    if data:
        await asyncio.sleep(0)  # Deadlock occurs here
        return True
    return False

async def api_call_one():
    result = await process_data()
    return f"API one result: {result}"

async def api_call_two():
    await asyncio.sleep(1)
    return "API two result"

async def main():
    task_one = asyncio.create_task(api_call_one())
    task_two = asyncio.create_task(api_call_two())

    results = await asyncio.gather(task_one, task_two)
    print(results)

if __name__ == "__main__":
    asyncio.run(main())
```

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

### Scenario 4: Floating-Point Error in Financial Calculation

A program for calculating monthly payments on a loan has a bug due to floating-point arithmetic, but this is masked by rounding operations and additional calculations.

```python
import math

def calculate_monthly_payment(principal, annual_rate, years):
    n = years * 12
    r = annual_rate / 12 / 100

    # The bug: floating-point arithmetic can be imprecise
    monthly_payment = principal * r * math.pow(1 + r, n) / (math.pow(1 + r, n) - 1)
    
    # Masking the bug
    monthly_payment = round(monthly_payment, 2)
    
    extra_payment = 0.01  # additional charge
    final_payment = monthly_payment + extra_payment
    
    return final_payment

result = calculate_monthly_payment(200000, 5, 30)
print(f"Monthly payment: {result}")
```

Each of these scenarios presents a bug that's difficult to diagnose due to the surrounding context and additional complexities.

[child ⬇️](#aaa2f2f6-ffae-4515-a01d-078e412919d2)

---

(main branch ⎇)
###### aaa2f2f6-ffae-4515-a01d-078e412919d2
[parent ⬆️](#24b2a49b-4ec7-4808-8cb2-7a985f77921f)
