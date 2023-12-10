---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (1).md
heading_stack: <root> -> 18e042b6-0753-47b9-8b94-dbf396965d51 -> System -> 705df361-3567-44f4-ad9c-70bb5d82744c -> System -> aaa29996-ddf3-403a-a4bb-fdfc7ef52d1a -> User -> 29be782a-5014-4a86-af90-9005dfcedffd -> Assistant -> Naive Implementation -> LRU Cached Version -> 1b9602eb-4a57-4178-bdd7-e7b55fca4a3b -> Assistant -> 7a2ff30b-7f64-44c1-9cf3-ce1be5a8528d -> Tool -> da282554-170d-416f-9f9d-d980cbed2faa -> Assistant -> Tolerant LRU Cache Implementation -> b712a863-6a4b-4b23-85ee-109191da28fa -> Assistant -> 5663a5e3-9e34-4b5d-b20e-2a69ee6dcc7a -> Tool -> 0dfe1cb7-16b8-48fe-8058-9a3cd43dfeec -> Assistant -> Benchmarking
---
### Benchmarking

Now let's benchmark the three versions:

1. Naive implementation (`adjust_rgb`)
2. LRU cached version (`adjust_rgb_lru_cached`)
3. Tolerant LRU cached version (`adjust_rgb_tolerant_cached`)

We'll use Python's `timeit` module to measure the performance. First, let's create some random test data to use in the benchmark.

[child ⬇️](#6a015b36-32b5-407d-b23e-1ca689cf3200)

---

(main branch ⎇)
###### 6a015b36-32b5-407d-b23e-1ca689cf3200
[parent ⬆️](#0dfe1cb7-16b8-48fe-8058-9a3cd43dfeec)
