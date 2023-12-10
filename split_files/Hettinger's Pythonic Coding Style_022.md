---
file: /home/pedro/Documents/chatgpt_export/Markdown/Hettinger's Pythonic Coding Style.md
heading_stack: <root> -> 1d52d5fe-beae-4acc-be0e-910c2784c842 -> System -> 990cbfc8-f01c-4465-94d6-e8a9d6fea7b5 -> System -> aaa237dc-dc1e-4222-abfc-c36e07f03dac -> User -> 776fab5c-cc53-47a1-93dc-69a27010cdb2 -> Assistant -> aaa247ef-988b-49a9-9915-daf574ce71f4 -> User -> eeb04c84-cace-44d7-bbf4-3e7201f1b820 -> Assistant -> Table of Contents -> aaa2a5cc-949d-4e45-a2d0-6bec76f30b74 -> User -> 33a36459-de59-441a-b57c-b1d27d5bbad4 -> Assistant -> Futures -> 605be0ce-7fc0-47d8-8fef-58ca8a49c65f -> Assistant -> 0c6dc032-3a73-440d-914f-c72664028d9b -> Tool
---
# Tool

```python
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
Cell In[1], line 26
     23     return result
     25 # Run the event loop
---> 26 asyncio.run(main())

File /usr/lib/python3.8/asyncio/runners.py:33, in run(main, debug)
      9 """Execute the coroutine and return the result.
     10 
     11 This function runs the passed coroutine, taking care of
   (...)
     30     asyncio.run(main())
     31 """
     32 if events._get_running_loop() is not None:
---> 33     raise RuntimeError(
     34         "asyncio.run() cannot be called from a running event loop")
     36 if not coroutines.iscoroutine(main):
     37     raise ValueError("a coroutine was expected, got {!r}".format(main))

RuntimeError: asyncio.run() cannot be called from a running event loop

```

[child ⬇️](#aaa454d4-0532-474b-82f6-8154c1a7612c)

---

(other branch ⎇)
###### aaa454d4-0532-474b-82f6-8154c1a7612c
[parent ⬆️](#0c6dc032-3a73-440d-914f-c72664028d9b)
