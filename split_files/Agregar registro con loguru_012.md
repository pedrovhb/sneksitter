---
file: /home/pedro/Documents/chatgpt_export/Markdown/Agregar registro con loguru.md
heading_stack: <root> -> bbc2eee3-d0e6-4dd5-a236-8aa929a8d323 -> System -> ce7fde3a-941f-4b7f-ac86-97a263e435dc -> System -> aaa26063-605a-4e6d-929e-590ee6e356d6 -> User -> f4b54abd-ea04-45dc-9235-d973f24c1a64 -> Assistant -> aaa2cf6b-49d5-489c-827b-3b1cdfb42d70 -> User -> 3cbcefc7-86a2-43c3-ab36-af1b0c4b80cc -> Assistant
---
# Assistant

To add comprehensive logging, I'll use the `loguru` library. Here's how the refactored code would look:

```python
from loguru import logger

class AsyncStreamer(BaseStreamer):
    def __init__(self, tokenizer):
        logger.info("AsyncStreamer initialized")
        self.tokenizer = tokenizer
        self.queue = asyncio.Queue()
        self.done = asyncio.Event()

    def put(self, value):
        logger.debug(f"Putting {value} in queue")
        self.queue.put_nowait(self.tokenizer.decode(value))

    def end(self):
        logger.debug("Setting done event")
        self.done.set()

    def __aiter__(self):
        return self

    async def __anext__(self):
        task_get, task_done = asyncio.create_task(
            self.queue.get()
        ), asyncio.create_task(self.done.wait())
        logger.debug("Waiting for either a queue item or a done event")
        
        done, pending = await asyncio.wait(
            {task_get, task_done}, return_when=asyncio.FIRST_COMPLETED
        )
        
        if task_get in done:
            logger.debug("Queue item retrieved")
            return task_get.result()
        else:
            logger.debug("Stopping async iteration")
            task_get.cancel()
            raise StopAsyncIteration


class AsyncTexter:
    def __init__(self, model, tokenizer):
        logger.info("AsyncTexter initialized")
        self.tokenizer = tokenizer
        self.model = model
        self._thread_gen = None

    def generate(
        self,
        prompt,
        max_length=250,
    ):
        logger.info(f"Generating text with prompt: {prompt} and max_length: {max_length}")
        streamer = AsyncStreamer(self.tokenizer)
        
        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            return_attention_mask=False,
        ).to("cuda")
        
        logger.debug("Creating thread for model generation")
        self._thread_gen = asyncio.create_task(
            asyncio.to_thread(
                self.model.generate,
                **inputs,
                max_length=max_length,
            )
        )
        return streamer


async def main(model, tokenizer):
    logger.info("Starting main coroutine")
    texter = AsyncTexter(model, tokenizer)
    async for text in texter.generate("Hello, my name is"):
        logger.info(f"Generated text: {text}")
```

Let me know if you'd like to dig deeper into any specific area.

[child ⬇️](#aaa22a4e-9be3-4101-83a6-e79c030b39b7)

---

(main branch ⎇)
###### aaa22a4e-9be3-4101-83a6-e79c030b39b7
[parent ⬆️](#3cbcefc7-86a2-43c3-ab36-af1b0c4b80cc)
