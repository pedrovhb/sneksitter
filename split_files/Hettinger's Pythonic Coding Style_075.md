---
file: /home/pedro/Documents/chatgpt_export/Markdown/Hettinger's Pythonic Coding Style.md
heading_stack: <root> -> 1d52d5fe-beae-4acc-be0e-910c2784c842 -> System -> 990cbfc8-f01c-4465-94d6-e8a9d6fea7b5 -> System -> aaa237dc-dc1e-4222-abfc-c36e07f03dac -> User -> 776fab5c-cc53-47a1-93dc-69a27010cdb2 -> Assistant -> aaa247ef-988b-49a9-9915-daf574ce71f4 -> User -> eeb04c84-cace-44d7-bbf4-3e7201f1b820 -> Assistant -> Table of Contents -> aaa2a5cc-949d-4e45-a2d0-6bec76f30b74 -> User -> 33a36459-de59-441a-b57c-b1d27d5bbad4 -> Assistant -> Futures -> 605be0ce-7fc0-47d8-8fef-58ca8a49c65f -> Assistant -> 0c6dc032-3a73-440d-914f-c72664028d9b -> Tool -> aaa454d4-0532-474b-82f6-8154c1a7612c -> Assistant -> 3237308d-b095-4d08-9746-c7458657226d -> Assistant -> aaa20508-57a4-4965-ba67-5ed4ef91fb76 -> User -> 92fb49ad-feb6-4053-983d-6b162fdbab12 -> Assistant -> d8424461-3cf2-49ac-a5da-ab7a1ddf0f99 -> Tool -> 3618722f-01ac-47cd-a789-3b6a0c7129cf -> Assistant -> Basic Usage -> Common Use-Cases -> Under the Hood -> aaa24d5e-3e65-4629-b95b-4cabd8fd44e1 -> User -> bf752daf-e729-42d7-85c7-57076960e59a -> Assistant -> d324ef77-d01a-487e-ad43-806693056408 -> Tool -> 3c13d1e9-f19f-4d1b-8cc5-134da804ac7d -> Assistant -> Advanced Usage -> Common Use-Cases for Advanced Features -> Under the Hood -> aaa24a82-59ae-4e30-baea-124b766b1cca -> User -> 48a83ee5-bb35-45fe-ac72-347b9a5cde78 -> Assistant -> 114949b2-0cda-4a48-a746-565185d983f7 -> Tool -> 9351035a-5fb3-4196-ab28-00f2d055f2a4 -> Assistant -> Lock -> 1. Acquiring and Releasing a Lock -> 2. Common Use-Cases -> 3. Under the Hood -> aaa26ea7-be3a-4754-8041-262f7d594988 -> User -> 6dc0b33d-eb92-4e52-a234-fd71a726b982 -> Assistant -> 716051e8-b953-427b-9094-4784bd24bf52 -> Tool -> c82dea23-a791-4ced-8798-9ac54e1a4f59 -> Assistant -> 2. Timeouts -> 3. Common Use-Cases for Timeouts -> 4. Under the Hood for Timeouts -> aaa2b275-90be-40ad-9f74-8a2e476ea8fa -> User -> 4216df09-bc59-4114-82b2-aa56a485dec7 -> Assistant
---
# Assistant

```python
# Initialize an Event
event = asyncio.Event()

# Function to set the Event
async def setter():
    print("Setter: Sleeping for 1s")
    await asyncio.sleep(1)
    print("Setter: Setting event")
    event.set()

# Function to wait for the Event
async def waiter(name):
    print(f"{name}: Waiting for event to be set")
    await event.wait()
    print(f"{name}: Event is set, proceeding")

# Run setter and waiter tasks
async def main_event():
    setter_task = asyncio.create_task(setter())
    waiter1_task = asyncio.create_task(waiter("Waiter 1"))
    waiter2_task = asyncio.create_task(waiter("Waiter 2"))
    
    await setter_task
    await waiter1_task
    await waiter2_task

# Await the event example
await main_event()
```

[child ⬇️](#bb800078-4902-40c4-841d-3d2158678bbc)

---

(other branch ⎇)
###### bb800078-4902-40c4-841d-3d2158678bbc
[parent ⬆️](#4216df09-bc59-4114-82b2-aa56a485dec7)