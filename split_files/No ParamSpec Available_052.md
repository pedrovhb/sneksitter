---
file: /home/pedro/Documents/chatgpt_export/Markdown/No ParamSpec Available.md
heading_stack: <root> -> dad99942-0f1f-4dba-9e02-2fd72f8a04e1 -> System -> 958b6e43-778f-4c79-88fc-d066a7cf90df -> System -> aaa2e994-c802-4cf3-842c-5533a1176f22 -> User -> 9f0c2854-2b94-4ff5-a675-13553ec0e0e8 -> Assistant -> 6c19a463-bae2-4a48-bdbc-85cc7cfd53bb -> Tool -> eb2cd2fb-58e5-459e-96e0-722fcd9c674f -> Assistant -> aaa292bc-ed3a-48ba-9c8e-2e8e7547b2ae -> User -> 60c029bf-2cb5-4845-8273-0b3ed78b13e8 -> Assistant -> aaa2874c-c2c4-425a-b2bf-4aad055089c3 -> User -> 76ce0814-52dd-400c-993b-cb1ca0f29863 -> Assistant -> 2a2229e8-9fb6-44d6-a5f1-34d925bbed85 -> Tool -> c18f6738-9091-40ca-833c-3aaa0e193e60 -> Assistant -> 21c42781-065c-4772-9c46-ffb387433ec9 -> Assistant -> aaa23e56-62bb-4050-aa00-a7c28fd14827 -> User -> 1131b2ec-ad6f-4b0f-8c2a-a584eaa695ce -> Assistant -> CIELAB -> CIE XYZ -> aaa293fd-2f16-4ef2-b0a1-456259823b50 -> User -> 0a42b66d-b93f-4522-95b3-f61f3dc0e695 -> Assistant -> dea296ac-6ae7-487a-b8b5-2cae906092ec -> Tool -> 4952cf67-eb49-4fab-af41-0d1be8ca665a -> Assistant -> aaa279b8-4797-4641-8eee-4f489a4e4d5b -> User -> aaa24466-7c1e-45ee-8858-48fb25dec843 -> User -> d094c262-9c72-42d1-87c3-39801d1e77d2 -> Assistant -> aaa2a396-d91d-4a09-b45f-9dd21d41a9a0 -> User -> 646ed682-3b4e-4645-9cf1-ab9aedc228c1 -> Assistant -> Installation -> Code Example
---
### Code Example
```python
import colorspacious as cs

# Sample RGB color (in sRGB space)
rgb = [128, 64, 32]

# Convert RGB to CIELAB
lab = cs.cspace_convert(rgb, start={"name": "sRGB1"}, end={"name": "CIELab"})

# Adjust L* for Lightness
lab[0] *= 1.2  # Increase lightness by 20%

# Adjust a* and b* for Saturation
lab[1] *= 1.2  # Increase saturation in the a* channel by 20%
lab[2] *= 1.2  # Increase saturation in the b* channel by 20%

# Convert back to RGB
adjusted_rgb = cs.cspace_convert(lab, start={"name": "CIELab"}, end={"name": "sRGB1"})

# Round the RGB values to integers
adjusted_rgb = [round(x) for x in adjusted_rgb]

print("Original RGB:", rgb)
print("Adjusted RGB:", adjusted_rgb)
```

This will adjust the lightness and saturation in the CIELAB color space and then convert it back to RGB. The `colorspacious` library takes care of the intricacies of the color conversion to give you more accurate results.

Would you like more details or another example using a different library?

[child ⬇️](#aaa2b416-822c-44b4-a516-96fd56660e7d)

---

(main branch ⎇)
###### aaa2b416-822c-44b4-a516-96fd56660e7d
[parent ⬆️](#646ed682-3b4e-4645-9cf1-ab9aedc228c1)
