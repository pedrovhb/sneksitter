---
file: /home/pedro/Documents/chatgpt_export/Markdown/Detecting Deadlocks in asyncio.md
heading_stack: <root> -> 37087476-f357-4c07-bb9a-cbd6f7ce8936 -> System -> 18a374ea-54f7-408a-829d-f60766f75e3a -> System -> aaa207d7-d8c9-4cfe-a09c-7a8c955a3979 -> User -> ce028723-44f2-4667-b510-9f27ad1b64ea -> Assistant -> Detecting Deadlocks in `asyncio` -> aaa22514-b1a5-43b2-be50-0b517693a92e -> User -> 387cf5fb-37d4-4a9b-8cdf-f50ec9986d1f -> Assistant -> Components of a Resource Allocation Graph -> Using Resource Allocation Graphs to Detect Deadlocks -> Implementing RAG in Python with `asyncio` -> aaa25dfd-3475-43cd-a062-f771187415f1 -> User -> f45eab83-6841-4049-87c6-81bd58a3f62b -> Assistant -> b6c29585-72e2-42dc-acc1-722073cdd9d6 -> Tool -> 753a37e7-4caf-4283-bc69-e6c3ed4d8a11 -> Assistant -> aaa24cd5-6313-4ab5-a8e0-3a01a36a2f91 -> User -> d256a5c8-25d4-4e12-8f23-2358fbfd0ebf -> Assistant -> 42feadbe-1395-40c0-8f20-3278284ea227 -> Tool -> 49db48c7-24df-495b-9e1a-171433d17971 -> Assistant -> 965a481d-04d0-46a9-ab43-b3503dc2e2b4 -> Assistant -> e7b40687-7008-42a1-9460-98541fd4c617 -> Tool
---
# Tool

```python
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[5], line 24
     21 coro2.cr_frame.f_locals['task'] = task2
     23 # Re-run the execution
---> 24 await execute_tasks()

Cell In[3], line 7, in execute_tasks()
      5 async def execute_tasks():
      6     try:
----> 7         await asyncio.gather(task1, task2)
      8     except RuntimeError as e:
      9         print(f"Exception caught: {e}")

Cell In[5], line 4, in task_coroutine(task, resource1, resource2)
      3 async def task_coroutine(task, resource1, resource2):
----> 4     await task.acquire(resource1.name)
      5     await asyncio.sleep(0.1)
      6     await task.acquire(resource2.name)

AttributeError: 'NoneType' object has no attribute 'acquire'

```

[child ⬇️](#ee95b322-1edd-4e67-a989-8a8ab39f88e8)

---

(other branch ⎇)
###### ee95b322-1edd-4e67-a989-8a8ab39f88e8
[parent ⬆️](#e7b40687-7008-42a1-9460-98541fd4c617)
