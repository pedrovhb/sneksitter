---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (11).md
heading_stack: <root> -> abe35052-cbe5-48c3-af93-8211c1803451 -> System -> 8f3ecc4a-8b68-4f89-9885-144c44a41411 -> System -> aaa23237-a0ee-437a-8a74-7126fe1c65dc -> User -> XL Overview -> Requirements -> General architecture -> File Structure -> Lossless -> Current Reference Implementation -> Conventions -> Architecture
---
### Architecture

Getting back to the earlier block diagram:

**Header** handling is implemented in `headers.h` and `field*`.

**Bitstream**: `entropy_coder.h`, `dec_ans_*`.

**(De)quantize**: `quantizer.h`.

**DC prediction**: `predictor.h`.

**Chroma from luma**: `chroma_from_luma.h`

**(I)DCT**: `dct*.h`. Instead of operating directly on blocks of memory, the
functions operate on thin wrappers which can handle blocks spread across
multiple image lines.

**DCT size selection**: `ac_strategy.cc`

**[Gaborish]**: `enc_gaborish.h`.

**[Edge preserving filter]**: `epf.h`

**[Noise injection]**: `noise*` (currently disabled)

**Color space conversion**: `color_*`, `dec_xyb.h`.

