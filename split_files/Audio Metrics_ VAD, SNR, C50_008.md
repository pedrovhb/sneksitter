---
file: /home/pedro/Documents/chatgpt_export/Markdown/Audio Metrics_ VAD, SNR, C50.md
heading_stack: <root> -> b1e23d59-6ad0-4ef7-a169-acf2e339bd00 -> System -> 624193d3-c2b2-4bf7-a466-07d277afd1ce -> System -> aaa2d697-3c69-41fa-9d99-fbca08692e7a -> User -> apply model -> iterate over each frame
---
# iterate over each frame
for frame, (vad, snr, c50) in output:
    t = frame.middle
    print(f"{t:8.3f} vad={100*vad:.0f}% snr={snr:.0f} c50={c50:.0f}")
