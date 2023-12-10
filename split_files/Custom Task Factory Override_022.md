---
file: /home/pedro/Documents/chatgpt_export/Markdown/Custom Task Factory Override.md
heading_stack: <root> -> 2ab8dc66-9c51-4664-90e9-06291e31eb26 -> System -> b8afa332-1ea4-489a-809b-ea613254549b -> System -> aaa2f793-43f9-4f7d-b610-c0383df035ef -> User -> e51f6927-b9b1-45af-902f-ed18fb8f792f -> Assistant -> c0e1b261-c980-4a5f-b391-32529049bb4a -> Tool -> de2b3bf3-2dc0-4443-b496-b9989d9a7faa -> Assistant -> b7a1266d-90be-4300-ae02-79a0ca6ecfc3 -> Assistant -> 2e81c05c-a23c-4caf-a129-1e2533c68919 -> Tool -> 29673e15-8598-4546-a8b2-91dcc341abd3 -> Assistant -> aaa2dc8b-2afe-467b-9cb0-fef2e64c7057 -> User -> dc4a074b-2ef5-4fa3-bb90-2094af9666eb -> Assistant
---
# Assistant

The task factory function takes two arguments:

1. `loop`: This is the event loop object that the task will be associated with. You can use this object to query or modify the event loop's behavior or state. For example, you could gather metrics or apply some global settings to all tasks.

2. `coro`: This is the coroutine object that the task will run. You can inspect this object to get information about the coroutine itself, such as its name or the function it wraps. However, please note that manipulating this object could lead to undefined behavior unless you know exactly what you're doing.

Here are some specific things you could potentially access or do:

- `loop.is_closed()`: Check if the loop is closed.
- `loop.time()`: Get the current time according to the event loop’s internal clock.
  
- `coro.cr_code`: Access the code object of the coroutine (low-level).
- `coro.cr_frame`: Access the frame object of the coroutine (low-level).

Would you like a code demo to explore some of these aspects?

[child ⬇️](#aaa269ee-9a58-44cb-980c-0c8b9ba11898)

---

(main branch ⎇)
###### aaa269ee-9a58-44cb-980c-0c8b9ba11898
[parent ⬆️](#dc4a074b-2ef5-4fa3-bb90-2094af9666eb)
