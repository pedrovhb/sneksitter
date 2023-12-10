---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (11).md
heading_stack: <root> -> abe35052-cbe5-48c3-af93-8211c1803451 -> System -> 8f3ecc4a-8b68-4f89-9885-144c44a41411 -> System -> aaa23237-a0ee-437a-8a74-7126fe1c65dc -> User -> XL Overview -> Requirements -> General architecture -> File Structure -> Lossless -> Current Reference Implementation -> Conventions -> Architecture -> Decoder overview -> 47439873-a420-4f30-b9a3-bb77dd2a5aec -> Assistant -> Comprehensive Summary for CFFI Bindings for libjxl -> Key Requirements -> General Architecture
---
#### General Architecture

Decoder's Modules:
1. **Header**: Decode metadata like image dimensions.
2. **Bitstream**: Decode transform coefficient residuals.
3. **Dequantize**: From adaptive quant map side information.
4. **DC Prediction**: Expand DC residuals.
5. **Chroma from Luma**: Restore predicted X from B and Y from B.
6. **IDCT**: 2x2 to 32x32, floating-point.
7. **Optional Post-Processing**: Gaborish, Edge preserving filter, Noise injection.
8. **Color Space Conversion**: From XYB to RGB.

Encoder is the reverse with modules for noise estimation, adaptive quantization, etc.

