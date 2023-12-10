---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (1).md
heading_stack: <root> -> 18e042b6-0753-47b9-8b94-dbf396965d51 -> System -> 705df361-3567-44f4-ad9c-70bb5d82744c -> System -> aaa29996-ddf3-403a-a4bb-fdfc7ef52d1a -> User -> 29be782a-5014-4a86-af90-9005dfcedffd -> Assistant -> Naive Implementation -> LRU Cached Version -> 1b9602eb-4a57-4178-bdd7-e7b55fca4a3b -> Assistant -> 7a2ff30b-7f64-44c1-9cf3-ce1be5a8528d -> Tool -> da282554-170d-416f-9f9d-d980cbed2faa -> Assistant -> Tolerant LRU Cache Implementation -> b712a863-6a4b-4b23-85ee-109191da28fa -> Assistant
---
# Assistant

```python
from collections import OrderedDict
from typing import Callable, Any, Hashable, TypeVar, Tuple

# Define a generic type for the return value of the function to be cached
_R = TypeVar("_R")

def tolerant_lru_cache(maxsize: int = 128, tolerance: int = 5) -> Callable[[Callable[..., _R]], Callable[..., _R]]:
    """
    An LRU cache implementation that is tolerant to floating-point variations.
    
    Parameters:
    - maxsize: Maximum cache size
    - tolerance: Number of decimal places for rounding floating-point numbers
    
    Returns:
    - A decorator to wrap around the function whose output is to be cached
    """
    cache = OrderedDict()
    
    def decorator(func: Callable[..., _R]) -> Callable[..., _R]:
        def wrapper(*args: Any, **kwargs: Any) -> _R:
            # Round the floating-point arguments to the specified tolerance
            tolerant_args = tuple(round(arg, tolerance) if isinstance(arg, float) else arg for arg in args)
            tolerant_kwargs = {k: round(v, tolerance) if isinstance(v, float) else v for k, v in kwargs.items()}
            
            # Create a hashable key for the arguments
            key: Hashable = (tolerant_args, frozenset(tolerant_kwargs.items()))
            
            # Check if result is in cache
            if key in cache:
                # Move the key to the end to show that it was recently used
                cache.move_to_end(key)
                return cache[key]
            
            # Calculate and store result in cache
            result = func(*args, **kwargs)
            cache[key] = result
            
            # Remove the oldest item from cache if exceeding max size
            if len(cache) > maxsize:
                cache.popitem(last=False)
            
            return result
        
        return wrapper
    
    return decorator

@tolerant_lru_cache(maxsize=128, tolerance=5)
def adjust_rgb_tolerant_cached(color: Tuple[int, int, int], saturation: float = 1.0, lightness: float = 1.0) -> Tuple[int, int, int]:
    r, g, b = color

    if saturation != 1:
        gray = (r * 0.3) + (g * 0.59) + (b * 0.11)
        
        # Adjust saturation
        r = gray + (r - gray) * saturation
        g = gray + (g - gray) * saturation
        b = gray + (b - gray) * saturation

    if lightness != 1:
        # Adjust lightness
        r = r * lightness
        g = g * lightness
        b = b * lightness
    
    # Clamp the values between 0 and 255
    r, g, b = min(255, max(0, r)), min(255, max(0, g)), min(255, max(0, b))
    
    return tuple(int(x) for x in (r, g, b))
```

[child ⬇️](#5663a5e3-9e34-4b5d-b20e-2a69ee6dcc7a)

---

(main branch ⎇)
###### 5663a5e3-9e34-4b5d-b20e-2a69ee6dcc7a
[parent ⬆️](#b712a863-6a4b-4b23-85ee-109191da28fa)
