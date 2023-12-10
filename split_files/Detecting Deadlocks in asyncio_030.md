---
file: /home/pedro/Documents/chatgpt_export/Markdown/Detecting Deadlocks in asyncio.md
heading_stack: <root> -> 37087476-f357-4c07-bb9a-cbd6f7ce8936 -> System -> 18a374ea-54f7-408a-829d-f60766f75e3a -> System -> aaa207d7-d8c9-4cfe-a09c-7a8c955a3979 -> User -> ce028723-44f2-4667-b510-9f27ad1b64ea -> Assistant -> Detecting Deadlocks in `asyncio` -> aaa22514-b1a5-43b2-be50-0b517693a92e -> User -> 387cf5fb-37d4-4a9b-8cdf-f50ec9986d1f -> Assistant -> Components of a Resource Allocation Graph -> Using Resource Allocation Graphs to Detect Deadlocks -> Implementing RAG in Python with `asyncio` -> aaa25dfd-3475-43cd-a062-f771187415f1 -> User -> f45eab83-6841-4049-87c6-81bd58a3f62b -> Assistant -> b6c29585-72e2-42dc-acc1-722073cdd9d6 -> Tool -> 753a37e7-4caf-4283-bc69-e6c3ed4d8a11 -> Assistant -> aaa24cd5-6313-4ab5-a8e0-3a01a36a2f91 -> User -> d256a5c8-25d4-4e12-8f23-2358fbfd0ebf -> Assistant -> 42feadbe-1395-40c0-8f20-3278284ea227 -> Tool
---
# Tool

```python
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[3], line 16
     13 task2 = asyncio.create_task(task_coroutine("Task_2", resource_b, resource_a))
     15 # Execute the tasks
---> 16 await execute_tasks()

Cell In[3], line 7, in execute_tasks()
      5 async def execute_tasks():
      6     try:
----> 7         await asyncio.gather(task1, task2)
      8     except RuntimeError as e:
      9         print(f"Exception caught: {e}")

Cell In[1], line 45, in task_coroutine(task_name, resource1, resource2)
     44 async def task_coroutine(task_name, resource1, resource2):
---> 45     task = CustomTask(current_task := asyncio.current_task(), name=task_name)
     46     await task.acquire(resource1.name)
     47     await asyncio.sleep(0.1)

Cell In[1], line 12, in CustomTask.__init__(self, coro, loop, name)
     11 def __init__(self, coro, *, loop=None, name=None):
---> 12     super().__init__(coro, loop=loop, name=name)
     13     self.id = id(self)
     14     # Add the task node to the RAG

TypeError: a coroutine was expected, got <Task pending name='Task-8' coro=<task_coroutine() running at /tmp/ipykernel_114/2371058986.py:45> cb=[gather.<locals>._done_callback() at /usr/lib/python3.8/asyncio/tasks.py:769]>

```

[child ⬇️](#49db48c7-24df-495b-9e1a-171433d17971)

---

(other branch ⎇)
###### 49db48c7-24df-495b-9e1a-171433d17971
[parent ⬆️](#42feadbe-1395-40c0-8f20-3278284ea227)
