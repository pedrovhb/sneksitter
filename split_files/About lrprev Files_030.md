---
file: /home/pedro/Documents/chatgpt_export/Markdown/About lrprev Files.md
heading_stack: <root> -> 544444bd-6b16-4eed-af43-98fa3a69b615 -> System -> 86c13176-225a-4bd5-97f5-f991207f5a43 -> System -> aaa2fe2d-7be2-4569-b4c4-7213cdb836d2 -> User -> 0914aa28-090b-435f-9ca1-8f7c0c62dc03 -> Assistant -> aaa20132-873b-43c5-ab60-59f9c8d01e05 -> User -> f79f78e3-7957-4083-89b1-e600a0c5019c -> Assistant -> aaa270bf-98d9-4562-a7d0-c101b527dd39 -> User -> 4cbd0c39-1237-4a7c-ab24-4e28585e6283 -> Assistant -> aaa2a778-f433-430a-81e3-453effcca283 -> User -> ddbfa15c-8c01-4a83-bdfe-76fdae4b5c23 -> Assistant -> b7e3a3d0-43f3-4493-8902-261673d3eda6 -> Tool -> 923beb7c-8b2b-49ba-9238-511fe70f8ad7 -> Assistant -> aaa2a102-75b1-4902-b8e8-ccb2dcee962f -> User -> dc8ece6b-164d-4295-b4c0-59e52c77fad9 -> Assistant -> dbbd77b9-cb64-40b0-ae21-38ccc7f89f46 -> Assistant
---
# Assistant

```python
# Function to extract JPEG image from a byte array starting from a given offset
def extract_jpeg(data, start_offset):
    end_marker = b'\xFF\xD9'
    end_offset = data.find(end_marker, start_offset)
    if end_offset == -1:
        return None, None
    end_offset += 2  # Include the end marker
    return data[start_offset:end_offset], end_offset

# Function to extract BMP image from a byte array starting from a given offset
def extract_bmp(data, start_offset):
    # BMP size is stored in bytes 2-6 from the start offset (little-endian)
    bmp_size = int.from_bytes(data[start_offset + 2:start_offset + 6], byteorder='little')
    end_offset = start_offset + bmp_size
    return data[start_offset:end_offset], end_offset

# Initialize containers for extracted images
extracted_images = {}

# Extract JPEG image
jpeg_data, _ = extract_jpeg(file_content, 608)
if jpeg_data:
    extracted_images['JPEG'] = jpeg_data

# Extract BMP image
bmp_data, _ = extract_bmp(file_content, 24763)
if bmp_data:
    extracted_images['BMP'] = bmp_data

# Write extracted images to files for verification
extracted_files = {}
for img_format, img_data in extracted_images.items():
    output_file_path = f'/mnt/data/extracted_{img_format.lower()}.img'
    with open(output_file_path, 'wb') as f:
        f.write(img_data)
    extracted_files[img_format] = output_file_path

extracted_files
```

[child ⬇️](#dfa27d3c-5c48-403b-a2c3-03c8ab38d2ab)

---

(main branch ⎇)
###### dfa27d3c-5c48-403b-a2c3-03c8ab38d2ab
[parent ⬆️](#dbbd77b9-cb64-40b0-ae21-38ccc7f89f46)
