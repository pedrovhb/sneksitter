---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (11).md
heading_stack: <root> -> abe35052-cbe5-48c3-af93-8211c1803451 -> System -> 8f3ecc4a-8b68-4f89-9885-144c44a41411 -> System -> aaa23237-a0ee-437a-8a74-7126fe1c65dc -> User -> XL Overview -> Requirements -> General architecture -> File Structure -> Lossless
---
## Lossless

JPEG XL supports tools for lossless coding designed by Alexander Rhatushnyak and
Jon Sneyers. They are about 60-75% of size of PNG, and smaller than WebP
lossless for photos.

An adaptive predictor computes 4 from the NW, N, NE and W pixels and combines
them with weights based on previous errors. The error value is encoded in a
bucket chosen based on a heuristic max error. The result is entropy-coded using
the ANS encoder.

