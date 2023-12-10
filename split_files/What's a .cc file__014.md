---
file: /home/pedro/Documents/chatgpt_export/Markdown/What's a .cc file_.md
heading_stack: <root> -> ffae1199-e3d7-428d-bef2-0ba6bdef3246 -> System -> 7fc83a87-2a74-4a2a-b7b7-70ee3febc9b6 -> System -> aaa2d2a3-eb22-4a1a-8055-b0dcebc34ecf -> User -> 4172cd3e-c949-4ea5-b502-f16fd8f33ffc -> Assistant -> aaa244ab-682a-4ecb-856a-c9d2751f02b9 -> User -> 77c43e1a-6196-4e4b-bd71-67739bebae87 -> Assistant -> Step 1: C-Compatible API -> Step 2: CFFI Binding
---
### Step 2: CFFI Binding

Here is how you can use CFFI to interact with this C API:

First, install cffi:

```bash
pip install cffi
```

Now, the Python code:

```python
from cffi import FFI

ffi = FFI()

ffi.cdef("""
    int c_read_pfm(const char* filename, float** pixels, uint32_t* xsize, uint32_t* ysize);
    int c_encode_jxl_oneshot(const float* pixels, uint32_t xsize, uint32_t ysize, uint8_t** compressed, uint32_t* compressed_size);
    int c_write_file(const uint8_t* compressed, uint32_t compressed_size, const char* filename);
""")

# Assuming that your compiled C++ library is named "example.so"
lib = ffi.dlopen("example.so")

# Now you can use `lib.c_read_pfm`, `lib.c_encode_jxl_oneshot`, and `lib.c_write_file` in your Python code.
```

Note that you'll need to compile your C++ code into a shared library (`.so` or `.dll` depending on your OS) that the CFFI can then load. The details of this would depend on your build system and compiler settings.

---
