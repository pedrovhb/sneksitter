---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Async Code Review.md
heading_stack: <root> -> 22e9cf0b-43d0-4cba-b6dd-485e711d406b -> System -> 8c4249b6-2feb-4974-82e2-5202ef7ebb86 -> System -> aaa255dc-4cd2-4201-aa1b-3acbcd5264eb -> User -> 010bb377-54fe-4294-993d-db25e5599734 -> Assistant -> Main Components: -> Some Points to Consider: -> aaa2d4ed-07b8-4361-b256-cd31a20ad6aa -> User -> 92304192-39de-46c9-a2fc-b0c0599329f9 -> System -> a9ae2de4-9804-429a-8d65-f970d87d1ae4 -> Assistant -> aaa2df94-6e04-4e19-a4d7-023d418623b1 -> User -> 0ce78417-20a9-4e6e-adf2-455f05313870 -> Assistant -> aaa21f59-e6e0-44a7-886b-fb6c51ce0f15 -> User -> a31a0c13-f56b-49e9-b146-e58375d41b9b -> Assistant
---
# Assistant

Certainly, you can achieve that by using low-level synchronization primitives like `asyncio.Future`. Here's an implementation that will merge multiple `AsyncStream`s and complete when all streams are exhausted:

```python
from typing import List, Optional
import asyncio

class AsyncStream(Generic[_T_co], AsyncIterable[_T_co]):
    # ... existing code ...

    @classmethod
    async def merge(cls, streams: List[AsyncStream[_T_co]]) -> AsyncStream[_T_co]:
        out_futures: List[asyncio.Future[Optional[_T_co]]] = [asyncio.Future() for _ in streams]

        async def _forward_to_output(stream: AsyncStream[_T_co], fut: asyncio.Future[Optional[_T_co]]) -> None:
            async for item in stream:
                temp_fut = asyncio.Future()
                fut.set_result((temp_fut, item))
                fut = await temp_fut
            fut.set_result(None)

        tasks = [asyncio.create_task(_forward_to_output(stream, fut)) for stream, fut in zip(streams, out_futures)]

        async def _merged_stream() -> AsyncIterator[_T_co]:
            pending_tasks = set(tasks)
            while pending_tasks:
                done, _ = await asyncio.wait(
                    out_futures, return_when=asyncio.FIRST_COMPLETED
                )
                for fut in done:
                    next_fut, item = fut.result()
                    if item is not None:
                        yield item
                        fut.clear()
                        next_fut.set_result(None
```

[child ⬇️](#aaa2cbbd-f215-4b9b-98e3-e26e27b3992a)

---

(main branch ⎇)
###### aaa2cbbd-f215-4b9b-98e3-e26e27b3992a
[parent ⬆️](#a31a0c13-f56b-49e9-b146-e58375d41b9b)
