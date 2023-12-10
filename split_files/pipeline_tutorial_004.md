---
file: /home/pedro/projs/transformers/docs/source/en/pipeline_tutorial.md
heading_stack: <root> -> Pipelines for inference -> Pipeline usage -> Parameters -> Device
---
### Device

If you use `device=n`, the pipeline automatically puts the model on the specified device.
This will work regardless of whether you are using PyTorch or Tensorflow.

```py
transcriber = pipeline(model="openai/whisper-large-v2", device=0)
```

If the model is too large for a single GPU and you are using PyTorch, you can set `device_map="auto"` to automatically 
determine how to load and store the model weights. Using the `device_map` argument requires the 🤗 [Accelerate](https://huggingface.co/docs/accelerate)
package:

```bash
pip install --upgrade accelerate
```

The following code automatically loads and stores model weights across devices:

```py
transcriber = pipeline(model="openai/whisper-large-v2", device_map="auto")
```

Note that if  `device_map="auto"` is passed, there is no need to add the argument `device=device` when instantiating your `pipeline` as you may encounter some unexpected behavior!

