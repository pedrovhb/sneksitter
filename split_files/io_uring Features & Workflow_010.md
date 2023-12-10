---
file: /home/pedro/Documents/chatgpt_export/Markdown/io_uring Features & Workflow.md
heading_stack: <root> -> f013dc86-2d37-4c23-bf27-327e4dcc81ea -> System -> 3aad8956-6efe-4d23-937d-928e45dec0e2 -> System -> aaa23db3-fa39-411e-a77c-61fc74f888be -> User -> 03e7a418-e0e6-49a3-87ca-0b973cd25839 -> Assistant -> io_uring Features and Use Cases -> Features
---
#### Features

1. **Asynchronous I/O**: io_uring provides a way to perform I/O operations asynchronously, improving throughput and reducing latency.
  
2. **Batch Submissions**: Multiple I/O requests can be submitted in a single system call, reducing syscall overhead.
  
3. **Buffer Management**: io_uring allows pre-registration of buffers, which can improve performance by reducing memory copies.
  
4. **Polling and Event Notification**: It supports event-driven programming, allowing applications to wait for multiple events efficiently.
  
5. **Thread Pooling**: io_uring can offload work to kernel threads, making it suitable for CPU-bound tasks as well.
  
6. **Timeouts**: Native support for timeouts on operations.
  
7. **Linked Operations**: Ability to chain multiple operations together to execute in a specific order.

