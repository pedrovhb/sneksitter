---
file: /home/pedro/Documents/chatgpt_export/Markdown/Agregar registro con loguru.md
heading_stack: <root> -> bbc2eee3-d0e6-4dd5-a236-8aa929a8d323 -> System -> ce7fde3a-941f-4b7f-ac86-97a263e435dc -> System -> aaa26063-605a-4e6d-929e-590ee6e356d6 -> User
---
# User

Please add comprehensive logging at every step of the way with loguru:

from transformers.generation.streamers import BaseStreamer


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



[child ⬇️](#f4b54abd-ea04-45dc-9235-d973f24c1a64)

---

(other branch ⎇)
###### f4b54abd-ea04-45dc-9235-d973f24c1a64
[parent ⬆️](#aaa26063-605a-4e6d-929e-590ee6e356d6)
