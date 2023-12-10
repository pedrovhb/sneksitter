---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python LSP Client Writing.md
heading_stack: <root> -> fb86b0e7-bf62-4975-be52-afe44c28e2ea -> System -> 93a72920-b6b0-4849-ae9f-6a6bac06bf87 -> System -> aaa23743-d4b8-479a-9cf4-b7e357d2d973 -> User -> 3a85587d-63d2-4e15-a912-383beeee1f3b -> Assistant -> 2cbd10f3-6642-4021-9e90-a67e05827bf9 -> Tool -> 22a86aba-e3b8-4805-a841-9752070c999b -> Assistant -> Language Server Protocol (LSP) -> Features -> Workflow -> Writing a Python Client for LSP -> Example Libraries -> Example Code Outline -> aaa2528e-4c1f-4ad0-991b-16ed764da716 -> User -> 4a334677-9d0e-4635-afaa-e2795893b1a9 -> Assistant -> c3734514-9dae-4be3-8123-c1558578e838 -> Tool -> 0f6f37b3-6ec2-43a7-b76f-bae08d4ce51c -> Assistant -> 580895c4-5981-4f16-a55d-41ba1ab8af1e -> Assistant -> 6e38ed5a-91cb-43b9-986c-658dcecf8cf0 -> Tool
---
# Tool

```python
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
Cell In[3], line 38
     36 # Running the coroutine to interact with python-lsp-server
     37 loop = asyncio.get_event_loop()
---> 38 lsp_init_response = loop.run_until_complete(lsp_example())
     39 lsp_init_response

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

File /usr/lib/python3.8/asyncio/base_events.py:552, in BaseEventLoop._check_running(self)
    550 def _check_running(self):
    551     if self.is_running():
--> 552         raise RuntimeError('This event loop is already running')
    553     if events._get_running_loop() is not None:
    554         raise RuntimeError(
    555             'Cannot run the event loop while another loop is running')

RuntimeError: This event loop is already running

```

[child ⬇️](#9fff6a60-716a-4a71-ba99-d15523367a56)

---

(other branch ⎇)
###### 9fff6a60-716a-4a71-ba99-d15523367a56
[parent ⬆️](#6e38ed5a-91cb-43b9-986c-658dcecf8cf0)
