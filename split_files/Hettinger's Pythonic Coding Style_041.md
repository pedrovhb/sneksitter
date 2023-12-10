---
file: /home/pedro/Documents/chatgpt_export/Markdown/Hettinger's Pythonic Coding Style.md
heading_stack: <root> -> 1d52d5fe-beae-4acc-be0e-910c2784c842 -> System -> 990cbfc8-f01c-4465-94d6-e8a9d6fea7b5 -> System -> aaa237dc-dc1e-4222-abfc-c36e07f03dac -> User -> 776fab5c-cc53-47a1-93dc-69a27010cdb2 -> Assistant -> aaa247ef-988b-49a9-9915-daf574ce71f4 -> User -> eeb04c84-cace-44d7-bbf4-3e7201f1b820 -> Assistant -> Table of Contents -> aaa2a5cc-949d-4e45-a2d0-6bec76f30b74 -> User -> 33a36459-de59-441a-b57c-b1d27d5bbad4 -> Assistant -> Futures -> 605be0ce-7fc0-47d8-8fef-58ca8a49c65f -> Assistant -> 0c6dc032-3a73-440d-914f-c72664028d9b -> Tool -> aaa454d4-0532-474b-82f6-8154c1a7612c -> Assistant -> 3237308d-b095-4d08-9746-c7458657226d -> Assistant -> aaa20508-57a4-4965-ba67-5ed4ef91fb76 -> User -> 92fb49ad-feb6-4053-983d-6b162fdbab12 -> Assistant -> d8424461-3cf2-49ac-a5da-ab7a1ddf0f99 -> Tool -> 3618722f-01ac-47cd-a789-3b6a0c7129cf -> Assistant -> Basic Usage -> Common Use-Cases -> Under the Hood -> aaa24d5e-3e65-4629-b95b-4cabd8fd44e1 -> User -> bf752daf-e729-42d7-85c7-57076960e59a -> Assistant
---
# Assistant

```python
# Advanced Usage of Futures

# Function to add a callback to the Future
def future_callback(fut):
    print(f"Callback invoked, Future result: {fut.result()}")

# Function to set the result of another Future based on the first Future
async def chain_futures(fut1, fut2):
    result = await fut1
    fut2.set_result(f"Chained: {result}")

# Run advanced Future examples
async def main_advanced():
    # Create Futures
    future1 = asyncio.Future()
    future2 = asyncio.Future()
    
    # Add a callback to future1
    future1.add_done_callback(future_callback)
    
    # Set the result for future1
    future1.set_result("Future 1 Result")
    
    # Chain future1 to future2
    await chain_futures(future1, future2)
    
    return future2.result()

# Await the advanced example
await main_advanced()
```

[child ⬇️](#d324ef77-d01a-487e-ad43-806693056408)

---

(other branch ⎇)
###### d324ef77-d01a-487e-ad43-806693056408
[parent ⬆️](#bf752daf-e729-42d7-85c7-57076960e59a)
