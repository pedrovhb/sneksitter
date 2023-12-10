---
file: /home/pedro/Documents/chatgpt_export/Markdown/Custom Task Factory Override.md
heading_stack: <root> -> 2ab8dc66-9c51-4664-90e9-06291e31eb26 -> System -> b8afa332-1ea4-489a-809b-ea613254549b -> System -> aaa2f793-43f9-4f7d-b610-c0383df035ef -> User -> e51f6927-b9b1-45af-902f-ed18fb8f792f -> Assistant -> c0e1b261-c980-4a5f-b391-32529049bb4a -> Tool -> de2b3bf3-2dc0-4443-b496-b9989d9a7faa -> Assistant -> b7a1266d-90be-4300-ae02-79a0ca6ecfc3 -> Assistant -> 2e81c05c-a23c-4caf-a129-1e2533c68919 -> Tool -> 29673e15-8598-4546-a8b2-91dcc341abd3 -> Assistant -> aaa2dc8b-2afe-467b-9cb0-fef2e64c7057 -> User -> dc4a074b-2ef5-4fa3-bb90-2094af9666eb -> Assistant -> aaa269ee-9a58-44cb-980c-0c8b9ba11898 -> User -> 7785f4ab-a474-4361-9f01-95802d62b670 -> Assistant
---
# Assistant

```python
# Custom Task Factory Function with additional logging
def custom_task_factory_with_info(loop, coro):
    print(f"Creating a new task.")
    
    # Inspect the loop
    print(f"Is loop closed: {loop.is_closed()}")
    print(f"Loop time: {loop.time()}")
    
    # Inspect the coroutine
    print(f"Coroutine code object: {coro.cr_code}")
    print(f"Coroutine frame object: {coro.cr_frame}")

    return asyncio.Task(coro, loop=loop)

# Update the task factory for the current event loop
current_loop.set_task_factory(custom_task_factory_with_info)

# Create and run a task using the updated custom factory
task_with_info = asyncio.ensure_future(my_coro())
await task_with_info
```

[child ⬇️](#dfe64904-ae71-4b3c-be04-5854a684db3d)

---

(main branch ⎇)
###### dfe64904-ae71-4b3c-be04-5854a684db3d
[parent ⬆️](#7785f4ab-a474-4361-9f01-95802d62b670)
