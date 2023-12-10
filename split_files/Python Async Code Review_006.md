---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Async Code Review.md
heading_stack: <root> -> 22e9cf0b-43d0-4cba-b6dd-485e711d406b -> System -> 8c4249b6-2feb-4974-82e2-5202ef7ebb86 -> System -> aaa255dc-4cd2-4201-aa1b-3acbcd5264eb -> User
---
# User

Take a gander at this bad boy - 

from __future__ import annotations

import asyncio
import functools
import inspect
from typing import (
    Protocol,
    TypeVar,
    Iterable,
    AsyncIterable,
    AsyncIterator,
    Union,
    cast,
    TYPE_CHECKING,
    ParamSpec,
    Generic,
    Callable,
)

if not TYPE_CHECKING:

    def reveal_type(v: object) -> None:
        print(f"reveal_type: {type(v)}")


_T_co = TypeVar("_T_co", covariant=True)
_T_contra = TypeVar("_T_contra", contravariant=True)
_P = ParamSpec("_P")


_Acc = TypeVar("_Acc")


class SyncCallable(Protocol[_P, _T_co]):
    def __call__(self, *args: _P.args, **kwargs: _P.kwargs) -> _T_co:
        ...


class AsyncCallable(Protocol[_P, _T_co]):
    async def __call__(self, *args: _P.args, **kwargs: _P.kwargs) -> _T_co:
        ...


AnyIt = Union[Iterable[_T_co], AsyncIterable[_T_co]]
AnyCallable = Union[SyncCallable[_P, _T_co], AsyncCallable[_P, _T_co]]
_R_co = TypeVar("_R_co", covariant=True)


async def arange(*args: int, delay: float = 0) -> AsyncIterable[int]:
    for i in range(*args):
        yield i
        await asyncio.sleep(delay / 1000)


async def ensure_async_iterator(it: AnyIt[_T_co]) -> AsyncIterator[_T_co]:
    if isinstance(it, AsyncIterable):
        async for i in it:
            yield i
    elif isinstance(it, Iterable):
        for i in it:
            yield i
            await asyncio.sleep(0)
    else:
        raise TypeError(f"expected iterable or async iterable, got {type(it)}")


def ensure_async_callable(fn: AnyCallable[_P, _T_co]) -> AsyncCallable[_P, _T_co]:
    if inspect.iscoroutinefunction(fn):
        async_fn = cast(AsyncCallable[_P, _T_co], fn)
        return async_fn
    elif callable(fn):
        sync_fn = cast(SyncCallable[_P, _T_co], fn)

        async def wrapped_fn(*args: _P.args, **kwargs: _P.kwargs) -> _T_co:
            return sync_fn(*args, **kwargs)

        return wrapped_fn
    else:
        raise TypeError(f"expected some stuff man")


a1 = ensure_async_iterator(range(10))
a2 = ensure_async_iterator(arange(20))
reveal_type(a1)
reveal_type(a2)


async def my_sleep(delay: float) -> str:
    await asyncio.sleep(delay / 1000)
    return "ok"


def do_nothing(something: float) -> str:
    return "ok"


b1 = ensure_async_callable(my_sleep)
b2 = ensure_async_callable(do_nothing)

reveal_type(b1)
reveal_type(b2)


def async_stream(fn: Callable[_P, AnyIt[_T_co]]) -> Callable[_P, AsyncStream[_T_co]]:
    @functools.wraps(fn)
    def _wrapped(*args: _P.args, **kwargs: _P.kwargs) -> AsyncStream[_T_co]:
        return AsyncStream(fn(*args, **kwargs))

    return _wrapped


@async_stream
def my_stream(i: int) -> Iterable[int]:
    for j in range(i):
        yield j


