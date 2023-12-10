---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (11).md
heading_stack: <root> -> abe35052-cbe5-48c3-af93-8211c1803451 -> System -> 8f3ecc4a-8b68-4f89-9885-144c44a41411 -> System -> aaa23237-a0ee-437a-8a74-7126fe1c65dc -> User -> XL Overview -> Requirements -> General architecture -> File Structure -> Lossless -> Current Reference Implementation -> Conventions -> Architecture -> Decoder overview -> 47439873-a420-4f30-b9a3-bb77dd2a5aec -> Assistant -> Comprehensive Summary for CFFI Bindings for libjxl -> Key Requirements -> General Architecture -> File Structure
---
#### File Structure

1. Starts with `FileHeader`.
2. Multiple passes (DC or AC_LF) are added together for the final image.
3. Each pass contains groups of AC and DC data that can be decoded in parallel.

