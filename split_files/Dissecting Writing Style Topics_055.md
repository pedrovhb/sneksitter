---
file: /home/pedro/Documents/chatgpt_export/Markdown/Dissecting Writing Style Topics.md
heading_stack: <root> -> c091f035-c809-4c99-999e-3c9f1a0bca92 -> System -> 4e26b9e5-7363-4eac-9fb3-e6fd55f02123 -> System -> aaa25e2d-f881-450a-9ac5-02b072f07858 -> User -> 67069467-5e90-4551-8707-782ef7e5155b -> Assistant -> Writing Style Analysis -> Ten Topics with Heading Outlines for Similar Dissection -> aaa2aaf6-a3f4-40d3-9cb3-e2dd0330500a -> User -> c9eb3cf7-892d-4f42-832f-a784e780d05e -> Assistant -> Comprehensive Analysis of the Writing Style -> 10 Topics with Outlines for Headings -> 1. Understanding Python's Decorators -> aaa23978-80f1-4fee-88bf-334965678a1e -> User -> 758e9cec-bea5-4f76-ac6c-be6bb51a482c -> Assistant -> Comprehensive Analysis of the Writing Style of the Post -> aaa2bfb0-6fa7-4832-97b1-8cb6f06ff066 -> User -> 06bf9663-7e46-478f-833f-87d30d37fec4 -> Assistant -> Introduction: The Asynchronous and Synchronous Dilemma -> Part 1: Understanding Synchronous Iterators -> Part 2: Delving into Asynchronous Iterators -> Part 3: Comparative Analysis -> Conclusion: The Balanced Iterator Diet -> Additional Resources -> aaa2d2ee-f38f-42b6-8cfc-9545ba1da3b7 -> User -> d74e385a-6570-42f7-9532-3776232cad7e -> Assistant -> Part 1: Understanding Synchronous Iterators -> What Are Synchronous Iterators? -> The `__iter__` and `__next__` Magic Methods -> Use Cases for Synchronous Iterators -> aaa21210-e59a-48ee-aec2-c51a1608a090 -> User -> 5f234b5f-5594-4f13-bbdc-7a00a003bfaa -> Assistant -> Part 2: Understanding Asynchronous Iterators -> What Are Asynchronous Iterators? -> The `__aiter__` and `__anext__` Magic Methods -> Use Cases for Asynchronous Iterators -> aaa2799c-195d-4cb8-bb1f-c8d01a334585 -> User -> 9513df32-d0bc-4b40-bc53-a5c3f155cef8 -> Assistant -> Part 2: Understanding Asynchronous Iterators -> What Are Asynchronous Iterators? -> The `__aiter__` and `__anext__` Magic Methods
---
### The `__aiter__` and `__anext__` Magic Methods

We'll enrich this section by creating an asynchronous iterator that not only returns a sequence of numbers but also logs the time at which each number is fetched. This will demonstrate how the iterator works under the hood.

```python
import datetime

class MyAsyncIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.index < len(self.numbers):
            result = self.numbers[self.index]
            self.index += 1
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Fetched {result} at {timestamp}")
            await asyncio.sleep(1)  # Simulate network delay
            return result
        else:
            raise StopAsyncIteration

# Usage
async def main():
    async for i in MyAsyncIterator([1, 2, 3]):
        print(f"Processed: {i}")

# Run the coroutine
asyncio.run(main())
```
