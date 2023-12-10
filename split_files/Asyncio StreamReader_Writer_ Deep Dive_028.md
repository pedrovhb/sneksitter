---
file: /home/pedro/Documents/chatgpt_export/Markdown/Asyncio StreamReader_Writer_ Deep Dive.md
heading_stack: <root> -> fcadc37a-73b3-4d5c-8df9-b161199195c8 -> System -> b74b0f9d-258d-4711-a53e-a6ef4f3e749e -> System -> aaa2d34c-19b8-4a73-87e5-e89cc52880f1 -> User -> e699cc32-2076-4b5d-98e8-d8c8d270498e -> Assistant -> asyncio StreamReader and StreamWriter: A Deep Dive -> StreamReader -> Basics -> Core Methods -> Use Case -> StreamWriter -> Basics -> Core Methods -> Use Case -> Combining StreamReader and StreamWriter -> Buffering and Flow Control -> Exception Handling -> Backpressure Handling -> Stream Adapters -> Conclusion -> aaa2cf71-b96b-4015-b8df-dadb1288a43a -> User -> 7f748aa6-27c6-4794-ad0d-049b6f2f97d5 -> Assistant -> Factors Affecting Overhead
---
#### Factors Affecting Overhead

1. **CPU Time**: Spawning a new process involves a series of system calls like `fork()` and `exec()`, which consume CPU cycles.
2. **Memory**: Each process has its own address space, stack, and heap, which consume RAM.
3. **I/O**: Reading the executable from disk and loading it into memory also involves I/O operations.
4. **Kernel Overhead**: The operating system kernel has to manage internal data structures for each process, such as Process Control Blocks (PCBs).
5. **Context Switching**: If the number of processes is high, the kernel has to spend more time switching between different processes, which adds to the overhead.

