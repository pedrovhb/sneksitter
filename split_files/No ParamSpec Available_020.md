---
file: /home/pedro/Documents/chatgpt_export/Markdown/No ParamSpec Available.md
heading_stack: <root> -> dad99942-0f1f-4dba-9e02-2fd72f8a04e1 -> System -> 958b6e43-778f-4c79-88fc-d066a7cf90df -> System -> aaa2e994-c802-4cf3-842c-5533a1176f22 -> User -> 9f0c2854-2b94-4ff5-a675-13553ec0e0e8 -> Assistant -> 6c19a463-bae2-4a48-bdbc-85cc7cfd53bb -> Tool -> eb2cd2fb-58e5-459e-96e0-722fcd9c674f -> Assistant -> aaa292bc-ed3a-48ba-9c8e-2e8e7547b2ae -> User -> 60c029bf-2cb5-4845-8273-0b3ed78b13e8 -> Assistant -> aaa2874c-c2c4-425a-b2bf-4aad055089c3 -> User -> 76ce0814-52dd-400c-993b-cb1ca0f29863 -> Assistant
---
# Assistant

```python
from typing import Tuple

def adjust_rgb(color: Tuple[int, int, int], saturation: float = 1.0, lightness: float = 1.0) -> Tuple[int, int, int]:
    """
    Adjusts the RGB color based on saturation and lightness factors.
    
    Parameters:
    - color: Tuple containing RGB values (0-255)
    - saturation: Saturation factor (1.0 means no change, < 1.0 desaturates, > 1.0 increases saturation)
    - lightness: Lightness factor (1.0 means no change, < 1.0 darkens, > 1.0 lightens)
    
    Returns:
    - Tuple containing the adjusted RGB values
    """
    r, g, b = color
    gray = int((r * 0.3) + (g * 0.59) + (b * 0.11))
    
    # Adjust saturation
    r = int(gray + (r - gray) * saturation)
    g = int(gray + (g - gray) * saturation)
    b = int(gray + (b - gray) * saturation)
    
    # Adjust lightness
    r = int(r * lightness)
    g = int(g * lightness)
    b = int(b * lightness)
    
    # Clamp the values between 0 and 255
    r, g, b = min(255, max(0, r)), min(255, max(0, g)), min(255, max(0, b))
    
    return (r, g, b)

# Test the function with sample RGB values
test_rgb = (128, 64, 32)
desaturated = adjust_rgb(test_rgb, saturation=0.5)
saturated = adjust_rgb(test_rgb, saturation=1.5)
lightened = adjust_rgb(test_rgb, lightness=1.2)

desaturated, saturated, lightened
```

[child ⬇️](#2a2229e8-9fb6-44d6-a5f1-34d925bbed85)

---

(main branch ⎇)
###### 2a2229e8-9fb6-44d6-a5f1-34d925bbed85
[parent ⬆️](#76ce0814-52dd-400c-993b-cb1ca0f29863)
