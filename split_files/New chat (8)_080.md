---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (8).md
heading_stack: <root> -> 87bd7f6a-c34c-4e21-a681-520aea876871 -> System -> 0305e3b7-9645-4e79-89a2-794319c6d100 -> System -> aaa236d3-b162-4863-965c-406dd86ac031 -> User -> 6389456d-56b1-43ae-97a4-9af03a2416cc -> Assistant -> e3e20cb1-d7af-4b3a-8989-0f635e7b7b37 -> Assistant -> 0f60f5d4-ccff-409d-a801-fe2e8e24b7e0 -> Tool -> 2dde9631-ce8a-470f-a73d-efdd18304420 -> Assistant -> efc03986-9e2b-44f4-b7a8-f1ea222b2fe6 -> Assistant -> 6ed08e43-230e-4b6e-a185-fa455f069e46 -> Tool -> b8da2c4b-9db2-47d7-a2af-389be4befc5f -> Assistant -> db2e1dd1-0795-480b-bc14-771d0eb39e4d -> Assistant -> e7105360-42e1-44dc-b634-fe0c00e4e999 -> Tool -> ca3c2937-19b7-4c14-9f94-a96c4aa48bf4 -> Assistant -> aaa241ef-101a-4eeb-93d2-e8d8919d06d9 -> User -> 0d4987c7-80b3-4264-a7cb-373f269f73d6 -> Assistant -> aaa2d51e-8b35-443b-8c51-50d3a8740574 -> User -> 4b0ff9a6-0c97-4d93-b7b8-d64c70c39fe0 -> Assistant -> aaa29522-caba-4582-81f4-fa790988a5cb -> User -> 2671227c-f5b3-4e6a-8bc8-cf8625b9df85 -> Assistant -> 0378287d-290e-4e7d-b03a-e96ab29bc45d -> Tool -> 8be38330-dba2-463c-acb5-18b403657055 -> Assistant -> c66b0691-c55b-4e68-96b1-91f3dc82f4b7 -> Assistant -> a3e0a4c8-fc88-4485-9059-7f406744f6b4 -> Tool -> 419e449b-8c14-40cc-a0c1-b3e7c21548f0 -> Assistant -> 736f7993-431a-4b09-ac29-e009d83997db -> Assistant -> aaa2ce72-49ee-49cc-8893-081472477efe -> User -> f6a699fc-9589-496c-bb9d-98b527929107 -> Assistant -> 589de901-2a5c-4250-85b4-341a154c4e14 -> Tool -> e56f4805-ab35-4bb2-9722-f0eec9acaf00 -> Assistant -> aaa22608-4043-42da-9c29-4a1a3e230baa -> User -> c8bd61ab-d7b3-4ea0-8ed8-a46f94890ef6 -> Assistant -> 159991f9-95da-4347-83e1-7b99538798c7 -> Tool -> 84a3281c-d2e7-4cab-b27c-9806745c1e1a -> Assistant -> aaa2be14-d179-458d-b54e-7c33eb48609e -> User -> 62b6f78a-e207-4caf-acf5-bc872a343ea3 -> Assistant -> 4fb74221-c79f-4794-bd21-74a14a2868bd -> Tool -> ebbc3941-713f-4615-9515-556f91842fda -> Assistant -> 19f6532d-da06-496e-92e8-c7cf8fcf7cf8 -> Assistant -> aaa20df5-4e26-41ea-a5d3-30d3962ad2ea -> User -> 6b0f7f5f-81a2-4a4b-b055-c61966bb7f2f -> Assistant
---
# Assistant

```python
# Modify the FuncWrapper to handle already wrapped objects in __new__
class FuncWrapper:
    def __new__(cls, func: Union[AsyncFunction, AsyncIterable]) -> 'FuncWrapper':
        if isinstance(func, FuncWrapper):
            return func
        return super(FuncWrapper, cls).__new__(cls)

    def __init__(self, func: Union[AsyncFunction, AsyncIterable]) -> None:
        self.func = func

    async def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return await self.func(*args, **kwargs)

    def _compose(self, other: Union[AsyncFunction, 'FuncWrapper'], order: str) -> 'FuncWrapper':
        other_func = other.func if isinstance(other, FuncWrapper) else other

        async def composed(*args: Any, **kwargs: Any) -> Any:
            if order == 'lr':  # Left to Right: f >> g
                return await other_func(await self.func(*args, **kwargs))
            else:  # Right to Left: g << f
                return await self.func(await other_func(*args, **kwargs))
        
        return FuncWrapper(composed)

    def __rshift__(self, other: Union[AsyncFunction, 'FuncWrapper']) -> 'FuncWrapper':
        return self._compose(other, 'lr')

    def __lshift__(self, other: Union[AsyncFunction, 'FuncWrapper']) -> 'FuncWrapper':
        return self._compose(other, 'rl')

    def __rrshift__(self, other: Union[AsyncFunction, 'FuncWrapper']) -> 'FuncWrapper':
        return FuncWrapper(other)._compose(self, 'lr')

    def __rlshift__(self, other: Union[AsyncFunction, 'FuncWrapper']) -> 'FuncWrapper':
        return FuncWrapper(other)._compose(self, 'rl')

# Wrap the functions again
f_wrap = FuncWrapper(f)
g_wrap = FuncWrapper(g)

# Compose the functions again
h1_wrap = f_wrap >> g_wrap  # Should be equivalent to g(f(x))
h2_wrap = g_wrap << f_wrap  # Should be equivalent to f(g(x))

# Run the test again, but this time calling the composed functions directly
assert await (f_wrap >> g_wrap)(1) == 4  # (1 + 1) * 2 = 4
assert await (g_wrap << f_wrap)(1) == 3  # (1 * 2) + 1 = 3
```

[child ⬇️](#a23783ae-2c26-493b-8b99-7d5f120745b8)

---

(main branch ⎇)
###### a23783ae-2c26-493b-8b99-7d5f120745b8
[parent ⬆️](#6b0f7f5f-81a2-4a4b-b055-c61966bb7f2f)