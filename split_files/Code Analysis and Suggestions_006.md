---
file: /home/pedro/Documents/chatgpt_export/Markdown/Code Analysis and Suggestions.md
heading_stack: <root> -> 9e26d6f4-d44b-48ce-804a-b866059e8a08 -> System -> 2688ae0b-3d9e-45f7-8b73-a565f3fdc93f -> System -> aaa2bac3-68ad-45e4-a1fd-a350837ca8d1 -> User
---
# User

Please analyze this code:

from __future__ import annotations

import inspect
import sys
import io
import logging

def patch_typing(verbose: bool=False, logger: logging.Logger|None=None) -> None:

    # Separate variable to please Pyright
    if logger is None:
        _logger = logging.getLogger("typing_patcher")
        _logger.setLevel(logging.INFO)
    else:
        _logger = logger

    if verbose:
        _logger.info("Patching `typing` to contain `typing_extension` members...")

    import typing
    import typing_extensions


    typing_members = {k: v for k, v in inspect.getmembers(typing) if not k.startswith("_")}
    ext_members = {
        k: v
        for k, v in inspect.getmembers(typing_extensions) if
        not k.startswith("_") and
        k not in typing_members and
        not inspect.ismodule(v)
    }
    
    for k, v in inspect.getmembers(typing_extensions):
        if k.startswith("_"):
            continue  # skip privates
        if k in typing_members:
            continue  # we already have this one
        if inspect.ismodule(v):
            continue  # these are internal usages (should've declared __all__!)

        if verbose:
            _logger.info(f"Adding `{k}` to the `typing` module")
        setattr(typing, k, v)

if __name__ == "__main__":
    # Test it out if it's being run directly
    patch_typing(verbose=True)

    from typing import ParamSpec, Callable, TYPE_CHECKING, TypeVar

    _P = ParamSpec("_P")

    NumT = TypeVar("NumT", int, float)

    def doubled(c: Callable[_P, NumT]) -> Callable[_P, NumT]:
        def wrapper(*args: _P.args, **kwargs: _P.kwargs) -> NumT:
            return 2 * c(*args, **kwargs)
            
        return wrapper

    @doubled
    def add(a: NumT, b: NumT) -> NumT:
        return a + b

    x = add(5, 2)
    print(f"doubled add(5, 2) -> {x}")

    if TYPE_CHECKING:
        reveal_type(x)        # information: Type of "x" is "int"
        reveal_type(add)      # information: Type of "add" is "(a: NumT@add, b: NumT@add) -> NumT@add"
        reveal_type(doubled)  # information: Type of "doubled" is "(c: (**_P@doubled) -> NumT@doubled) -> ((**_P@doubled) -> NumT@doubled)"

    # Pyright: 0 errors, 0 warnings, 3 informations


[child ⬇️](#f831b866-ab70-403a-9851-255413e1dcc2)

---

(main branch ⎇)
###### f831b866-ab70-403a-9851-255413e1dcc2
[parent ⬆️](#aaa2bac3-68ad-45e4-a1fd-a350837ca8d1)
