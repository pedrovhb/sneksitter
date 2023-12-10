---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (11).md
heading_stack: <root> -> abe35052-cbe5-48c3-af93-8211c1803451 -> System -> 8f3ecc4a-8b68-4f89-9885-144c44a41411 -> System -> aaa23237-a0ee-437a-8a74-7126fe1c65dc -> User -> XL Overview -> Requirements -> General architecture -> File Structure -> Lossless -> Current Reference Implementation
---
## Current Reference Implementation

### Conventions

The software is written in C++ and built using CMake 3.6 or later.

Error handling is done by having functions return values of type `jxl::Status`
(a thin wrapper around bool which checks that it is not ignored). A convenience
macro named `JXL_RETURN_IF_ERROR` makes this more convenient by automatically
forwarding errors, and another macro named `JXL_FAILURE` exits with an error
message if reached, with no effect in optimized builds.

To diagnose the cause of encoder/decoder failures (which often only result in a
generic "decode failed" message), build using the following command:

```bash
CMAKE_FLAGS="-DJXL_CRASH_ON_ERROR" ./ci.sh opt
```

In such builds, the first JXL_FAILURE will print a message identifying where the
problem is and the program will exit immediately afterwards.

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

