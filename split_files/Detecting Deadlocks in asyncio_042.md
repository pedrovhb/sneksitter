---
file: /home/pedro/Documents/chatgpt_export/Markdown/Detecting Deadlocks in asyncio.md
heading_stack: <root> -> 37087476-f357-4c07-bb9a-cbd6f7ce8936 -> System -> 18a374ea-54f7-408a-829d-f60766f75e3a -> System -> aaa207d7-d8c9-4cfe-a09c-7a8c955a3979 -> User -> ce028723-44f2-4667-b510-9f27ad1b64ea -> Assistant -> Detecting Deadlocks in `asyncio` -> aaa22514-b1a5-43b2-be50-0b517693a92e -> User -> 387cf5fb-37d4-4a9b-8cdf-f50ec9986d1f -> Assistant -> Components of a Resource Allocation Graph -> Using Resource Allocation Graphs to Detect Deadlocks -> Implementing RAG in Python with `asyncio` -> aaa25dfd-3475-43cd-a062-f771187415f1 -> User -> f45eab83-6841-4049-87c6-81bd58a3f62b -> Assistant -> b6c29585-72e2-42dc-acc1-722073cdd9d6 -> Tool -> 753a37e7-4caf-4283-bc69-e6c3ed4d8a11 -> Assistant -> aaa24cd5-6313-4ab5-a8e0-3a01a36a2f91 -> User -> d256a5c8-25d4-4e12-8f23-2358fbfd0ebf -> Assistant -> 42feadbe-1395-40c0-8f20-3278284ea227 -> Tool -> 49db48c7-24df-495b-9e1a-171433d17971 -> Assistant -> 965a481d-04d0-46a9-ab43-b3503dc2e2b4 -> Assistant -> e7b40687-7008-42a1-9460-98541fd4c617 -> Tool -> ee95b322-1edd-4e67-a989-8a8ab39f88e8 -> Assistant -> 9fe1e873-9643-4edc-a95f-5cf8d519587e -> Assistant -> 6a55030b-9fe3-4cc7-8594-eae302b08e33 -> Tool
---
# Tool

```python
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[7], line 28
     25     except RuntimeError as e:
     26         print(f"Exception caught: {e}")
---> 28 await execute_tasks()

Cell In[7], line 24, in execute_tasks()
     22     task1 = custom_task_factory(task_coroutine, resource_a, resource_b)
     23     task2 = custom_task_factory(task_coroutine, resource_b, resource_a)
---> 24     await asyncio.gather(task1, task2)
     25 except RuntimeError as e:
     26     print(f"Exception caught: {e}")

Cell In[7], line 5, in custom_task_factory(coro_func, *args, **kwargs)
      4 async def custom_task_factory(coro_func, *args, **kwargs):
----> 5     coro = coro_func(*args, **kwargs)
      6     task = CustomTask(coro)
      7     coro.cr_frame.f_locals['task'] = task

TypeError: task_coroutine() missing 1 required positional argument: 'resource2'

```

[child ⬇️](#806bbcf3-849c-4b42-9a54-63fb197b0ec9)

---

(other branch ⎇)
###### 806bbcf3-849c-4b42-9a54-63fb197b0ec9
[parent ⬆️](#6a55030b-9fe3-4cc7-8594-eae302b08e33)
