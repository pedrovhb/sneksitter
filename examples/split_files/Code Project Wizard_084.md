# Assistant

```python
# Update the custom example YAML specification based on the user's answers.

# Update the data storage mechanism
custom_example['data_storage'] = ['txtai', 'hnswlib or annoy', 'SQLite']

# Update the algorithms for image similarity
custom_example['image_similarity_algorithm'] = ['Cosine Similarity', 'KMeans']

# Update the CLI sub-commands and options
custom_example['cli_commands'] = {
    'index': {
        'description': 'Indexes images in a given directory',
        'usage': '$ imseek index ~/Pictures'
    },
    'text_search': {
        'description': 'Searches images based on text query',
        'usage': '$ imseek "black dog in the park" --after 2023 -b 2023-07-20 -n 15'
    },
    'image_search': {
        'description': 'Searches images based on a sample image',
        'usage': '$ imseek example_image.png --camera Canon'
    }
}

# Update the metadata extraction methods
custom_example['metadata_extraction'] = ['exiv2', 'Python EXIF library']

# Save the updated custom example specification to a YAML file
with open(custom_example_file_path, 'w') as f:
    yaml.dump(custom_example, f)

custom_example_file_path
```

[child ⬇️](#1d1d8a64-b577-4e98-827e-a3a08976b5c5)

---

(main branch ⎇)
###### 1d1d8a64-b577-4e98-827e-a3a08976b5c5
[parent ⬆️](#4c5eff3e-6c36-42cd-b879-0a7ebe6ec36f)
