---
file: /home/pedro/Documents/chatgpt_export/Markdown/Audio Metrics_ VAD, SNR, C50.md
heading_stack: <root> -> b1e23d59-6ad0-4ef7-a169-acf2e339bd00 -> System -> 624193d3-c2b2-4bf7-a466-07d277afd1ce -> System -> aaa2d697-3c69-41fa-9d99-fbca08692e7a -> User -> apply model -> iterate over each frame -> ... -> 12.952 vad=100% snr=51 c50=17 -> 12.968 vad=100% snr=52 c50=17 -> 12.985 vad=100% snr=53 c50=17 -> ... -> fb8a49f1-6eac-4f76-8150-43797a373ea6 -> Assistant -> aaa2ddf2-1647-4fb1-8bfd-b2c64f9f1332 -> User -> 524563db-b004-4ef8-9b0b-070f499904f2 -> Assistant -> 1. Preprocessing -> 2. Voice Activity Detection (VAD)
---
### 2. Voice Activity Detection (VAD)
Use VAD to identify portions of the audio that likely contain speech.

```python
from pyannote.audio import Model, Inference

# Initialize model and inference
model = Model.from_pretrained("pyannote/brouhaha", use_auth_token="ACCESS_TOKEN_GOES_HERE")
inference = Inference(model)

# Run VAD
output = inference("input.wav")

# Collect speech segments
speech_segments = []
for frame, (vad, _, _) in output:
    if vad > 0.7:  # Threshold
        speech_segments.append(frame)
```

