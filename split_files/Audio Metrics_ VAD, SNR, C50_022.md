---
file: /home/pedro/Documents/chatgpt_export/Markdown/Audio Metrics_ VAD, SNR, C50.md
heading_stack: <root> -> b1e23d59-6ad0-4ef7-a169-acf2e339bd00 -> System -> 624193d3-c2b2-4bf7-a466-07d277afd1ce -> System -> aaa2d697-3c69-41fa-9d99-fbca08692e7a -> User -> apply model -> iterate over each frame -> ... -> 12.952 vad=100% snr=51 c50=17 -> 12.968 vad=100% snr=52 c50=17 -> 12.985 vad=100% snr=53 c50=17 -> ... -> fb8a49f1-6eac-4f76-8150-43797a373ea6 -> Assistant -> aaa2ddf2-1647-4fb1-8bfd-b2c64f9f1332 -> User -> 524563db-b004-4ef8-9b0b-070f499904f2 -> Assistant -> 1. Preprocessing -> 2. Voice Activity Detection (VAD) -> 3. Segment Audio
---
### 3. Segment Audio
Group consecutive frames to form speech segments and then extract those segments as separate audio clips.

```python
# Pseudo-code to group consecutive frames
grouped_segments = group_consecutive_frames(speech_segments)

# Extract audio segments
for segment in grouped_segments:
    start, end = segment
    extracted_audio = audio[start:end]
    # Save or process the extracted audio
```

