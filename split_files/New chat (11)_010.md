---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (11).md
heading_stack: <root> -> abe35052-cbe5-48c3-af93-8211c1803451 -> System -> 8f3ecc4a-8b68-4f89-9885-144c44a41411 -> System -> aaa23237-a0ee-437a-8a74-7126fe1c65dc -> User -> XL Overview -> Requirements -> General architecture -> File Structure
---
# File Structure

A codestream begins with a `FileHeader` followed by one or more "passes"
(= scans: e.g. DC or AC_LF) which are then added together (summing the
respective color components in Opsin space) to form the final image. There is no
limit to the number of passes, so an encoder could choose to send salient parts
first, followed by arbitrary decompositions of the final image (in terms of
resolution, bit depth, quality or spatial location).

Each pass contains groups of AC and DC data. A group is a subset of pixels that
can be decoded in parallel. DC groups contain 256x256 DCs (from 2048x2048 input
pixels), AC groups cover 256x256 input pixels.

Each pass starts with a table of contents (sizes of each of their DC+AC
groups), which enables parallel decoding and/or the decoding of a subset.
However, there is no higher-level TOC of passes, as that would prevent
appending additional images and could be too constraining for the encoder.


## Lossless

JPEG XL supports tools for lossless coding designed by Alexander Rhatushnyak and
Jon Sneyers. They are about 60-75% of size of PNG, and smaller than WebP
lossless for photos.

An adaptive predictor computes 4 from the NW, N, NE and W pixels and combines
them with weights based on previous errors. The error value is encoded in a
bucket chosen based on a heuristic max error. The result is entropy-coded using
the ANS encoder.

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

## Decoder overview

After decoding headers, the decoder begins processing frames (`dec_frame.cc`).

For each pass, it will read the DC group table of contents (TOC) and start
decoding, dequantizing and restoring color correlation of each DC group
(covering 2048x2048 pixels in the input image) in parallel
(`compressed_dc.cc`). The DC is split into parts corresponding to each AC group
(with 1px of extra border); the AC group TOC is read and each AC group (256x256
pixels) is processed in parallel (`dec_group.cc`).

In each AC group, the decoder reads per-block side information indicating the
kind of DCT transform; this is followed by the quantization field. Then, AC
coefficients are read, dequantized and have color correlation restored on a
tile per tile basis for better locality.

After all the groups are read, postprocessing is applied: Gaborish smoothing
and edge preserving filter, to reduce blocking and other artifacts.

Finally, the image is converted back from the XYB color space
(`dec_xyb.cc`) and saved to the output image (`codec_*.cc`).

[child ⬇️](#47439873-a420-4f30-b9a3-bb77dd2a5aec)

---

(main branch ⎇)
###### 47439873-a420-4f30-b9a3-bb77dd2a5aec
[parent ⬆️](#aaa23237-a0ee-437a-8a74-7126fe1c65dc)
