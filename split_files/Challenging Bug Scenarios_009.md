---
file: /home/pedro/Documents/chatgpt_export/Markdown/Challenging Bug Scenarios.md
heading_stack: <root> -> 16b4f038-f461-4bea-aab3-f16d97102976 -> System -> f030f68c-1381-4970-ab86-0ddb5dbec373 -> System -> aaa2a9a6-bc09-4eb8-ade3-de667199f255 -> User -> 297b2268-6318-4cbd-8782-30c76dd52aa2 -> Assistant -> Scenario 1: Race Condition in Multithreading
---
### Scenario 1: Race Condition in Multithreading
A program that calculates the sum of squares for a list of numbers using threads. Due to a race condition, the final sum can be incorrect.

```python
from threading import Thread
from random import randint
import time

total = 0

def calculate_square(numbers):
    global total
    for n in numbers:
        time.sleep(randint(0, 2) / 10)  # Simulate some delay
        total += n * n

numbers = [1, 2, 3, 4, 5]
t1 = Thread(target=calculate_square, args=(numbers[:3],))
t2 = Thread(target=calculate_square, args=(numbers[3:],))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Total sum of squares: {total}")  # Incorrect due to race condition
```

