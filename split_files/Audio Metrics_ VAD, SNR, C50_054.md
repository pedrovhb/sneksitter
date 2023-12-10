---
file: /home/pedro/Documents/chatgpt_export/Markdown/Audio Metrics_ VAD, SNR, C50.md
heading_stack: <root> -> b1e23d59-6ad0-4ef7-a169-acf2e339bd00 -> System -> 624193d3-c2b2-4bf7-a466-07d277afd1ce -> System -> aaa2d697-3c69-41fa-9d99-fbca08692e7a -> User -> apply model -> iterate over each frame -> ... -> 12.952 vad=100% snr=51 c50=17 -> 12.968 vad=100% snr=52 c50=17 -> 12.985 vad=100% snr=53 c50=17 -> ... -> fb8a49f1-6eac-4f76-8150-43797a373ea6 -> Assistant -> aaa2ddf2-1647-4fb1-8bfd-b2c64f9f1332 -> User -> 524563db-b004-4ef8-9b0b-070f499904f2 -> Assistant -> 1. Preprocessing -> 2. Voice Activity Detection (VAD) -> 3. Segment Audio -> 4. Signal-to-Noise Ratio (SNR) Filtering -> 5. Export Segments -> 6. Optional: Post-processing -> aaa2c47a-8e13-43af-a844-5dcf0bfc72ee -> User -> 5b6cd6e3-e03b-4269-bc74-c1b9788634a6 -> Assistant -> SNR (Signal-to-Noise Ratio) -> C50 (Clarity Index) -> Correlation -> Which to Use? -> aaa24ad1-2f18-499f-98ec-7398e741f17f -> User -> f8adef6f-f675-450b-85a9-24dea56c3e1c -> Assistant -> 1. Established Techniques and Literature Dealing with This Problem -> 2. Established Techniques for Dealing with Similar or Analogous Problems -> 3. Designing an Effective Approach for the Task -> Step 1: Initial Segmentation -> Step 2: Feature Calculation -> Step 3: Filtering -> Step 4: Sequence Identification -> Step 5: Scoring and Ranking -> Step 6: Output -> aaa2434c-861f-43a8-a50c-1bef20fc36a4 -> User -> 4bd45e48-5203-4a76-bf48-4fdde9f8e324 -> Assistant -> aaa258d3-afb4-45cc-9651-7a967a7032e9 -> User -> 02c6bd0d-7e79-4eb4-92c0-b7faebd86582 -> Assistant
---
# Assistant

```python
# Importing required modules
from dataclasses import dataclass, field
from typing import List, Tuple
import statistics

# Define dataclass for a frame and its associated metrics (VAD, SNR, C50)
@dataclass
class Frame:
    start: float
    end: float
    middle: float
    vad: float
    snr: float
    c50: float

    @property
    def duration(self) -> float:
        return self.end - self.start

# Mocked output iterator (just for demonstration purposes)
mock_output = [
    Frame(10.0, 10.016, 10.008, 0.31, -6, 49),
    Frame(10.016, 10.032, 10.024, 0.31, -6, 49),
    Frame(10.032, 10.048, 10.040, 0.30, -6, 49),
    Frame(10.048, 10.064, 10.056, 0.30, -6, 49),
    # ... (more frames)
]

# Dataclass to hold a sequence of frames
@dataclass
class FrameSequence:
    frames: List[Frame] = field(default_factory=list)

    @property
    def duration(self) -> float:
        return sum(frame.duration for frame in self.frames)

    @property
    def avg_vad(self) -> float:
        return statistics.mean(frame.vad for frame in self.frames)

    @property
    def avg_snr(self) -> float:
        return statistics.mean(frame.snr for frame in self.frames)

    @property
    def avg_c50(self) -> float:
        return statistics.mean(frame.c50 for frame in self.frames)

    def score(self, vad_weight: float = 1.0, snr_weight: float = 1.0, c50_weight: float = 1.0) -> float:
        return self.avg_vad * vad_weight + self.avg_snr * snr_weight + self.avg_c50 * c50_weight

# Function to group consecutive frames into sequences
def group_frames(frames: List[Frame], min_gap: float = 0.016) -> List[FrameSequence]:
    sequences = []
    current_sequence = FrameSequence()

    for frame in frames:
        if current_sequence.frames:
            last_frame = current_sequence.frames[-1]
            gap = frame.start - last_frame.end
            if gap > min_gap:
                sequences.append(current_sequence)
                current_sequence = FrameSequence()

        current_sequence.frames.append(frame)

    if current_sequence.frames:
        sequences.append(current_sequence)

    return sequences

# Test the helper functions
grouped_sequences = group_frames(mock_output)
for seq in grouped_sequences:
    print(f"Duration: {seq.duration}, Avg VAD: {seq.avg_vad}, Avg SNR: {seq.avg_snr}, Avg C50: {seq.avg_c50}, Score: {seq.score()}")
```

[child ⬇️](#1eed05f2-09c2-4749-ab23-91019cdfb537)

---

(main branch ⎇)
###### 1eed05f2-09c2-4749-ab23-91019cdfb537
[parent ⬆️](#02c6bd0d-7e79-4eb4-92c0-b7faebd86582)
