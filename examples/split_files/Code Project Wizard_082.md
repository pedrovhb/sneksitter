# User

1. Something able to store embeddings and metadata like exif, md5, and file location on disk. Perhaps txtai, or a combination of hnswlib or annoy and SQLite.

2. I'm guessing cosine similarity, through kmeans via one of the libraries mentioned above

3. Something like

```
$ imseek index ~/Pictures
<rich animated progress bar with rich.Live>
Done, 1337 files indexed!

$ imseek "black dog in the park" --after 2023 -b 2023-07-20 -n 15
<rich but simple machine-parsable listing of top 15 matching files and their scores>

$imseek example_image.png --camera Canon
<same output format, highest similarity to given image filtered by exif info fields indicating camera and containing Canon, case insensitive>
```

4. Maybe exiv2 or some exif library with a nice python interface 

[child ⬇️](#4c5eff3e-6c36-42cd-b879-0a7ebe6ec36f)

---

(main branch ⎇)
###### 4c5eff3e-6c36-42cd-b879-0a7ebe6ec36f
[parent ⬆️](#aaa24628-c65b-42bd-9b96-43164c4415f8)
