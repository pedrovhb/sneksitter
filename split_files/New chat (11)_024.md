---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (11).md
heading_stack: <root> -> abe35052-cbe5-48c3-af93-8211c1803451 -> System -> 8f3ecc4a-8b68-4f89-9885-144c44a41411 -> System -> aaa23237-a0ee-437a-8a74-7126fe1c65dc -> User -> XL Overview -> Requirements -> General architecture -> File Structure -> Lossless -> Current Reference Implementation -> Conventions -> Architecture -> Decoder overview -> 47439873-a420-4f30-b9a3-bb77dd2a5aec -> Assistant -> Comprehensive Summary for CFFI Bindings for libjxl -> Key Requirements -> General Architecture -> File Structure -> Lossless -> Current Reference Implementation -> Decoder Overview
---
#### Decoder Overview

1. Processes frames (`dec_frame.cc`).
2. Reads DC and AC group TOCs.
3. Decodes, dequantizes, and restores color correlation in parallel (`dec_group.cc`).
4. Applies postprocessing.
5. Converts back from XYB and saves (`codec_*.cc`).

