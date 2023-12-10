---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (1).md
heading_stack: <root> -> 18e042b6-0753-47b9-8b94-dbf396965d51 -> System -> 705df361-3567-44f4-ad9c-70bb5d82744c -> System -> aaa29996-ddf3-403a-a4bb-fdfc7ef52d1a -> User -> 29be782a-5014-4a86-af90-9005dfcedffd -> Assistant -> Naive Implementation -> LRU Cached Version -> 1b9602eb-4a57-4178-bdd7-e7b55fca4a3b -> Assistant -> 7a2ff30b-7f64-44c1-9cf3-ce1be5a8528d -> Tool -> da282554-170d-416f-9f9d-d980cbed2faa -> Assistant -> Tolerant LRU Cache Implementation -> b712a863-6a4b-4b23-85ee-109191da28fa -> Assistant -> 5663a5e3-9e34-4b5d-b20e-2a69ee6dcc7a -> Tool -> 0dfe1cb7-16b8-48fe-8058-9a3cd43dfeec -> Assistant -> Benchmarking -> 6a015b36-32b5-407d-b23e-1ca689cf3200 -> Assistant -> 84651923-f448-4370-8451-cabc45f4c360 -> Tool -> 6d250cf1-e160-4db9-a806-517164fd8aea -> Assistant -> 10182347-e97a-49d4-83de-865d8a7b8104 -> Assistant -> aaa2b100-8b2b-41ef-b5df-9c1650a616c3 -> User -> cadb7b51-0796-4d21-ad04-16485f480d89 -> Assistant
---
# Assistant

```python
import timeit

# Function to benchmark a given function with test data
def benchmark_func(func: Callable, test_data: list, num_runs: int = 1000) -> float:
    def wrapper():
        for data in test_data:
            func(*data)
    return timeit.timeit(wrapper, number=num_runs)

# Benchmark naive implementation
time_naive = benchmark_func(adjust_rgb, test_data)

# Benchmark LRU cached version
time_lru_cached = benchmark_func(adjust_rgb_lru_cached, test_data)

# Benchmark tolerant LRU cached version
time_tolerant_cached = benchmark_func(adjust_rgb_tolerant_cached, test_data)

time_naive, time_lru_cached, time_tolerant_cached
```

[child ⬇️](#f76e204c-48da-480e-b6a7-aea4f4479222)

---

(main branch ⎇)
###### f76e204c-48da-480e-b6a7-aea4f4479222
[parent ⬆️](#cadb7b51-0796-4d21-ad04-16485f480d89)
