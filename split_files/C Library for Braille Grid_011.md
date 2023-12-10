---
file: /home/pedro/Documents/chatgpt_export/Markdown/C Library for Braille Grid.md
heading_stack: <root> -> ec931c03-8f32-457a-8896-06e907d6514d -> System -> 60c8cb8a-5be6-436c-a7a1-cb652f0b1c63 -> System -> aaa235c3-fbbd-4934-8b73-22293c85c582 -> User -> d76e01e6-664a-4b58-a15d-be309aaa9e65 -> Assistant -> 1. **Data Structures:** -> 1.1 Grid Structure: -> 1.2 Bitset:
---
#### 1.2 Bitset:

- A bitset to represent the status (set/unset) of each dot in the Braille grid. Each Braille character can represent 8 dots, so an 8-bit bitset (1 byte) can be used for each character.

```c
typedef unsigned char BrailleChar;
```

