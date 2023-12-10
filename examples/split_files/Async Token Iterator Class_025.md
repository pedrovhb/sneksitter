# User

Does this make sense?

from typing import Optional
from asyncio import Queue, get_event_loop
import asyncio

class AsyncTextIteratorStreamer(TextIteratorStreamer):
    def __init__(
        self, 
        tokenizer: "AutoTokenizer", 
        skip_prompt: bool = False, 
        timeout: Optional[float] = None, 
        **decode_kwargs
    ):
        super().__init__(tokenizer, skip_prompt, timeout, **decode_kwargs)
        self.text_queue = Queue()
        self.stop_signal = object()
        self.timeout = timeout
        self._generate_task = None

    def on_finalized_text(self, text: str, stream_end: bool = False):
        self.text_queue.put_nowait(text)
        if stream_end:
            self.text_queue.put_nowait(self.stop_signal)

    def run_generate(self, model, **kwargs):
        self._generate_task = asyncio.create_task(asyncio.to_thread(model.generate, **kwargs))

    def __aiter__(self):
        return self

    async def __anext__(self):
        value = await self.text_queue.get()
        if value == self.stop_signal:
            raise StopAsyncIteration
        return value


[child ⬇️](#ad163769-0950-42ae-b280-25cfccfbee48)

---

(other branch ⎇)
###### ad163769-0950-42ae-b280-25cfccfbee48
[parent ⬆️](#aaa2f2fa-1b15-4b37-8e32-688308044077)
