---
file: /home/pedro/Documents/chatgpt_export/Markdown/Challenging Bug Scenarios.md
heading_stack: <root> -> 16b4f038-f461-4bea-aab3-f16d97102976 -> System -> f030f68c-1381-4970-ab86-0ddb5dbec373 -> System -> aaa2a9a6-bc09-4eb8-ade3-de667199f255 -> User -> 297b2268-6318-4cbd-8782-30c76dd52aa2 -> Assistant -> Scenario 1: Race Condition in Multithreading -> Scenario 2: Memory Leak -> Scenario 3: Heisenbug (Behavior changes under observation) -> Scenario 4: Non-Deterministic Behavior -> aaa2da28-e469-4aab-accc-b52d7aa18433 -> User -> 24b2a49b-4ec7-4808-8cb2-7a985f77921f -> Assistant -> Scenario 1: Nested Async Calls Hiding a Deadlock
---
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

