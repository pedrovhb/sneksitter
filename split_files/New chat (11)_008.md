---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (11).md
heading_stack: <root> -> abe35052-cbe5-48c3-af93-8211c1803451 -> System -> 8f3ecc4a-8b68-4f89-9885-144c44a41411 -> System -> aaa23237-a0ee-437a-8a74-7126fe1c65dc -> User -> XL Overview -> Requirements
---
## Requirements

JPEG XL was designed for two main requirements:

*   high quality: visually lossless at reasonable bitrates;
*   decoding speed: multithreaded decoding should be able to reach around
    400 Megapixel/s on large images.

These goals apply to various types of images, including HDR content, whose
support is made possible by full-precision (float32) computations and extensive
support of color spaces and transfer functions.

High performance is achieved by designing the format with careful consideration
of memory bandwidth usage and ease of SIMD/GPU implementation.

The full requirements for JPEG XL are listed in document wg1m82079.

