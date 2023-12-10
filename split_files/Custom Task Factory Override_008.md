---
file: /home/pedro/Documents/chatgpt_export/Markdown/Custom Task Factory Override.md
heading_stack: <root> -> 2ab8dc66-9c51-4664-90e9-06291e31eb26 -> System -> b8afa332-1ea4-489a-809b-ea613254549b -> System -> aaa2f793-43f9-4f7d-b610-c0383df035ef -> User -> e51f6927-b9b1-45af-902f-ed18fb8f792f -> Assistant
---
# Assistant

```python
import asyncio

# Custom Task Factory Function
def custom_task_factory(loop, coro):
    print("Creating a new task.")
    return asyncio.Task(coro, loop=loop)

# A simple asynchronous function
async def my_coro():
    print("Running in coroutine")
    await asyncio.sleep(1)
    print("Coroutine completed")

# Setting up the event loop and task factory
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.set_task_factory(custom_task_factory)

# Creating a task using the custom factory
task = loop.create_task(my_coro())

# Running the event loop
loop.run_until_complete(task)
```

[child ⬇️](#c0e1b261-c980-4a5f-b391-32529049bb4a)

---

(main branch ⎇)
###### c0e1b261-c980-4a5f-b391-32529049bb4a
[parent ⬆️](#e51f6927-b9b1-45af-902f-ed18fb8f792f)
