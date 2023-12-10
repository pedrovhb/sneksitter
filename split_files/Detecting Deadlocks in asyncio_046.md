---
file: /home/pedro/Documents/chatgpt_export/Markdown/Detecting Deadlocks in asyncio.md
heading_stack: <root> -> 37087476-f357-4c07-bb9a-cbd6f7ce8936 -> System -> 18a374ea-54f7-408a-829d-f60766f75e3a -> System -> aaa207d7-d8c9-4cfe-a09c-7a8c955a3979 -> User -> ce028723-44f2-4667-b510-9f27ad1b64ea -> Assistant -> Detecting Deadlocks in `asyncio` -> aaa22514-b1a5-43b2-be50-0b517693a92e -> User -> 387cf5fb-37d4-4a9b-8cdf-f50ec9986d1f -> Assistant -> Components of a Resource Allocation Graph -> Using Resource Allocation Graphs to Detect Deadlocks -> Implementing RAG in Python with `asyncio` -> aaa25dfd-3475-43cd-a062-f771187415f1 -> User -> f45eab83-6841-4049-87c6-81bd58a3f62b -> Assistant -> b6c29585-72e2-42dc-acc1-722073cdd9d6 -> Tool -> 753a37e7-4caf-4283-bc69-e6c3ed4d8a11 -> Assistant -> aaa24cd5-6313-4ab5-a8e0-3a01a36a2f91 -> User -> d256a5c8-25d4-4e12-8f23-2358fbfd0ebf -> Assistant -> 42feadbe-1395-40c0-8f20-3278284ea227 -> Tool -> 49db48c7-24df-495b-9e1a-171433d17971 -> Assistant -> 965a481d-04d0-46a9-ab43-b3503dc2e2b4 -> Assistant -> e7b40687-7008-42a1-9460-98541fd4c617 -> Tool -> ee95b322-1edd-4e67-a989-8a8ab39f88e8 -> Assistant -> 9fe1e873-9643-4edc-a95f-5cf8d519587e -> Assistant -> 6a55030b-9fe3-4cc7-8594-eae302b08e33 -> Tool -> 806bbcf3-849c-4b42-9a54-63fb197b0ec9 -> Assistant -> 7c10e2c3-6394-49c8-b0e5-b6698e1a565a -> Assistant
---
# Assistant

```python
# Adjusting the custom_task_factory to await the created task and pass the task object to the coroutine

async def custom_task_factory(coro_func, *args, **kwargs):
    # Initialize coroutine and CustomTask
    coro = coro_func(None, *args, **kwargs)  # Placeholder 'None' for task
    task = CustomTask(coro)
    # Update the task object in the coroutine's frame locals
    coro.cr_frame.f_locals['task'] = task
    # Await the task to completion
    await task

# Recreate tasks using the modified CustomTask and Resource classes
async def execute_tasks():
    try:
        task1 = asyncio.create_task(custom_task_factory(task_coroutine, resource_a, resource_b))
        task2 = asyncio.create_task(custom_task_factory(task_coroutine, resource_b, resource_a))
        await asyncio.gather(task1, task2)
    except RuntimeError as e:
        print(f"Exception caught: {e}")

# Reset the RAG to avoid conflicts with the previous example
rag = nx.DiGraph()

# Execute the tasks
await execute_tasks()
```

[child ⬇️](#54845f93-f188-4521-92fb-73eab95ebcfb)

---

(other branch ⎇)
###### 54845f93-f188-4521-92fb-73eab95ebcfb
[parent ⬆️](#7c10e2c3-6394-49c8-b0e5-b6698e1a565a)
