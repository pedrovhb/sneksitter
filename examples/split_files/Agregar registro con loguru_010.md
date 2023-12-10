# User

Please add comprehensive logging at every step of the way with loguru:


class AsyncStreamer(BaseStreamer):
    def __init__(self, tokenizer):
        print("initialized")
        self.tokenizer = tokenizer
        self.queue = asyncio.Queue()
        self.done = asyncio.Event()

    def put(self, value):
        print(f"putting {value} in queue")
        self.queue.put_nowait(self.tokenizer.decode(value))

    def end(self):
        print("setting done")
        self.done.set()

    def __aiter__(self):
        return self

    async def __anext__(self):
        task_get, task_done = asyncio.create_task(
            self.queue.get()
        ), asyncio.create_task(self.done.wait())
        done, pending = await asyncio.wait(
            {task_get, task_done}, return_when=asyncio.FIRST_COMPLETED
        )
        if task_get in done:
            return task_get.result()
        else:
            task_get.cancel()
            raise StopAsyncIteration


class AsyncTexter:
    def __init__(self, model, tokenizer):
        self.tokenizer = tokenizer
        self.model = model
        self._thread_gen = None

    def generate(
        self,
        prompt,
        max_length=250,
    ):
        streamer = AsyncStreamer(self.tokenizer)
        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            return_attention_mask=False,
        ).to("cuda")
        
        self._thread_gen = asyncio.create_task(
            asyncio.to_thread(
                self.model.generate,
                **inputs,
                max_length=max_length,
            )
        )
        return streamer


async def main(model, tokenizer):
    texter = AsyncTexter(model, tokenizer)
    async for text in texter.generate("Hello, my name is"):
        print(text)


[child ⬇️](#3cbcefc7-86a2-43c3-ab36-af1b0c4b80cc)

---

(main branch ⎇)
###### 3cbcefc7-86a2-43c3-ab36-af1b0c4b80cc
[parent ⬆️](#aaa2cf6b-49d5-489c-827b-3b1cdfb42d70)
