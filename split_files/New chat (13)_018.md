---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (13).md
heading_stack: <root> -> e10c2f77-8080-42ec-af42-a3887b76def9 -> System -> 83d65b0b-2baa-449b-b718-d2b8cc114684 -> System -> aaa2bcea-4758-4eec-8700-5edd0f828f38 -> User -> Goals: -> C Code: -> Python CFFI Code: -> Testing: -> a9dd4a4e-dd38-41a0-8a1c-7cd1ec1322d7 -> Assistant -> aaa2c495-7caa-41da-b556-f4724b700e29 -> User -> 1cea3620-b3b0-4586-a8dd-2b9526fa49a2 -> Assistant -> c4f3cfd4-3397-44d1-ae02-556aa8cae661 -> Assistant
---
# Assistant

```python
# Writing the C code to simulate the sensor data generator

c_code = """
#include <stdlib.h>
#include <math.h>
#include <time.h>

// Sensor structure
typedef struct {
    double freq_x;
    double freq_y;
    double freq_z;
    double time;
} Sensor;

// Initialize sensor
void* init_sensor(double freq_x, double freq_y, double freq_z) {
    Sensor* sensor = (Sensor*)malloc(sizeof(Sensor));
    sensor->freq_x = freq_x;
    sensor->freq_y = freq_y;
    sensor->freq_z = freq_z;
    sensor->time = 0;
    srand(time(0)); // Initialize random seed for noise
    return (void*)sensor;
}

// Fetch next sensor data
void next_sensor_data(void *handle, double *x, double *y, double *z) {
    Sensor* sensor = (Sensor*)handle;
    double noise_x = ((double)rand() / RAND_MAX) * 0.1;
    double noise_y = ((double)rand() / RAND_MAX) * 0.1;
    double noise_z = ((double)rand() / RAND_MAX) * 0.1;
    *x = sin(sensor->freq_x * sensor->time) + noise_x;
    *y = cos(sensor->freq_y * sensor->time) + noise_y;
    *z = sin(sensor->freq_z * sensor->time) + noise_z;
    sensor->time += 0.1;
}

// Free sensor
void free_sensor(void *handle) {
    free(handle);
}
"""

# Save the C code into a file
with open("sensor.c", "w") as f:
    f.write(c_code)

# Compile the C code into a shared library (.so file)
!gcc -shared -o sensor.so -fPIC sensor.c -lm
```

[child ⬇️](#7ac5f3e2-8a76-4b15-af32-416bc967f33c)

---

(main branch ⎇)
###### 7ac5f3e2-8a76-4b15-af32-416bc967f33c
[parent ⬆️](#c4f3cfd4-3397-44d1-ae02-556aa8cae661)
