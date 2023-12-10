---
file: /home/pedro/Documents/chatgpt_export/Markdown/No ParamSpec Available.md
heading_stack: <root> -> dad99942-0f1f-4dba-9e02-2fd72f8a04e1 -> System -> 958b6e43-778f-4c79-88fc-d066a7cf90df -> System -> aaa2e994-c802-4cf3-842c-5533a1176f22 -> User -> 9f0c2854-2b94-4ff5-a675-13553ec0e0e8 -> Assistant -> 6c19a463-bae2-4a48-bdbc-85cc7cfd53bb -> Tool -> eb2cd2fb-58e5-459e-96e0-722fcd9c674f -> Assistant -> aaa292bc-ed3a-48ba-9c8e-2e8e7547b2ae -> User -> 60c029bf-2cb5-4845-8273-0b3ed78b13e8 -> Assistant -> aaa2874c-c2c4-425a-b2bf-4aad055089c3 -> User -> 76ce0814-52dd-400c-993b-cb1ca0f29863 -> Assistant -> 2a2229e8-9fb6-44d6-a5f1-34d925bbed85 -> Tool -> c18f6738-9091-40ca-833c-3aaa0e193e60 -> Assistant -> 21c42781-065c-4772-9c46-ffb387433ec9 -> Assistant -> aaa23e56-62bb-4050-aa00-a7c28fd14827 -> User -> 1131b2ec-ad6f-4b0f-8c2a-a584eaa695ce -> Assistant -> CIELAB -> CIE XYZ -> aaa293fd-2f16-4ef2-b0a1-456259823b50 -> User -> 0a42b66d-b93f-4522-95b3-f61f3dc0e695 -> Assistant
---
# Assistant

```python
from typing import Tuple
import colorsys
import math

# Define the conversion functions
def rgb_to_xyz(rgb: Tuple[int, int, int]) -> Tuple[float, float, float]:
    r, g, b = [x / 255.0 for x in rgb]
    r = 100 * (r / 12.92 if r <= 0.04045 else ((r + 0.055) / 1.055) ** 2.4)
    g = 100 * (g / 12.92 if g <= 0.04045 else ((g + 0.055) / 1.055) ** 2.4)
    b = 100 * (b / 12.92 if b <= 0.04045 else ((b + 0.055) / 1.055) ** 2.4)
    x = 0.4124 * r + 0.3576 * g + 0.1805 * b
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    z = 0.0193 * r + 0.1192 * g + 0.9505 * b
    return x, y, z

def xyz_to_rgb(xyz: Tuple[float, float, float]) -> Tuple[int, int, int]:
    x, y, z = xyz
    x /= 100.0
    y /= 100.0
    z /= 100.0
    r = 3.2406 * x + -1.5372 * y + -0.4986 * z
    g = -0.9689 * x + 1.8758 * y + 0.0415 * z
    b = 0.0557 * x + -0.2040 * y + 1.0570 * z
    r = 255.0 * (r / 1.055 if r > 0.0031308 else 12.92 * r)
    g = 255.0 * (g / 1.055 if g > 0.0031308 else 12.92 * g)
    b = 255.0 * (b / 1.055 if b > 0.0031308 else 12.92 * b)
    return int(round(r)), int(round(g)), int(round(b))

def adjust_lightness_xyz(xyz: Tuple[float, float, float], lightness: float) -> Tuple[float, float, float]:
    x, y, z = xyz
    return x, y * lightness, z

# Test the conversion and adjustment functions
sample_rgb = (128, 64, 32)
sample_xyz = rgb_to_xyz(sample_rgb)
lightened_xyz = adjust_lightness_xyz(sample_xyz, 1.2)
lightened_rgb = xyz_to_rgb(lightened_xyz)

sample_xyz, lightened_xyz, lightened_rgb
```

[child ⬇️](#dea296ac-6ae7-487a-b8b5-2cae906092ec)

---

(main branch ⎇)
###### dea296ac-6ae7-487a-b8b5-2cae906092ec
[parent ⬆️](#0a42b66d-b93f-4522-95b3-f61f3dc0e695)
