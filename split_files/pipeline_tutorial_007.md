---
file: /home/pedro/projs/transformers/docs/source/en/pipeline_tutorial.md
heading_stack: <root> -> Pipelines for inference -> Pipeline usage -> Parameters -> Device -> Batch size -> Task specific parameters -> Using pipelines on a dataset
---
## Using pipelines on a dataset

The pipeline can also run inference on a large dataset. The easiest way we recommend doing this is by using an iterator:

```py
def data():
    for i in range(1000):
        yield f"My example {i}"


pipe = pipeline(model="gpt2", device=0)
generated_characters = 0
for out in pipe(data()):
    generated_characters += len(out[0]["generated_text"])
```

The iterator `data()` yields each result, and the pipeline automatically
recognizes the input is iterable and will start fetching the data while
it continues to process it on the GPU (this uses [DataLoader](https://pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader) under the hood).
This is important because you don't have to allocate memory for the whole dataset
and you can feed the GPU as fast as possible.

Since batching could speed things up, it may be useful to try tuning the `batch_size` parameter here.

The simplest way to iterate over a dataset is to just load one from 🤗 [Datasets](https://github.com/huggingface/datasets/):

```py
# KeyDataset is a util that will just output the item we're interested in.
from transformers.pipelines.pt_utils import KeyDataset
from datasets import load_dataset

pipe = pipeline(model="hf-internal-testing/tiny-random-wav2vec2", device=0)
dataset = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation[:10]")

for out in pipe(KeyDataset(dataset, "audio")):
    print(out)
```


