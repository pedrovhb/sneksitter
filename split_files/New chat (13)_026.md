---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (13).md
heading_stack: <root> -> e10c2f77-8080-42ec-af42-a3887b76def9 -> System -> 83d65b0b-2baa-449b-b718-d2b8cc114684 -> System -> aaa2bcea-4758-4eec-8700-5edd0f828f38 -> User -> Goals: -> C Code: -> Python CFFI Code: -> Testing: -> a9dd4a4e-dd38-41a0-8a1c-7cd1ec1322d7 -> Assistant -> aaa2c495-7caa-41da-b556-f4724b700e29 -> User -> 1cea3620-b3b0-4586-a8dd-2b9526fa49a2 -> Assistant -> c4f3cfd4-3397-44d1-ae02-556aa8cae661 -> Assistant -> 7ac5f3e2-8a76-4b15-af32-416bc967f33c -> Tool -> 1d7338c4-6acf-438a-bfc9-476c82af7f1b -> Assistant -> aaa2513e-fdef-4417-a0f2-c4fed9c61ec1 -> User -> 5ae3b56f-c884-4058-bac4-5c437a191366 -> Assistant
---
# Assistant

```python
from cffi import FFI

# Initialize FFI
ffi = FFI()

# Load the C header declarations
ffi.cdef("""
void* init_sensor(double freq_x, double freq_y, double freq_z);
void next_sensor_data(void *handle, double *x, double *y, double *z);
void free_sensor(void *handle);
""")

# Load the shared library
lib = ffi.dlopen("./sensor.so")

# Python class SensorIterator
class SensorIterator:
    def __init__(self, freq_x: float, freq_y: float, freq_z: float):
        self.handle = lib.init_sensor(freq_x, freq_y, freq_z)
        self.x = ffi.new("double*")
        self.y = ffi.new("double*")
        self.z = ffi.new("double*")

    def __iter__(self):
        return self

    def __next__(self):
        lib.next_sensor_data(self.handle, self.x, self.y, self.z)
        # Assume a stopping condition for demonstration
        if self.x[0] + self.y[0] + self.z[0] > 5:
            lib.free_sensor(self.handle)
            raise StopIteration
        return (self.x[0], self.y[0], self.z[0])

# Testing the SensorIterator
sensor_data = []
sensor_iterator = SensorIterator(1.0, 1.0, 1.0)
for data in sensor_iterator:
    sensor_data.append(data)

sensor_data
```

[child ⬇️](#dfd9290e-a703-4e82-bf1c-827935c5ee39)

---

(main branch ⎇)
###### dfd9290e-a703-4e82-bf1c-827935c5ee39
[parent ⬆️](#5ae3b56f-c884-4058-bac4-5c437a191366)
