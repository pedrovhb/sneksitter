---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (8).md
heading_stack: <root> -> 87bd7f6a-c34c-4e21-a681-520aea876871 -> System -> 0305e3b7-9645-4e79-89a2-794319c6d100 -> System -> aaa236d3-b162-4863-965c-406dd86ac031 -> User -> 6389456d-56b1-43ae-97a4-9af03a2416cc -> Assistant -> e3e20cb1-d7af-4b3a-8989-0f635e7b7b37 -> Assistant -> 0f60f5d4-ccff-409d-a801-fe2e8e24b7e0 -> Tool -> 2dde9631-ce8a-470f-a73d-efdd18304420 -> Assistant -> efc03986-9e2b-44f4-b7a8-f1ea222b2fe6 -> Assistant
---
# Assistant

```python
import math

# Test with synchronous functions
sync_composed = Composed(math.sqrt) / int / str / (lambda s: s[::-1]) / int
print(sync_composed(256))  # Should return 41 (sqrt(256) -> 16.0 -> 16 -> '16' -> '61' -> 61)

# Test with async function
async def async_add_one(x):
    await asyncio.sleep(1)
    return x + 1

async_composed = Composed(async_add_one) / int / str / (lambda s: s[::-1]) / int

# Test it asynchronously
async def test_async_composed():
    result = await async_composed.__acall__(9)  # Should return 11 (9 + 1 -> 10 -> '10' -> '01' -> 1)
    print(result)

await test_async_composed()
```

[child ⬇️](#6ed08e43-230e-4b6e-a185-fa455f069e46)

---

(other branch ⎇)
###### 6ed08e43-230e-4b6e-a185-fa455f069e46
[parent ⬆️](#efc03986-9e2b-44f4-b7a8-f1ea222b2fe6)
