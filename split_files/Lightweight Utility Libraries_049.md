---
file: /home/pedro/Documents/chatgpt_export/Markdown/Lightweight Utility Libraries.md
heading_stack: <root> -> db50d90f-fdf2-44f2-925b-ae66fdd7cfa0 -> System -> f462c4f4-0c7f-47fb-9237-a7d0ddbed997 -> System -> aaa26b54-0d2d-44d8-a646-0310427be0eb -> User -> ddb3dc5b-752e-4561-a939-b3de8b08d32f -> Assistant -> Data Manipulation and Analysis -> aaa205bc-d11e-4621-bc91-c8700e9b03ed -> User -> 945429c9-250d-41f7-b62d-d659a26c2d87 -> Assistant -> Data Manipulation -> Text and Parsing -> Networking -> File Handling -> Testing and Debugging -> Asynchronous Programming -> Functional Programming -> Code Analysis and Refactoring -> Miscellaneous -> aaa28fee-d697-42e3-bbe0-0e326b045dd7 -> User -> 03cd3de2-6edf-4ea6-98f5-168547563566 -> Assistant -> c8193452-a094-4568-8208-baae59e02bea -> Tool -> bc3074a5-dd96-498e-993d-f86abd592ee2 -> Assistant -> aaa263a5-33b9-47d9-a7f8-7a9b64b887a4 -> User -> a2faf051-4d79-41df-ae50-98d4779dfa98 -> Assistant -> Data Manipulation with `toolz` -> 44888ccd-cc10-41b4-8740-17f5ea12b035 -> Assistant -> 3e278eb5-5bed-4c77-a192-5cca5affdf4d -> Tool -> 432415d6-6abe-4b73-ab3e-eceb217b35b7 -> Assistant -> Text and Parsing with `parse` -> 16a0f14c-d434-4b10-ae5d-aa81e8846ee2 -> Assistant -> 05bde113-80ef-45aa-824a-bf23f4fbf95f -> Tool -> 395b9a62-27b9-4e21-9f0c-9a36587c9552 -> Assistant -> Programming Utilities with `wrapt`
---
### Programming Utilities with `wrapt`

`wrapt` is a library for decorators, wrappers, and monkey patching. Here's a quick example to demonstrate a timing decorator.

```python
import wrapt
import time

@wrapt.decorator
def timing_decorator(wrapped, instance, args, kwargs):
    start_time = time.time()
    result = wrapped(*args, **kwargs)
    end_time = time.time()
    print(f"Elapsed time: {end_time - start_time:.4f} seconds")
    return result

@timing_decorator
def slow_function(duration):
    time.sleep(duration)
    return "Done"
```

Executing this to measure the elapsed time of a slow function.

[child ⬇️](#23bddd27-f0c4-482e-8cd1-a1942fde7165)

---

(main branch ⎇)
###### 23bddd27-f0c4-482e-8cd1-a1942fde7165
[parent ⬆️](#395b9a62-27b9-4e21-9f0c-9a36587c9552)
