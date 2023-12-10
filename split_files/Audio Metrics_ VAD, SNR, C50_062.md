---
file: /home/pedro/Documents/chatgpt_export/Markdown/Audio Metrics_ VAD, SNR, C50.md
heading_stack: <root> -> b1e23d59-6ad0-4ef7-a169-acf2e339bd00 -> System -> 624193d3-c2b2-4bf7-a466-07d277afd1ce -> System -> aaa2d697-3c69-41fa-9d99-fbca08692e7a -> User -> apply model -> iterate over each frame -> ... -> 12.952 vad=100% snr=51 c50=17 -> 12.968 vad=100% snr=52 c50=17 -> 12.985 vad=100% snr=53 c50=17 -> ... -> fb8a49f1-6eac-4f76-8150-43797a373ea6 -> Assistant -> aaa2ddf2-1647-4fb1-8bfd-b2c64f9f1332 -> User -> 524563db-b004-4ef8-9b0b-070f499904f2 -> Assistant -> 1. Preprocessing -> 2. Voice Activity Detection (VAD) -> 3. Segment Audio -> 4. Signal-to-Noise Ratio (SNR) Filtering -> 5. Export Segments -> 6. Optional: Post-processing -> aaa2c47a-8e13-43af-a844-5dcf0bfc72ee -> User -> 5b6cd6e3-e03b-4269-bc74-c1b9788634a6 -> Assistant -> SNR (Signal-to-Noise Ratio) -> C50 (Clarity Index) -> Correlation -> Which to Use? -> aaa24ad1-2f18-499f-98ec-7398e741f17f -> User -> f8adef6f-f675-450b-85a9-24dea56c3e1c -> Assistant -> 1. Established Techniques and Literature Dealing with This Problem -> 2. Established Techniques for Dealing with Similar or Analogous Problems -> 3. Designing an Effective Approach for the Task -> Step 1: Initial Segmentation -> Step 2: Feature Calculation -> Step 3: Filtering -> Step 4: Sequence Identification -> Step 5: Scoring and Ranking -> Step 6: Output -> aaa2434c-861f-43a8-a50c-1bef20fc36a4 -> User -> 4bd45e48-5203-4a76-bf48-4fdde9f8e324 -> Assistant -> aaa258d3-afb4-45cc-9651-7a967a7032e9 -> User -> 02c6bd0d-7e79-4eb4-92c0-b7faebd86582 -> Assistant -> 1eed05f2-09c2-4749-ab23-91019cdfb537 -> Tool -> d2d1461c-8f9c-4afc-878f-5ea9577be3cd -> Assistant -> aaa21684-e58c-4067-a343-ae55f1d4af52 -> User -> f8a80132-ddd5-4111-8759-ccec18e91951 -> Assistant
---
# Assistant

```python
# Function to filter frames based on VAD, SNR, and C50 thresholds
def filter_frames(frames: List[Frame], vad_threshold: float = 0.3, snr_threshold: float = -10, c50_threshold: float = 40) -> List[Frame]:
    return [
        frame for frame in frames
        if frame.vad >= vad_threshold and frame.snr >= snr_threshold and frame.c50 >= c50_threshold
    ]

# Function to filter and rank sequences based on duration and score
def filter_and_rank_sequences(sequences: List[FrameSequence], min_duration: float = 0.05, max_duration: float = 1.0) -> List[Tuple[FrameSequence, float]]:
    filtered_sequences = [seq for seq in sequences if min_duration <= seq.duration <= max_duration]
    ranked_sequences = sorted(filtered_sequences, key=lambda x: x.score(), reverse=True)
    return [(seq, seq.score()) for seq in ranked_sequences]

# Mock more output frames for demonstration
more_mock_output = [
    Frame(10.0, 10.016, 10.008, 0.31, -6, 49),
    Frame(10.016, 10.032, 10.024, 0.15, -8, 35),
    Frame(10.032, 10.048, 10.040, 0.30, -6, 49),
    Frame(10.048, 10.064, 10.056, 0.40, -2, 55),
    Frame(10.064, 10.080, 10.072, 0.25, -10, 30),
    Frame(10.080, 10.096, 10.088, 0.35, -4, 50),
]

# Filter frames based on thresholds
filtered_frames = filter_frames(more_mock_output)

# Group filtered frames into sequences
grouped_sequences = group_frames(filtered_frames)

# Filter and rank sequences based on duration and score
ranked_sequences = filter_and_rank_sequences(grouped_sequences)

# Display ranked sequences and their scores
for i, (seq, score) in enumerate(ranked_sequences):
    print(f"Rank {i+1}, Duration: {seq.duration}, Score: {score}, Avg VAD: {seq.avg_vad}, Avg SNR: {seq.avg_snr}, Avg C50: {seq.avg_c50}")
```

[child ⬇️](#ab99d04b-8160-4908-aa1d-2319a2850d47)

---

(other branch ⎇)
###### ab99d04b-8160-4908-aa1d-2319a2850d47
[parent ⬆️](#f8a80132-ddd5-4111-8759-ccec18e91951)
