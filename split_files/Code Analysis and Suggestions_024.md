---
file: /home/pedro/Documents/chatgpt_export/Markdown/Code Analysis and Suggestions.md
heading_stack: <root> -> 9e26d6f4-d44b-48ce-804a-b866059e8a08 -> System -> 2688ae0b-3d9e-45f7-8b73-a565f3fdc93f -> System -> aaa2bac3-68ad-45e4-a1fd-a350837ca8d1 -> User -> f831b866-ab70-403a-9851-255413e1dcc2 -> Assistant -> patch_typing Function -> Test Code -> Observations -> Suggestions for Improvement -> aaa292b7-5873-4fdd-acd7-3720ed81585a -> User -> 6e85476a-bbc8-4290-8a85-b381d5a4438e -> Assistant -> ad4cc9ce-a359-4b07-b521-9d0ada5a8f3f -> Tool -> 6825bd3f-20d0-48dd-a208-3c83401997c3 -> Assistant -> aaa27443-b7ec-476a-ad99-a9dce5cbf447 -> User -> ac2802d2-4c64-4077-bf8b-6faa64e9fbfb -> Assistant
---
# Assistant

```python
# Importing required modules
from __future__ import annotations
import inspect
import sys
import io
import logging
from typing import Any

def patch_typing(verbose: bool = False, logger: logging.Logger | None = None) -> None:
    """Patch the `typing` module to include members from `typing_extensions`."""

    # Initialize logger if not provided
    if logger is None:
        logger = logging.getLogger("typing_patcher")
        logger.setLevel(logging.INFO)

    # Log if verbose mode is enabled
    if verbose:
        logger.info("Patching `typing` to contain `typing_extensions` members...")

    # Import modules
    import typing
    import typing_extensions

    # Get existing members in `typing` module
    existing_typing_members = {k: v for k, v in inspect.getmembers(typing) if not k.startswith("_")}

    # Loop to add missing members from `typing_extensions` to `typing`
    for k, v in inspect.getmembers(typing_extensions):
        # Skip private members and modules
        if k.startswith("_") or inspect.ismodule(v):
            continue

        # Skip if already exists in `typing`
        if k in existing_typing_members:
            continue

        # Log the addition if verbose is True
        if verbose:
            logger.info(f"Adding `{k}` to the `typing` module")

        # Add the member to `typing`
        setattr(typing, k, v)

# Test the function
if __name__ == "__main__":
    # Setup logging
    logging.basicConfig(level=logging.INFO)

    # Test the patching function
    patch_typing(verbose=True)

    # Import types and define functions to test if patching worked
    from typing import ParamSpec, Callable, TYPE_CHECKING, TypeVar

    _P = ParamSpec("_P")
    NumT = TypeVar("NumT", int, float)

    def doubled(c: Callable[_P, NumT]) -> Callable[_P, NumT]:
        """Doubles the output of the decorated function."""

        def wrapper(*args: _P.args, **kwargs: _P.kwargs) -> NumT:
            return 2 * c(*args, **kwargs)

        return wrapper

    @doubled
    def add(a: NumT, b: NumT) -> NumT:
        """Adds two numbers."""
        return a + b

    x = add(5, 2)
    print(f"doubled add(5, 2) -> {x}")

    if TYPE_CHECKING:
        reveal_type(x)  # should reveal "int"
        reveal_type(add)  # should reveal "(a: NumT@add, b: NumT@add) -> NumT@add"
        reveal_type(doubled)  # should reveal "(c: (**_P@doubled) -> NumT@doubled) -> ((**_P@doubled) -> NumT@doubled)"
```

[child ⬇️](#0236633e-756b-4691-9c22-0d65ac40e5bb)

---

(main branch ⎇)
###### 0236633e-756b-4691-9c22-0d65ac40e5bb
[parent ⬆️](#ac2802d2-4c64-4077-bf8b-6faa64e9fbfb)
