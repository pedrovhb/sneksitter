---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Async Code Review.md
heading_stack: <root> -> 22e9cf0b-43d0-4cba-b6dd-485e711d406b -> System -> 8c4249b6-2feb-4974-82e2-5202ef7ebb86 -> System -> aaa255dc-4cd2-4201-aa1b-3acbcd5264eb -> User -> 010bb377-54fe-4294-993d-db25e5599734 -> Assistant -> Main Components: -> Some Points to Consider: -> aaa2d4ed-07b8-4361-b256-cd31a20ad6aa -> User -> 92304192-39de-46c9-a2fc-b0c0599329f9 -> System -> a9ae2de4-9804-429a-8d65-f970d87d1ae4 -> Assistant -> aaa2df94-6e04-4e19-a4d7-023d418623b1 -> User -> 0ce78417-20a9-4e6e-adf2-455f05313870 -> Assistant -> aaa21f59-e6e0-44a7-886b-fb6c51ce0f15 -> User -> a31a0c13-f56b-49e9-b146-e58375d41b9b -> Assistant -> aaa2cbbd-f215-4b9b-98e3-e26e27b3992a -> User -> 9e13158c-ee20-49bf-9635-af5c23d44f10 -> Assistant -> aaa2ef44-b8b1-466c-84fe-cd64264b3165 -> User -> 8e17e4d2-49f9-4ff4-aaac-2cb095ccb613 -> Assistant
---
# Assistant

You're right; waiting on the same future that you're setting could lead to issues. It would be cleaner to separate out the futures used for "getting" from those used for "setting." I'll introduce a small data structure to manage the futures more cleanly.

Here's the updated code:

```python
from typing import List, AsyncIterator, Generic, TypeVar
import asyncio

_T_co = TypeVar('_T_co', covariant=True)

class Sentinel:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Sentinel, cls).__new__(cls)
        return cls._instance

END_OF_STREAM = Sentinel()

class FuturePair:
    def __init__(self):
        self.set_fut: asyncio.Future = asyncio.Future()
        self.get_fut: asyncio.Future = asyncio.Future()

class AsyncStream(Generic[_T_co]):
    def __init__(self, iterator: AsyncIterator[_T_co]):
        self.iterator = iterator
    
    async def __aiter__(self) -> AsyncIterator[_T_co]:
        return self.iterator

    @classmethod
    async def merge(cls, streams: List[AsyncStream[_T_co]]) -> AsyncStream[_T_co]:
        future_pairs: List[FuturePair] = [FuturePair() for _ in streams]

        async def _forward_to_output(stream: AsyncStream[_T_co], pair: FuturePair) -> None:
            async for item in stream:
                next_pair = FuturePair()
                pair.set_fut.set_result((next_pair, item))
                pair = await pair.get_fut
            pair.set_fut.set_result((None, END_OF_STREAM))

        tasks = [asyncio.create_task(_forward_to_output(stream, pair)) for stream, pair in zip(streams, future_pairs)]

        async def _merged_stream() -> AsyncIterator[_T_co]:
            pending_tasks = set(tasks)
            while pending_tasks:
                done, _ = await asyncio.wait(
                    [pair.get_fut for pair in future_pairs], return_when=asyncio.FIRST_COMPLETED
                )
                for pair in [future_pairs[i] for i, fut in enumerate(future_pairs) if fut.get_fut in done]:
                    next_pair, item = pair.set_fut.result()
                    pair.get_fut.set_result(None)  # Clear the "get" future for the next round
                    if next_pair is not None:
                        next_pair.get_fut.set_result(None)
                    if item is END_OF_STREAM:
                        pending_tasks.remove(tasks[future_pairs.index(pair)])
                    else:
                        yield item

        return AsyncStream(_merged_stream())
```

In this updated implementation, each stream has its own `FuturePair`, which includes a `set_fut` for setting the next value and a `get_fut` for waiting on it. This avoids any potential issues with waiting on and setting the same future.

---
