# User

Does this make sense?



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
        task_get, task_done = asyncio.create_task(self.queue.get()), asyncio.create_task(self.done.wait())
        done, pending = await asyncio.wait({task_get, task_done}, return_when=asyncio.FIRST_COMPLETED)
        if task_get in done:
            return task_get.result()
        else:
            task_get.cancel()
            raise StopAsyncIteration


[child ⬇️](#62c86447-2186-44a0-95f6-028b2302d815)

---

(main branch ⎇)
###### 62c86447-2186-44a0-95f6-028b2302d815
[parent ⬆️](#aaa201d5-91c3-420f-8195-aaab4651bde7)
