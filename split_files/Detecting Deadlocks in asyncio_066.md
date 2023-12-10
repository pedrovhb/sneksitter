---
file: /home/pedro/Documents/chatgpt_export/Markdown/Detecting Deadlocks in asyncio.md
heading_stack: <root> -> 37087476-f357-4c07-bb9a-cbd6f7ce8936 -> System -> 18a374ea-54f7-408a-829d-f60766f75e3a -> System -> aaa207d7-d8c9-4cfe-a09c-7a8c955a3979 -> User -> ce028723-44f2-4667-b510-9f27ad1b64ea -> Assistant -> Detecting Deadlocks in `asyncio` -> aaa22514-b1a5-43b2-be50-0b517693a92e -> User -> 387cf5fb-37d4-4a9b-8cdf-f50ec9986d1f -> Assistant -> Components of a Resource Allocation Graph -> Using Resource Allocation Graphs to Detect Deadlocks -> Implementing RAG in Python with `asyncio` -> aaa25dfd-3475-43cd-a062-f771187415f1 -> User -> f45eab83-6841-4049-87c6-81bd58a3f62b -> Assistant -> b6c29585-72e2-42dc-acc1-722073cdd9d6 -> Tool -> 753a37e7-4caf-4283-bc69-e6c3ed4d8a11 -> Assistant -> aaa24cd5-6313-4ab5-a8e0-3a01a36a2f91 -> User -> d256a5c8-25d4-4e12-8f23-2358fbfd0ebf -> Assistant -> 42feadbe-1395-40c0-8f20-3278284ea227 -> Tool -> 49db48c7-24df-495b-9e1a-171433d17971 -> Assistant -> 965a481d-04d0-46a9-ab43-b3503dc2e2b4 -> Assistant -> e7b40687-7008-42a1-9460-98541fd4c617 -> Tool -> ee95b322-1edd-4e67-a989-8a8ab39f88e8 -> Assistant -> 9fe1e873-9643-4edc-a95f-5cf8d519587e -> Assistant -> 6a55030b-9fe3-4cc7-8594-eae302b08e33 -> Tool -> 806bbcf3-849c-4b42-9a54-63fb197b0ec9 -> Assistant -> 7c10e2c3-6394-49c8-b0e5-b6698e1a565a -> Assistant -> 54845f93-f188-4521-92fb-73eab95ebcfb -> Tool -> 975536f5-3987-424a-ab40-f6786a573335 -> Assistant -> a7772d41-6cbc-42ab-b02a-6b4212f7b7f4 -> Assistant -> 93112e53-5832-48a0-9298-226568732913 -> Tool -> b15b384e-18ad-4f96-83f2-4860a21407b6 -> Assistant -> 299a560a-e87e-4fb8-aff4-c17228986602 -> Assistant -> 3b4f9e2f-512a-422f-b90e-f9678b6f85de -> Assistant -> aaa2ca36-73da-4a0c-a9d7-179bd806f9e9 -> User -> b108cf81-249e-47a3-82b1-791d88ae8486 -> Assistant -> e3d44ddc-eb25-43a2-925c-4f17ff61feac -> Tool
---
# Tool

```python
---------------------------------------------------------------------------
RecursionError                            Traceback (most recent call last)
Cell In[1], line 72
     69         print("No deadlock detected.")
     71 # Execute the main coroutine
---> 72 await main()

Cell In[1], line 61, in main()
     58 async def main():
     59     lock1 = CustomLock('Lock1')
---> 61     task1 = asyncio.create_task(worker(lock1, 'Task1'))
     62     task2 = asyncio.create_task(worker(lock1, 'Task2'))
     64     await asyncio.gather(task1, task2)

File /usr/lib/python3.8/asyncio/tasks.py:382, in create_task(coro, name)
    377 """Schedule the execution of a coroutine object in a spawn task.
    378 
    379 Return a Task object.
    380 """
    381 loop = events.get_running_loop()
--> 382 task = loop.create_task(coro)
    383 _set_task_name(task, name)
    384 return task

File /usr/lib/python3.8/asyncio/base_events.py:435, in BaseEventLoop.create_task(self, coro, name)
    433         del task._source_traceback[-1]
    434 else:
--> 435     task = self._task_factory(self, coro)
    436     tasks._set_task_name(task, name)
    438 return task

Cell In[1], line 36, in custom_task_factory(loop, coro, name)
     33 def custom_task_factory(loop: asyncio.AbstractEventLoop,
     34                         coro: Union[Callable, asyncio.Future],
     35                         name: str = None) -> asyncio.Task:
---> 36     task = loop.create_task(coro)
     37     if name:
     38         task.set_name(name)

File /usr/lib/python3.8/asyncio/base_events.py:435, in BaseEventLoop.create_task(self, coro, name)
    433         del task._source_traceback[-1]
    434 else:
--> 435     task = self._task_factory(self, coro)
    436     tasks._set_task_name(task, name)
    438 return task

Cell In[1], line 36, in custom_task_factory(loop, coro, name)
     33 def custom_task_factory(loop: asyncio.AbstractEventLoop,
     34                         coro: Union[Callable, asyncio.Future],
     35                         name: str = None) -> asyncio.Task:
---> 36     task = loop.create_task(coro)
     37     if name:
     38         task.set_name(name)

    [... skipping similar frames: BaseEventLoop.create_task at line 435 (1488 times), custom_task_factory at line 36 (1488 times)]

File /usr/lib/python3.8/asyncio/base_events.py:435, in BaseEventLoop.create_task(self, coro, name)
    433         del task._source_traceback[-1]
    434 else:
--> 435     task = self._task_factory(self, coro)
    436     tasks._set_task_name(task, name)
    438 return task

Cell In[1], line 36, in custom_task_factory(loop, coro, name)
     33 def custom_task_factory(loop: asyncio.AbstractEventLoop,
     34                         coro: Union[Callable, asyncio.Future],
     35                         name: str = None) -> asyncio.Task:
---> 36     task = loop.create_task(coro)
     37     if name:
     38         task.set_name(name)

RecursionError: maximum recursion depth exceeded

```

[child ⬇️](#e8aff250-3f31-458e-a52e-0941b427b133)

---

(main branch ⎇)
###### e8aff250-3f31-458e-a52e-0941b427b133
[parent ⬆️](#e3d44ddc-eb25-43a2-925c-4f17ff61feac)
