---
file: /home/pedro/Documents/chatgpt_export/Markdown/Asyncio StreamReader_Writer_ Deep Dive.md
heading_stack: <root> -> fcadc37a-73b3-4d5c-8df9-b161199195c8 -> System -> b74b0f9d-258d-4711-a53e-a6ef4f3e749e -> System -> aaa2d34c-19b8-4a73-87e5-e89cc52880f1 -> User -> e699cc32-2076-4b5d-98e8-d8c8d270498e -> Assistant -> asyncio StreamReader and StreamWriter: A Deep Dive -> StreamReader -> Basics -> Core Methods -> Use Case -> StreamWriter -> Basics -> Core Methods -> Use Case -> Combining StreamReader and StreamWriter -> Buffering and Flow Control -> Exception Handling
---
#### Exception Handling

Both classes are designed to be robust and handle exceptions gracefully. For instance, if you try to read after the stream has been closed, a default value is returned, indicating the end of the stream. Similarly, `StreamWriter` raises appropriate exceptions when you attempt to write to a closed stream.
