---
file: /home/pedro/Documents/chatgpt_export/Markdown/Lightweight Utility Libraries.md
heading_stack: <root> -> db50d90f-fdf2-44f2-925b-ae66fdd7cfa0 -> System -> f462c4f4-0c7f-47fb-9237-a7d0ddbed997 -> System -> aaa26b54-0d2d-44d8-a646-0310427be0eb -> User -> ddb3dc5b-752e-4561-a939-b3de8b08d32f -> Assistant -> Data Manipulation and Analysis -> aaa205bc-d11e-4621-bc91-c8700e9b03ed -> User -> 945429c9-250d-41f7-b62d-d659a26c2d87 -> Assistant -> Data Manipulation -> Text and Parsing -> Networking -> File Handling -> Testing and Debugging -> Asynchronous Programming -> Functional Programming -> Code Analysis and Refactoring -> Miscellaneous -> aaa28fee-d697-42e3-bbe0-0e326b045dd7 -> User -> 03cd3de2-6edf-4ea6-98f5-168547563566 -> Assistant -> c8193452-a094-4568-8208-baae59e02bea -> Tool -> bc3074a5-dd96-498e-993d-f86abd592ee2 -> Assistant -> aaa263a5-33b9-47d9-a7f8-7a9b64b887a4 -> User -> a2faf051-4d79-41df-ae50-98d4779dfa98 -> Assistant
---
# Assistant

Certainly, I'll start by showcasing some of the most interesting features from the installed libraries. Due to the variety of libraries, I'll categorize the demos into a few buckets: data manipulation, text and parsing, and programming utilities.

### Data Manipulation with `toolz`

First up is `toolz`, a library for functional programming in Python that makes data manipulation more convenient. Let's start by demonstrating the `groupby` and `valfilter` functions.

```python
from toolz import groupby, valfilter

# Data
fruits = ['apple', 'banana', 'cherry', 'date']

# Group by length
grouped_by_length = groupby(len, fruits)

# Filter by value
filtered_fruits = valfilter(lambda x: len(x) > 1, grouped_by_length)
```

Executing this to see the output.

[child ⬇️](#44888ccd-cc10-41b4-8740-17f5ea12b035)

---

(main branch ⎇)
###### 44888ccd-cc10-41b4-8740-17f5ea12b035
[parent ⬆️](#a2faf051-4d79-41df-ae50-98d4779dfa98)