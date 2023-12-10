---
file: /home/pedro/Documents/chatgpt_export/Markdown/Asyncio StreamReader_Writer_ Deep Dive.md
heading_stack: <root> -> fcadc37a-73b3-4d5c-8df9-b161199195c8 -> System -> b74b0f9d-258d-4711-a53e-a6ef4f3e749e -> System -> aaa2d34c-19b8-4a73-87e5-e89cc52880f1 -> User -> e699cc32-2076-4b5d-98e8-d8c8d270498e -> Assistant -> asyncio StreamReader and StreamWriter: A Deep Dive -> StreamReader
---
#### StreamReader

##### Basics

The `StreamReader` class is used for reading data from a stream, typically a network connection. It provides various methods for reading different types of data, such as bytes, lines, or specified lengths of data.

##### Core Methods

- `read(n: int = -1)`: Reads up to `n` bytes from the stream. If `n` is omitted or set to `-1`, it reads until EOF.
- `readline()`: Reads a line from the stream, where a line is a sequence of bytes ending with `\n`.
- `readexactly(n: int)`: Reads exactly `n` bytes from the stream, raises an `IncompleteReadError` if the stream closes before that.
- `readuntil(separator: bytes = b'\n')`: Reads data from the stream until the `separator` is found.

##### Use Case

Reading from a TCP socket can be as simple as:

```python
reader, writer = await asyncio.open_connection('localhost', 8080)
data = await reader.read(100)
```

