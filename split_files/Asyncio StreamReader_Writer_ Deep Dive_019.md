---
file: /home/pedro/Documents/chatgpt_export/Markdown/Asyncio StreamReader_Writer_ Deep Dive.md
heading_stack: <root> -> fcadc37a-73b3-4d5c-8df9-b161199195c8 -> System -> b74b0f9d-258d-4711-a53e-a6ef4f3e749e -> System -> aaa2d34c-19b8-4a73-87e5-e89cc52880f1 -> User -> e699cc32-2076-4b5d-98e8-d8c8d270498e -> Assistant -> asyncio StreamReader and StreamWriter: A Deep Dive -> StreamReader -> Basics -> Core Methods -> Use Case -> StreamWriter -> Basics -> Core Methods -> Use Case -> Combining StreamReader and StreamWriter -> Buffering and Flow Control
---
#### Buffering and Flow Control

Both `StreamReader` and `StreamWriter` handle buffering internally. `StreamReader` will keep an internal buffer of incoming data, while `StreamWriter` maintains an output buffer for data waiting to be written. The `drain()` method in `StreamWriter` allows you to handle flow control by waiting until the write buffer is flushed.

