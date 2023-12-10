---
file: /home/pedro/Documents/chatgpt_export/Markdown/Encoding_Decoding Benchmark Results.md
heading_stack: <root> -> 45bfa0f9-0280-4536-84fe-9f5a2b886748 -> System -> 6e6dc52e-87cd-443f-8455-8f3b2627c1a5 -> System -> aaa2d7d6-5705-4351-a4b5-6ac5b9bb328d -> User -> 2fb2df16-e3b9-43e8-b679-167cac98874e -> Assistant
---
# Assistant

```python
# Importing required libraries for benchmarking and plotting
import base64
import timeit
import matplotlib.pyplot as plt
import pandas as pd

# Functions to benchmark
def encode_base64(data: bytes) -> bytes:
    return base64.b64encode(data)

def decode_base64(data: bytes) -> bytes:
    return base64.b64decode(data)

def encode_base32(data: bytes) -> bytes:
    return base64.b32encode(data)

def decode_base32(data: bytes) -> bytes:
    return base64.b32decode(data)

def encode_base16(data: bytes) -> bytes:
    return base64.b16encode(data)

def decode_base16(data: bytes) -> bytes:
    return base64.b16decode(data)

def encode_base85(data: bytes) -> bytes:
    return base64.b85encode(data)

def decode_base85(data: bytes) -> bytes:
    return base64.b85decode(data)

# Data for benchmarking
test_data = b"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sed odio eu ligula aliquam fringilla."
data_dict = {
    'base64_encoded': encode_base64(test_data),
    'base32_encoded': encode_base32(test_data),
    'base16_encoded': encode_base16(test_data),
    'base85_encoded': encode_base85(test_data)
}

# Benchmark settings
functions_to_benchmark = {
    'encode_base64': encode_base64,
    'decode_base64': decode_base64,
    'encode_base32': encode_base32,
    'decode_base32': decode_base32,
    'encode_base16': encode_base16,
    'decode_base16': decode_base16,
    'encode_base85': encode_base85,
    'decode_base85': decode_base85
}

num_repeats = 1000
benchmark_results = {}

# Run benchmarks
for func_name, func in functions_to_benchmark.items():
    if 'encode' in func_name:
        benchmark_results[func_name] = timeit.timeit(lambda: func(test_data), number=num_repeats)
    else:  # decode
        encoded_data_key = f"{func_name[7:]}_encoded"  # Extract the encoding type from the function name
        benchmark_results[func_name] = timeit.timeit(lambda: func(data_dict[encoded_data_key]), number=num_repeats)

# Convert the results to a DataFrame for easier plotting and analysis later
df_benchmark_results = pd.DataFrame(list(benchmark_results.items()), columns=['Function', 'Time (s)'])
df_benchmark_results.sort_values('Time (s)', inplace=True)

df_benchmark_results
```

[child ⬇️](#99cabd56-53c1-4d29-95a7-64a236319ddf)

---

(main branch ⎇)
###### 99cabd56-53c1-4d29-95a7-64a236319ddf
[parent ⬆️](#2fb2df16-e3b9-43e8-b679-167cac98874e)
