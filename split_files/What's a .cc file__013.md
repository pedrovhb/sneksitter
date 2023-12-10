---
file: /home/pedro/Documents/chatgpt_export/Markdown/What's a .cc file_.md
heading_stack: <root> -> ffae1199-e3d7-428d-bef2-0ba6bdef3246 -> System -> 7fc83a87-2a74-4a2a-b7b7-70ee3febc9b6 -> System -> aaa2d2a3-eb22-4a1a-8055-b0dcebc34ecf -> User -> 4172cd3e-c949-4ea5-b502-f16fd8f33ffc -> Assistant -> aaa244ab-682a-4ecb-856a-c9d2751f02b9 -> User -> 77c43e1a-6196-4e4b-bd71-67739bebae87 -> Assistant -> Step 1: C-Compatible API
---
### Step 1: C-Compatible API

Here is a possible `c_api.h` header with wrapper functions for the provided C++ code:

```c
#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>

int c_read_pfm(const char* filename, float** pixels, uint32_t* xsize, uint32_t* ysize);
int c_encode_jxl_oneshot(const float* pixels, uint32_t xsize, uint32_t ysize, uint8_t** compressed, uint32_t* compressed_size);
int c_write_file(const uint8_t* compressed, uint32_t compressed_size, const char* filename);

#ifdef __cplusplus
}
#endif
```

The corresponding `c_api.cpp` file would look like this:

```cpp
#include "c_api.h"
#include <vector>
#include "your_c++_code_file.h" // Include your existing C++ code here

int c_read_pfm(const char* filename, float** pixels, uint32_t* xsize, uint32_t* ysize) {
    std::vector<float> cpp_pixels;
    if(!ReadPFM(filename, &cpp_pixels, xsize, ysize)) return -1;
    *pixels = (float*) malloc(cpp_pixels.size() * sizeof(float));
    std::copy(cpp_pixels.begin(), cpp_pixels.end(), *pixels);
    return 0;
}

int c_encode_jxl_oneshot(const float* pixels, uint32_t xsize, uint32_t ysize, uint8_t** compressed, uint32_t* compressed_size) {
    std::vector<float> cpp_pixels(pixels, pixels + xsize * ysize * 3);
    std::vector<uint8_t> cpp_compressed;
    if(!EncodeJxlOneshot(cpp_pixels, xsize, ysize, &cpp_compressed)) return -1;
    *compressed_size = cpp_compressed.size();
    *compressed = (uint8_t*) malloc(*compressed_size);
    std::copy(cpp_compressed.begin(), cpp_compressed.end(), *compressed);
    return 0;
}

int c_write_file(const uint8_t* compressed, uint32_t compressed_size, const char* filename) {
    std::vector<uint8_t> cpp_compressed(compressed, compressed + compressed_size);
    return WriteFile(cpp_compressed, filename) ? 0 : -1;
}
```

