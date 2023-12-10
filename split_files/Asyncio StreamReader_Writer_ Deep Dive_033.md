---
file: /home/pedro/Documents/chatgpt_export/Markdown/Asyncio StreamReader_Writer_ Deep Dive.md
heading_stack: <root> -> fcadc37a-73b3-4d5c-8df9-b161199195c8 -> System -> b74b0f9d-258d-4711-a53e-a6ef4f3e749e -> System -> aaa2d34c-19b8-4a73-87e5-e89cc52880f1 -> User -> e699cc32-2076-4b5d-98e8-d8c8d270498e -> Assistant -> asyncio StreamReader and StreamWriter: A Deep Dive -> StreamReader -> Basics -> Core Methods -> Use Case -> StreamWriter -> Basics -> Core Methods -> Use Case -> Combining StreamReader and StreamWriter -> Buffering and Flow Control -> Exception Handling -> Backpressure Handling -> Stream Adapters -> Conclusion -> aaa2cf71-b96b-4015-b8df-dadb1288a43a -> User -> 7f748aa6-27c6-4794-ad0d-049b6f2f97d5 -> Assistant -> Factors Affecting Overhead -> Quantitative Measures -> aaa28268-171d-4aa2-a801-59980b4a1c72 -> User -> f0baf8c5-cfdc-42e3-a943-3a86a0a6b515 -> Assistant
---
# Assistant

```python
import time
import subprocess

# Number of iterations to average out the measurement
iterations = 100

# Command to execute (using 'true' as a lightweight command that does nothing but exit successfully)
cmd = ["true"]

# Collect time measurements
elapsed_times = []

for _ in range(iterations):
    start_time = time.time()
    subprocess.run(cmd)
    end_time = time.time()
    elapsed_times.append(end_time - start_time)

# Calculate the average time taken to spawn a process
average_time = sum(elapsed_times) / iterations
average_time_ms = average_time * 1000  # convert to milliseconds

average_time_ms
```

[child ⬇️](#106fe138-27c6-4725-a628-17dd817481b0)

---

(main branch ⎇)
###### 106fe138-27c6-4725-a628-17dd817481b0
[parent ⬆️](#f0baf8c5-cfdc-42e3-a943-3a86a0a6b515)
