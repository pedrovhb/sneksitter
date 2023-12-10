---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (11).md
heading_stack: <root> -> abe35052-cbe5-48c3-af93-8211c1803451 -> System -> 8f3ecc4a-8b68-4f89-9885-144c44a41411 -> System -> aaa23237-a0ee-437a-8a74-7126fe1c65dc -> User -> XL Overview -> Requirements -> General architecture -> File Structure -> Lossless -> Current Reference Implementation -> Conventions -> Architecture -> Decoder overview
---
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
