---
file: /home/pedro/Documents/chatgpt_export/Markdown/Challenging Bug Scenarios.md
heading_stack: <root> -> 16b4f038-f461-4bea-aab3-f16d97102976 -> System -> f030f68c-1381-4970-ab86-0ddb5dbec373 -> System -> aaa2a9a6-bc09-4eb8-ade3-de667199f255 -> User -> 297b2268-6318-4cbd-8782-30c76dd52aa2 -> Assistant -> Scenario 1: Race Condition in Multithreading -> Scenario 2: Memory Leak -> Scenario 3: Heisenbug (Behavior changes under observation)
---
### Scenario 3: Heisenbug (Behavior changes under observation)
A program that behaves differently when running in debug mode due to time-sensitive operations.

```python
import logging
import time

def time_sensitive_operation():
    start_time = time.time()
    # Do something
    time.sleep(0.1)
    end_time = time.time()

    if end_time - start_time > 0.2:
        logging.debug("Operation took too long")
        return False
    return True

# Uncommenting the following line makes the bug go away
# logging.basicConfig(level=logging.DEBUG)

result = time_sensitive_operation()
print(f"Result: {result}")
```

