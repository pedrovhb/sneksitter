---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (9).md
heading_stack: <root> -> 62554ab3-2da7-44bf-904f-c2673716efe5 -> System -> 8d1d4b3c-44b1-4d04-96b3-550c080648bf -> System -> aaa24b13-f6aa-4dc9-860e-54f6ac6eea4e -> User -> f71aad2c-c170-4a64-8858-305c82518d98 -> Assistant -> 250514eb-8a60-408d-a6d4-f10333f29402 -> Tool -> 9dec960c-19d4-405f-bd56-76c7191a2b75 -> Assistant -> d30d6e7e-14cd-4e34-869d-a7993f5f3df2 -> Tool -> ef70ce7e-d235-4852-b0f4-4f4169b38653 -> Assistant -> f2385be4-7700-476e-8ea6-797a5813879a -> Tool -> f760029f-ba0a-45ac-aa6b-af62b52e9e25 -> Assistant -> a6533d90-0e2b-458e-87ec-d4d87d8e0c12 -> Assistant -> 8eccbbf6-52e2-4f7d-a6ca-b6ed3ce56644 -> Tool -> 3aa50e6b-dee1-489d-854e-d9f83ce1cae7 -> Assistant -> aaa29438-7719-492c-8768-88d0be83ed13 -> User -> ce115e2d-72e7-4e7d-8bfd-f6870442b902 -> Assistant -> 72038b2b-0138-4680-842f-4eb8c7c8ae44 -> Tool -> aaa25e37-97b9-4c3a-bb5c-30f81414dcaf -> User -> a70bc29a-c84c-4996-b2d6-32897163bc87 -> Assistant -> Braille Unicode Code Points
---
### Braille Unicode Code Points

Braille Unicode characters are encoded from U+2800 to U+28FF. Each Braille character can be thought of as a 2x4 grid:

```
⠃
⡃
⢃
⣃
```

The dots in this grid are numbered from 1 to 8:

```
1  4
2  5
3  6
7  8
```

The Braille Unicode character for an empty grid is U+2800 (`⠄`). Each dot adds a specific value to this base code point:

- Dot 1: 1
- Dot 2: 2
- Dot 3: 4
- Dot 4: 8
- Dot 5: 16
- Dot 6: 32
- Dot 7: 64
- Dot 8: 128

To represent a specific pattern, you add the values corresponding to the dots you want to light up to the base code point (U+2800).
