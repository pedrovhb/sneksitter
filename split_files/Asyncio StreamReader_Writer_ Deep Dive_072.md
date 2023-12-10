---
file: /home/pedro/Documents/chatgpt_export/Markdown/Asyncio StreamReader_Writer_ Deep Dive.md
heading_stack: <root> -> fcadc37a-73b3-4d5c-8df9-b161199195c8 -> System -> b74b0f9d-258d-4711-a53e-a6ef4f3e749e -> System -> aaa2d34c-19b8-4a73-87e5-e89cc52880f1 -> User -> e699cc32-2076-4b5d-98e8-d8c8d270498e -> Assistant -> asyncio StreamReader and StreamWriter: A Deep Dive -> StreamReader -> Basics -> Core Methods -> Use Case -> StreamWriter -> Basics -> Core Methods -> Use Case -> Combining StreamReader and StreamWriter -> Buffering and Flow Control -> Exception Handling -> Backpressure Handling -> Stream Adapters -> Conclusion -> aaa2cf71-b96b-4015-b8df-dadb1288a43a -> User -> 7f748aa6-27c6-4794-ad0d-049b6f2f97d5 -> Assistant -> Factors Affecting Overhead -> Quantitative Measures -> aaa28268-171d-4aa2-a801-59980b4a1c72 -> User -> f0baf8c5-cfdc-42e3-a943-3a86a0a6b515 -> Assistant -> 106fe138-27c6-4725-a628-17dd817481b0 -> Tool -> a2bb3d7f-bfdb-4ba5-aad8-e214580c0735 -> Assistant -> aaa27b35-554d-4d3a-b0b1-05e9b47e8bce -> User -> c27c1f1f-8661-42c3-9fc1-9fec3e63778a -> Assistant -> 942df40d-f0d2-4734-a40b-e2fe941ca83d -> Tool -> 7582187a-cfe1-4b09-9cad-c3eea53147fa -> Assistant -> aaa2dfaa-f25d-4390-bd5c-88400d309de0 -> User -> da348eb2-81de-4e5a-b41b-f9952559bf4a -> Assistant -> 275208a9-a3c4-4d6a-b8cd-db028d437455 -> Tool -> 0eb5d6f9-aad2-4cd1-b84f-12935b9eb055 -> Assistant -> aaa2cf19-8bcb-4615-9854-e7d1dec71204 -> User -> 30d0eb11-0fa3-43f2-af38-23473e7fb317 -> Assistant -> Context Management -> Streaming Output -> Command Queueing -> Timed Execution -> Error Handling -> Signal Handling -> Process Metadata -> Default Readers and Writers -> Data Format -> aaa26c5d-1140-4596-93aa-b2c6290ecbcb -> User -> ff45d771-ca0b-4405-8581-40e25368c0d3 -> Assistant -> 4c22c849-77fe-4278-98f0-794c92eddbae -> Tool
---
# Tool

```python
---------------------------------------------------------------------------
ProcessLookupError                        Traceback (most recent call last)
Cell In[5], line 98
     95     return stdout_data.decode(), stderr_data.decode(), exit_code
     97 # Run the test
---> 98 await test_enhanced_async_process()

Cell In[5], line 93, in test_enhanced_async_process()
     91     # Stream output (would be more useful in long-running processes)
     92     async for line in proc.stream_stdout():
---> 93         print(f"Streaming stdout: {line.decode().strip()}")
     95 return stdout_data.decode(), stderr_data.decode(), exit_code

Cell In[5], line 19, in AsyncProcess.__aexit__(self, exc_type, exc, tb)
     17 async def __aexit__(self, exc_type, exc, tb):
     18     if self.process:
---> 19         self.process.terminate()
     20         await self.process.wait()

File /usr/lib/python3.8/asyncio/subprocess.py:141, in Process.terminate(self)
    140 def terminate(self):
--> 141     self._transport.terminate()

File /usr/lib/python3.8/asyncio/base_subprocess.py:149, in BaseSubprocessTransport.terminate(self)
    148 def terminate(self):
--> 149     self._check_proc()
    150     self._proc.terminate()

File /usr/lib/python3.8/asyncio/base_subprocess.py:142, in BaseSubprocessTransport._check_proc(self)
    140 def _check_proc(self):
    141     if self._proc is None:
--> 142         raise ProcessLookupError()

ProcessLookupError: 

```

[child ⬇️](#075f585c-c0cb-4f56-a9b5-aab1418cd543)

---

(main branch ⎇)
###### 075f585c-c0cb-4f56-a9b5-aab1418cd543
[parent ⬆️](#4c22c849-77fe-4278-98f0-794c92eddbae)
