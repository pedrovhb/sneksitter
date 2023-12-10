---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (1).md
heading_stack: <root> -> 18e042b6-0753-47b9-8b94-dbf396965d51 -> System -> 705df361-3567-44f4-ad9c-70bb5d82744c -> System -> aaa29996-ddf3-403a-a4bb-fdfc7ef52d1a -> User -> 29be782a-5014-4a86-af90-9005dfcedffd -> Assistant -> Naive Implementation -> LRU Cached Version -> 1b9602eb-4a57-4178-bdd7-e7b55fca4a3b -> Assistant -> 7a2ff30b-7f64-44c1-9cf3-ce1be5a8528d -> Tool -> da282554-170d-416f-9f9d-d980cbed2faa -> Assistant
---
# Assistant

The LRU cached version `adjust_rgb_lru_cached` is implemented using Python's built-in `lru_cache`. Next, we'll implement a custom version of `lru_cache` that is tolerant to floating-point variations.

### Tolerant LRU Cache Implementation

We'll create a custom decorator that rounds the floating-point numbers to a specified number of decimal places before caching. This will provide a level of tolerance to the cache.

Let's go ahead and implement this.

[child ⬇️](#b712a863-6a4b-4b23-85ee-109191da28fa)

---

(main branch ⎇)
###### b712a863-6a4b-4b23-85ee-109191da28fa
[parent ⬆️](#da282554-170d-416f-9f9d-d980cbed2faa)
