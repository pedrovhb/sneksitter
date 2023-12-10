---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (1).md
heading_stack: <root> -> 18e042b6-0753-47b9-8b94-dbf396965d51 -> System -> 705df361-3567-44f4-ad9c-70bb5d82744c -> System -> aaa29996-ddf3-403a-a4bb-fdfc7ef52d1a -> User
---
# User

Let's build an efficient and optimized version of lru_cache which has some specified tolerance for floating point calculations. Benchmark the naive, lru_cache, and tolerant_lru_cache with the following -


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
    
    return [int(x) for x in (r, g, b)]
  

[child ⬇️](#29be782a-5014-4a86-af90-9005dfcedffd)

---

(main branch ⎇)
###### 29be782a-5014-4a86-af90-9005dfcedffd
[parent ⬆️](#aaa29996-ddf3-403a-a4bb-fdfc7ef52d1a)
