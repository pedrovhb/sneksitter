---
file: /home/pedro/projs/transformers/docs/source/en/pipeline_tutorial.md
heading_stack: <root> -> Pipelines for inference -> Pipeline usage -> Parameters -> Device -> Batch size -> Task specific parameters -> Using pipelines on a dataset -> Using pipelines for a webserver -> Vision pipeline -> Text pipeline -> Multimodal pipeline -> Using `pipeline` on large models with 🤗 `accelerate`:
---
## Using `pipeline` on large models with 🤗 `accelerate`:

You can easily run `pipeline` on large models using 🤗 `accelerate`! First make sure you have installed `accelerate` with `pip install accelerate`. 

First load your model using `device_map="auto"`! We will use `facebook/opt-1.3b` for our example.

```py
# pip install accelerate
import torch
from transformers import pipeline

pipe = pipeline(model="facebook/opt-1.3b", torch_dtype=torch.bfloat16, device_map="auto")
output = pipe("This is a cool example!", do_sample=True, top_p=0.95)
```

You can also pass 8-bit loaded models if you install `bitsandbytes` and add the argument `load_in_8bit=True`

```py
# pip install accelerate bitsandbytes
import torch
from transformers import pipeline

pipe = pipeline(model="facebook/opt-1.3b", device_map="auto", model_kwargs={"load_in_8bit": True})
output = pipe("This is a cool example!", do_sample=True, top_p=0.95)
```

Note that you can replace the checkpoint with any of the Hugging Face model that supports large model loading such as BLOOM!
