---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (1).md
heading_stack: <root> -> 18e042b6-0753-47b9-8b94-dbf396965d51 -> System -> 705df361-3567-44f4-ad9c-70bb5d82744c -> System -> aaa29996-ddf3-403a-a4bb-fdfc7ef52d1a -> User -> 29be782a-5014-4a86-af90-9005dfcedffd -> Assistant -> Naive Implementation -> LRU Cached Version -> 1b9602eb-4a57-4178-bdd7-e7b55fca4a3b -> Assistant
---
# Assistant

```python
from functools import lru_cache
from typing import Tuple

@lru_cache(maxsize=128)
def adjust_rgb_lru_cached(color: Tuple[int, int, int], saturation: float = 1.0, lightness: float = 1.0) -> Tuple[int, int, int]:
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

[child ⬇️](#7a2ff30b-7f64-44c1-9cf3-ce1be5a8528d)

---

(main branch ⎇)
###### 7a2ff30b-7f64-44c1-9cf3-ce1be5a8528d
[parent ⬆️](#1b9602eb-4a57-4178-bdd7-e7b55fca4a3b)
