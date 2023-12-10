---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (8).md
heading_stack: <root> -> 87bd7f6a-c34c-4e21-a681-520aea876871 -> System -> 0305e3b7-9645-4e79-89a2-794319c6d100 -> System -> aaa236d3-b162-4863-965c-406dd86ac031 -> User -> 6389456d-56b1-43ae-97a4-9af03a2416cc -> Assistant -> e3e20cb1-d7af-4b3a-8989-0f635e7b7b37 -> Assistant -> 0f60f5d4-ccff-409d-a801-fe2e8e24b7e0 -> Tool -> 2dde9631-ce8a-470f-a73d-efdd18304420 -> Assistant -> efc03986-9e2b-44f4-b7a8-f1ea222b2fe6 -> Assistant -> 6ed08e43-230e-4b6e-a185-fa455f069e46 -> Tool -> b8da2c4b-9db2-47d7-a2af-389be4befc5f -> Assistant -> db2e1dd1-0795-480b-bc14-771d0eb39e4d -> Assistant
---
# Assistant

```python
class Composed:
    def __init__(self, fn: FnType):
        self.fn = fn
        self.is_async = inspect.iscoroutinefunction(fn)
        self.is_gen = inspect.isgeneratorfunction(fn)
        self.is_async_gen = inspect.isasyncgenfunction(fn)
    
    def __truediv__(self, other: FnType) -> 'Composed':
        @wraps(other)
        def composed_fn(*args, **kwargs):
            intermediate = self.fn(*args, **kwargs)
            if inspect.iscoroutine(intermediate):
                raise TypeError("This is an async function, use 'await'")
            return other(intermediate)
        
        @wraps(other)
        async def composed_async_fn(*args, **kwargs):
            intermediate = await self.fn(*args, **kwargs) if self.is_async else self.fn(*args, **kwargs)
            if inspect.iscoroutinefunction(other):
                return await other(intermediate)
            else:
                return other(intermediate)

        @wraps(other)
        def composed_gen_fn(*args, **kwargs) -> Generator[Any, None, None]:
            for item in self.fn(*args, **kwargs):
                yield other(item)
                
        @wraps(other)
        async def composed_async_gen_fn(*args, **kwargs) -> AsyncGenerator[Any, None]:
            async for item in self.fn(*args, **kwargs):
                yield await other(item) if inspect.iscoroutinefunction(other) else other(item)

        if inspect.isasyncgenfunction(other):
            return Composed(composed_async_gen_fn)
        elif inspect.isgeneratorfunction(other):
            return Composed(composed_gen_fn)
        elif inspect.iscoroutinefunction(other):
            return Composed(composed_async_fn)
        else:
            return Composed(composed_fn)
    
    # ... (Rest of the methods are unchanged)

# Re-test with async function
async_composed = Composed(async_add_one) / int / str / (lambda s: s[::-1]) / int

async def test_async_composed():
    result = await async_composed.__acall__(9)  # Should return 11 (9 + 1 -> 10 -> '10' -> '01' -> 1)
    print(result)

await test_async_composed()
```

[child ⬇️](#e7105360-42e1-44dc-b634-fe0c00e4e999)

---

(other branch ⎇)
###### e7105360-42e1-44dc-b634-fe0c00e4e999
[parent ⬆️](#db2e1dd1-0795-480b-bc14-771d0eb39e4d)
