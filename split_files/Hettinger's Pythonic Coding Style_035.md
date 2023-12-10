---
file: /home/pedro/Documents/chatgpt_export/Markdown/Hettinger's Pythonic Coding Style.md
heading_stack: <root> -> 1d52d5fe-beae-4acc-be0e-910c2784c842 -> System -> 990cbfc8-f01c-4465-94d6-e8a9d6fea7b5 -> System -> aaa237dc-dc1e-4222-abfc-c36e07f03dac -> User -> 776fab5c-cc53-47a1-93dc-69a27010cdb2 -> Assistant -> aaa247ef-988b-49a9-9915-daf574ce71f4 -> User -> eeb04c84-cace-44d7-bbf4-3e7201f1b820 -> Assistant -> Table of Contents -> aaa2a5cc-949d-4e45-a2d0-6bec76f30b74 -> User -> 33a36459-de59-441a-b57c-b1d27d5bbad4 -> Assistant -> Futures -> 605be0ce-7fc0-47d8-8fef-58ca8a49c65f -> Assistant -> 0c6dc032-3a73-440d-914f-c72664028d9b -> Tool -> aaa454d4-0532-474b-82f6-8154c1a7612c -> Assistant -> 3237308d-b095-4d08-9746-c7458657226d -> Assistant -> aaa20508-57a4-4965-ba67-5ed4ef91fb76 -> User -> 92fb49ad-feb6-4053-983d-6b162fdbab12 -> Assistant -> d8424461-3cf2-49ac-a5da-ab7a1ddf0f99 -> Tool -> 3618722f-01ac-47cd-a789-3b6a0c7129cf -> Assistant -> Basic Usage
---
#### Basic Usage

1. **Creating a Future**
    - We created an asyncio Future object using `asyncio.Future()`. This object will hold the result of an asynchronous operation.

```python
future = asyncio.Future()
```

2. **Setting and Getting the Result**
    - We defined two asynchronous functions: `set_future_result` and `get_future_result`. The former sets the result of the future after a simulated delay (`await asyncio.sleep(1)`), and the latter awaits the future to get its result.

```python
async def set_future_result():
    await asyncio.sleep(1)
    future.set_result("Hello, Future!")

async def get_future_result():
    result = await future
    return result
```

3. **Running Both Functions**
    - Both functions are scheduled to run asynchronously. The result is set after a delay of 1 second, and then it is retrieved.

```python
set_result_task = asyncio.create_task(set_future_result())
get_result_task = asyncio.create_task(get_future_result())
```

