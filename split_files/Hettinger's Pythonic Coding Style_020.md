---
file: /home/pedro/Documents/chatgpt_export/Markdown/Hettinger's Pythonic Coding Style.md
heading_stack: <root> -> 1d52d5fe-beae-4acc-be0e-910c2784c842 -> System -> 990cbfc8-f01c-4465-94d6-e8a9d6fea7b5 -> System -> aaa237dc-dc1e-4222-abfc-c36e07f03dac -> User -> 776fab5c-cc53-47a1-93dc-69a27010cdb2 -> Assistant -> aaa247ef-988b-49a9-9915-daf574ce71f4 -> User -> eeb04c84-cace-44d7-bbf4-3e7201f1b820 -> Assistant -> Table of Contents -> aaa2a5cc-949d-4e45-a2d0-6bec76f30b74 -> User -> 33a36459-de59-441a-b57c-b1d27d5bbad4 -> Assistant -> Futures -> 605be0ce-7fc0-47d8-8fef-58ca8a49c65f -> Assistant
---
# Assistant

```python
import asyncio

# Creating a Future
future = asyncio.Future()

# Function to set the result of the Future
async def set_future_result():
    await asyncio.sleep(1)
    future.set_result("Hello, Future!")

# Function to get the result of the Future
async def get_future_result():
    result = await future
    return result

# Run both functions
async def main():
    set_result_task = asyncio.create_task(set_future_result())
    get_result_task = asyncio.create_task(get_future_result())

    await set_result_task
    result = await get_result_task
    return result

# Run the event loop
asyncio.run(main())
```

[child ⬇️](#0c6dc032-3a73-440d-914f-c72664028d9b)

---

(other branch ⎇)
###### 0c6dc032-3a73-440d-914f-c72664028d9b
[parent ⬆️](#605be0ce-7fc0-47d8-8fef-58ca8a49c65f)
