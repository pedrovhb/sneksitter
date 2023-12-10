---
file: /home/pedro/Documents/chatgpt_export/Markdown/Challenging Bug Scenarios.md
heading_stack: <root> -> 16b4f038-f461-4bea-aab3-f16d97102976 -> System -> f030f68c-1381-4970-ab86-0ddb5dbec373 -> System -> aaa2a9a6-bc09-4eb8-ade3-de667199f255 -> User -> 297b2268-6318-4cbd-8782-30c76dd52aa2 -> Assistant -> Scenario 1: Race Condition in Multithreading -> Scenario 2: Memory Leak -> Scenario 3: Heisenbug (Behavior changes under observation) -> Scenario 4: Non-Deterministic Behavior -> aaa2da28-e469-4aab-accc-b52d7aa18433 -> User -> 24b2a49b-4ec7-4808-8cb2-7a985f77921f -> Assistant -> Scenario 1: Nested Async Calls Hiding a Deadlock -> Scenario 2: Data Corruption due to Inconsistent Global State -> Scenario 3: Intermittent Failure due to Uninitialized Variable -> Scenario 4: Floating-Point Error in Financial Calculation
---
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
