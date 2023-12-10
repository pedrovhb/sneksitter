---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python LSP Client Writing.md
heading_stack: <root> -> fb86b0e7-bf62-4975-be52-afe44c28e2ea -> System -> 93a72920-b6b0-4849-ae9f-6a6bac06bf87 -> System -> aaa23743-d4b8-479a-9cf4-b7e357d2d973 -> User -> 3a85587d-63d2-4e15-a912-383beeee1f3b -> Assistant -> 2cbd10f3-6642-4021-9e90-a67e05827bf9 -> Tool -> 22a86aba-e3b8-4805-a841-9752070c999b -> Assistant -> Language Server Protocol (LSP) -> Features -> Workflow -> Writing a Python Client for LSP -> Example Libraries -> Example Code Outline -> aaa2528e-4c1f-4ad0-991b-16ed764da716 -> User -> 4a334677-9d0e-4635-afaa-e2795893b1a9 -> Assistant -> c3734514-9dae-4be3-8123-c1558578e838 -> Tool
---
# Tool

```python
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
Cell In[2], line 51
     48     return response
     50 # Run the main coroutine to launch and initialize the LSP server
---> 51 lsp_response = asyncio.run(main())
     52 lsp_response

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

[child ⬇️](#0f6f37b3-6ec2-43a7-b76f-bae08d4ce51c)

---

(other branch ⎇)
###### 0f6f37b3-6ec2-43a7-b76f-bae08d4ce51c
[parent ⬆️](#c3734514-9dae-4be3-8123-c1558578e838)
