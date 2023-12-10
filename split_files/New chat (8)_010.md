---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (8).md
heading_stack: <root> -> 87bd7f6a-c34c-4e21-a681-520aea876871 -> System -> 0305e3b7-9645-4e79-89a2-794319c6d100 -> System -> aaa236d3-b162-4863-965c-406dd86ac031 -> User -> 6389456d-56b1-43ae-97a4-9af03a2416cc -> Assistant -> e3e20cb1-d7af-4b3a-8989-0f635e7b7b37 -> Assistant
---
# Assistant

```python
from typing import Any, Callable, Protocol, TypeVar, Union, AsyncGenerator, Generator, Awaitable
from functools import wraps
import asyncio
import inspect

F = TypeVar('F', bound=Callable[..., Any])

class SyncFn(Protocol):
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...

class AsyncFn(Protocol):
    async def __call__(self, *args: Any, **kwargs: Any) -> Any: ...

class SyncGen(Protocol):
    def __call__(self, *args: Any, **kwargs: Any) -> Generator[Any, None, None]: ...

class AsyncGen(Protocol):
    async def __call__(self, *args: Any, **kwargs: Any) -> AsyncGenerator[Any, None]: ...

FnType = Union[SyncFn, AsyncFn, SyncGen, AsyncGen]

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
            return other(intermediate)
        
        @wraps(other)
        async def composed_async_fn(*args, **kwargs):
            intermediate = await self.fn(*args, **kwargs)
            return await other(intermediate)

        @wraps(other)
        def composed_gen_fn(*args, **kwargs) -> Generator[Any, None, None]:
            for item in self.fn(*args, **kwargs):
                yield other(item)
                
        @wraps(other)
        async def composed_async_gen_fn(*args, **kwargs) -> AsyncGenerator[Any, None]:
            async for item in self.fn(*args, **kwargs):
                yield await other(item)

        if inspect.isasyncgenfunction(other):
            return Composed(composed_async_gen_fn)
        elif inspect.isgeneratorfunction(other):
            return Composed(composed_gen_fn)
        elif inspect.iscoroutinefunction(other):
            return Composed(composed_async_fn)
        else:
            return Composed(composed_fn)
    
    def __call__(self, *args, **kwargs) -> Any:
        if self.is_async:
            raise TypeError("This is an async function, use 'await'")
        elif self.is_gen:
            return self.fn(*args, **kwargs)
        elif self.is_async_gen:
            raise TypeError("This is an async generator function, use 'async for'")
        else:
            return self.fn(*args, **kwargs)
    
    async def __acall__(self, *args, **kwargs) -> Any:
        if self.is_async:
            return await self.fn(*args, **kwargs)
        elif self.is_gen:
            raise TypeError("This is a generator function, use 'for'")
        elif self.is_async_gen:
            return self.fn(*args, **kwargs)
        else:
            return self.fn(*args, **kwargs)
    
    def __aiter__(self):
        if self.is_async_gen:
            return self.fn().__aiter__()
        else:
            raise TypeError("This is not an async generator function")

    def __iter__(self):
        if self.is_gen:
            return self.fn().__iter__()
        else:
            raise TypeError("This is not a generator function")
```

[child ⬇️](#0f60f5d4-ccff-409d-a801-fe2e8e24b7e0)

---

(other branch ⎇)
###### 0f60f5d4-ccff-409d-a801-fe2e8e24b7e0
[parent ⬆️](#e3e20cb1-d7af-4b3a-8989-0f635e7b7b37)
