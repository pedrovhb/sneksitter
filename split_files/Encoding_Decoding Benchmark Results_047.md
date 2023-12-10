---
file: /home/pedro/Documents/chatgpt_export/Markdown/Encoding_Decoding Benchmark Results.md
heading_stack: <root> -> 45bfa0f9-0280-4536-84fe-9f5a2b886748 -> System -> 6e6dc52e-87cd-443f-8455-8f3b2627c1a5 -> System -> aaa2d7d6-5705-4351-a4b5-6ac5b9bb328d -> User -> 2fb2df16-e3b9-43e8-b679-167cac98874e -> Assistant -> 99cabd56-53c1-4d29-95a7-64a236319ddf -> Tool -> 6e23f93f-78cb-4931-95c5-1a03ade96cc2 -> Assistant -> 6417ee72-c53a-491c-b535-4ee25c0edae1 -> Tool -> 196bf9c5-4a6e-4346-8dee-a0640c7dc5c2 -> Assistant -> aaa2ab41-acb8-41a3-b1d0-b8ec666f58a5 -> User -> e26c263d-ac9c-47fd-aa9a-583f3b0038e7 -> Assistant -> URL Encoding (Percent Encoding) -> HTML Entity Encoding -> Quoted-Printable -> Uuencoding -> Ascii85 -> BinHex -> yEnc -> MIME Encoding -> Custom Encoding Schemes -> aaa2624b-ce6d-47fc-a9f8-ff22012ba9a1 -> User -> 3f70515d-968c-41f2-b4af-5f16bd1589f1 -> Assistant -> URL Encoding (Percent Encoding) -> HTML Entity Encoding -> Quoted-Printable -> Uuencoding -> Ascii85 -> Custom Encoding Schemes -> aaa20384-524c-408d-bf28-28bc2e403bb5 -> User -> 3db02b8b-27a9-400f-97c5-232faec839a2 -> Assistant -> c756a8dd-1a33-4d23-9093-ab916a8270f6 -> Tool -> 936f481b-229b-4af3-8eeb-5711b1cc4b52 -> Assistant
---
# Assistant

```python
# Re-importing the required libraries and redefining functions for benchmarking
import base64
import timeit
import matplotlib.pyplot as plt
import pandas as pd
from urllib.parse import quote, unquote
import html
import quopri
import uu
from io import BytesIO

# Redefining functions for baseNN encoding/decoding
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

# Defining functions for alternative encoding schemes
def encode_url(data: str) -> str:
    return quote(data)

def decode_url(data: str) -> str:
    return unquote(data)

def encode_html(data: str) -> str:
    return html.escape(data)

def decode_html(data: str) -> str:
    return html.unescape(data)

def encode_quopri(data: bytes) -> bytes:
    return quopri.encodestring(data)

def decode_quopri(data: bytes) -> bytes:
    return quopri.decodestring(data)

def encode_uu(data: bytes) -> bytes:
    output = BytesIO()
    uu.encode(BytesIO(data), output)
    return output.getvalue()

def decode_uu(data: bytes) -> bytes:
    output = BytesIO()
    uu.decode(BytesIO(data), output)
    return output.getvalue()

# Data for benchmarking
test_data = b"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sed odio eu ligula aliquam fringilla."
test_data_str = test_data.decode('utf-8')

# Benchmark settings
functions_to_benchmark = {
    'encode_base64': encode_base64,
    'decode_base64': decode_base64,
    'encode_base32': encode_base32,
    'decode_base32': decode_base32,
    'encode_base16': encode_base16,
    'decode_base16': decode_base16,
    'encode_base85': encode_base85,
    'decode_base85': decode_base85,
    'encode_url': encode_url,
    'decode_url': decode_url,
    'encode_html': encode_html,
    'decode_html': decode_html,
    'encode_quopri': encode_quopri,
    'decode_quopri': decode_quopri,
    'encode_uu': encode_uu,
    'decode_uu': decode_uu
}

num_repeats = 1000
benchmark_results = {}

# Run benchmarks
for func_name, func in functions_to_benchmark.items():
    if 'encode' in func_name:
        if func_name in ['encode_url', 'encode_html']:
            benchmark_results[func_name] = timeit.timeit(lambda: func(test_data_str), number=num_repeats)
        else:
            benchmark_results[func_name] = timeit.timeit(lambda: func(test_data), number=num_repeats)
    else:  # decode
        if func_name in ['decode_url', 'decode_html']:
            encoded_data = func(test_data_str)
            benchmark_results[func_name] = timeit.timeit(lambda: func(encoded_data), number=num_repeats)
        else:
            encoded_data = func(test_data)
            benchmark_results[func_name] = timeit.timeit(lambda: func(encoded_data), number=num_repeats)

# Convert the results to a DataFrame for easier plotting and analysis later
df_benchmark_results = pd.DataFrame(list(benchmark_results.items()), columns=['Function', 'Time (s)'])
df_benchmark_results.sort_values('Time (s)', inplace=True)

df_benchmark_results
```

[child ⬇️](#fbb68eb4-8365-4154-8cfb-7bb7aa582560)

---

(main branch ⎇)
###### fbb68eb4-8365-4154-8cfb-7bb7aa582560
[parent ⬆️](#936f481b-229b-4af3-8eeb-5711b1cc4b52)
