---
file: /home/pedro/Documents/chatgpt_export/Markdown/Asyncio StreamReader_Writer_ Deep Dive.md
heading_stack: <root> -> fcadc37a-73b3-4d5c-8df9-b161199195c8 -> System -> b74b0f9d-258d-4711-a53e-a6ef4f3e749e -> System -> aaa2d34c-19b8-4a73-87e5-e89cc52880f1 -> User -> e699cc32-2076-4b5d-98e8-d8c8d270498e -> Assistant -> asyncio StreamReader and StreamWriter: A Deep Dive -> StreamReader -> Basics -> Core Methods -> Use Case -> StreamWriter
---
#### StreamWriter

##### Basics

The `StreamWriter` class is the counterpart to `StreamReader` and is used for writing data to a stream. Like `StreamReader`, it is also typically used in the context of network programming.

##### Core Methods

- `write(data: bytes)`: Writes `data` to the stream.
- `writelines(data: List[bytes])`: Writes a list of bytes to the stream.
- `drain()`: Waits until the write buffer is completely flushed. This is often called after `write()` to ensure data is sent.
- `close()`: Closes the stream.

##### Use Case

Writing to a TCP socket might look like:

```python
reader, writer = await asyncio.open_connection('localhost', 8080)
writer.write(b'Hello, world!')
await writer.drain()
writer.close()
```

