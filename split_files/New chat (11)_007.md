---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (11).md
heading_stack: <root> -> abe35052-cbe5-48c3-af93-8211c1803451 -> System -> 8f3ecc4a-8b68-4f89-9885-144c44a41411 -> System -> aaa23237-a0ee-437a-8a74-7126fe1c65dc -> User -> XL Overview
---
# XL Overview

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

## General architecture

The architecture follows the traditional block transform model with improvements
in the individual components. For a quick overview, we sketch a "block diagram"
of the lossy format decoder in the form of module names in **bold** followed by
a brief description. Note that post-processing modules in [brackets] are
optional - they are unnecessary or even counterproductive at very high quality
settings.

**Header**: decode metadata (e.g. image dimensions) from compressed fields
(smaller than Exp-Golomb thanks to per-field encodings). The compression and
small number of required fields enables very compact headers - much smaller than
JFIF and HEVC. The container supports multiple images (e.g. animations/bursts)
and passes (progressive).

**Bitstream**: decode transform coefficient residuals using rANS-encoded
<#bits,bits> symbols

**Dequantize**: from adaptive quant map side information, plus chroma from luma

**DC prediction**: expand DC residuals using adaptive (history-based) predictors

**Chroma from luma**: restore predicted X from B and Y from B

**IDCT:** 2x2..32x32, floating-point

**[Gaborish]**: additional deblocking convolution with 3x3 kernel

**[Edge preserving filter]**: nonlinear adaptive smoothing controlled by side
information

**[Noise injection]**: add perceptually pleasing noise according to a per-image
noise model

**Color space conversion**: from perceptual opsin XYB to linear RGB

**[Converting to other color spaces via ICC]**

The encoder is basically the reverse:

**Color space conversion**: from linear RGB to perceptual opsin XYB

**[Noise estimation]**: compute a noise model for the image

**[Gaborish]**: sharpening to counteract the blurring on the decoder side

**DCT**: transform sizes communicated via per-block side information

**Chroma from luma**: find the best multipliers of Y for X and B channels of
entire image

**Adaptive quantization**: iterative search for quant map that yields the best
perceived restoration

**Quantize**: store 16-bit prediction residuals

**DC prediction**: store residuals (prediction happens in quantized space)

**Entropy coding**: rANS and context modeling with clustering