class AsyncStream(Generic[_T_co], AsyncIterable[_T_co]):
    def __init__(self, it: AnyIt[_T_co]) -> None:
        self._it = ensure_async_iterator(it)

    def mapped(self, fn: AnyCallable[[_T_co], _T_contra]) -> AsyncStream[_T_contra]:
        async_fn = ensure_async_callable(fn)

        async def _mapped() -> AsyncIterator[_T_contra]:
            async for item in self._it:
                yield await async_fn(item)

        return AsyncStream(_mapped())

    def flat_mapped(
        self, fn: AnyCallable[[_T_co], AnyIt[_T_contra]]
    ) -> AsyncStream[_T_contra]:
        async_fn = ensure_async_callable(fn)

        async def _flat_mapped() -> AsyncIterator[_T_contra]:
            async for item in self._it:
                iterator = await async_fn(item)
                reveal_type(iterator)
                async_iter = ensure_async_iterator(iterator)
                async for sub_item in async_iter:
                    yield sub_item

        return AsyncStream(_flat_mapped())

    def filtered(self, fn: AnyCallable[[_T_co], bool]) -> AsyncStream[_T_co]:
        async_fn = ensure_async_callable(fn)

        async def _filtered() -> AsyncIterator[_T_co]:
            async for item in self._it:
                if await async_fn(item):
                    yield item

        return AsyncStream(_filtered())

    def flatten(self: AsyncStream[Iterable[_R_co]]) -> AsyncStream[_R_co]:
        async def _flatten() -> AsyncIterator[_R_co]:
            async for item in self._it:
                is_async_iter = inspect.isasyncgen(item)
                is_iter = isinstance(item, Iterable)
                if is_async_iter or is_iter:
                    async for sub_item in ensure_async_iterator(item):
                        yield sub_item
                else:
                    yield item

        return AsyncStream(_flatten())

    __truediv__ = mapped
    __mod__ = filtered
    __floordiv__ = flat_mapped
    __pos__ = flatten

    async def reduce(
        self,
        fn: AnyCallable[[_Acc, _T_co], _Acc],
        initial_value: _Acc,
    ) -> _Acc:
        async_fn = ensure_async_callable(fn)
        acc = initial_value
        async for item in self._it:
            acc = await async_fn(acc, item)
        return acc

    def __aiter__(self) -> AsyncStream[_T_co]:
        return self

    async def __anext__(self) -> _T_co:
        return await self._it.__anext__()


async def main() -> None:
    async for i in arange(10):
        print(i * 2)
        reveal_type(i)
    c1 = await b1(2.0)
    c2 = await b2(2.0)
    reveal_type(c1)
    reveal_type(c2)

    def halve(i: float) -> float:
        return i / 2

    d1 = ensure_async_callable(halve)
    reveal_type(d1)
    v: float = 2.0
    d2 = await d1(v)
    reveal_type(d2)

    d3 = await d1(4)
    reveal_type(d3)

    async for i in AsyncStream(range(10)).mapped(str).filtered(
        lambda x: x in "246"
    ) / ord % (lambda i: i > 50):
        print(i)
        reveal_type(i)

    def add(a, b):
        return a + b

    result = await AsyncStream(range(10)).reduce(add, 0)
    reveal_type(result)
    print(f"{result=}")

    s = AsyncStream(range(10))
    i = s / str / ord
    n = await i.reduce(add, 0)
    reveal_type(n)
    print(f"{n=}")

    cascade = AsyncStream(range(10))
    cascade = cascade / str % (lambda x: x in "246") / ord % (lambda x: x > 50)

    async for ii in cascade:
        print(ii)
        reveal_type(ii)

    # Demonstrate flatmap
    async for i in AsyncStream(range(10)) / (lambda x: range(x)):
        print(i)
        reveal_type(i)

    async for i in +(AsyncStream(range(10)) / (lambda x: str(x))):
        print(i)
        reveal_type(i)

    tt: list[tuple[int, str]] = [(1, "2"), (3, "4"), (5, "6")]
    async for i in +AsyncStream(tt):
        print(i)
        reveal_type(i)


if __name__ == "__main__":
    print("starting")
    asyncio.run(main())


[child ⬇️](#010bb377-54fe-4294-993d-db25e5599734)

---

(main branch ⎇)
###### 010bb377-54fe-4294-993d-db25e5599734
[parent ⬆️](#aaa255dc-4cd2-4201-aa1b-3acbcd5264eb)
