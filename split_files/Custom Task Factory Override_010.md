---
file: /home/pedro/Documents/chatgpt_export/Markdown/Custom Task Factory Override.md
heading_stack: <root> -> 2ab8dc66-9c51-4664-90e9-06291e31eb26 -> System -> b8afa332-1ea4-489a-809b-ea613254549b -> System -> aaa2f793-43f9-4f7d-b610-c0383df035ef -> User -> e51f6927-b9b1-45af-902f-ed18fb8f792f -> Assistant -> c0e1b261-c980-4a5f-b391-32529049bb4a -> Tool
---
# Tool

```python
Creating a new task.
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
Cell In[1], line 23
     20 task = loop.create_task(my_coro())
     22 # Running the event loop
---> 23 loop.run_until_complete(task)

File /usr/lib/python3.8/asyncio/base_events.py:592, in BaseEventLoop.run_until_complete(self, future)
    581 """Run until the Future is done.
    582 
    583 If the argument is a coroutine, it is wrapped in a Task.
   (...)
    589 Return the Future's result, or raise its exception.
    590 """
    591 self._check_closed()
--> 592 self._check_running()
    594 new_task = not futures.isfuture(future)
    595 future = tasks.ensure_future(future, loop=self)

File /usr/lib/python3.8/asyncio/base_events.py:554, in BaseEventLoop._check_running(self)
    552     raise RuntimeError('This event loop is already running')
    553 if events._get_running_loop() is not None:
--> 554     raise RuntimeError(
    555         'Cannot run the event loop while another loop is running')

RuntimeError: Cannot run the event loop while another loop is running

```

[child ⬇️](#de2b3bf3-2dc0-4443-b496-b9989d9a7faa)

---

(main branch ⎇)
###### de2b3bf3-2dc0-4443-b496-b9989d9a7faa
[parent ⬆️](#c0e1b261-c980-4a5f-b391-32529049bb4a)
