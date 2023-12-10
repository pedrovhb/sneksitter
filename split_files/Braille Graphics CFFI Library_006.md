---
file: /home/pedro/Documents/chatgpt_export/Markdown/Braille Graphics CFFI Library.md
heading_stack: <root> -> b0cd4ccf-b58a-4555-9f13-6b1a31814d25 -> System -> 5a574436-e9d1-4b97-a272-d099a8dccb99 -> System -> aaa20d14-8506-4527-a842-e8b226e754d5 -> User
---
# User

We'll be practical and develop a useful CFFI bound library for writing some performance sensitive code in C and enjoying the benefits of calling it from Python.

For now, we'll lay down the groundwork and theoretical basis, as well as exploring different algorithms to achieve our goal.

The goal is to create a library which allows creating a sort of "dot matrix" made up of braille characters to create and display any sort of drawing in the terminal, made up of the braille characters.

To do this, we'll need to brush up on our knowledge of how braille works in Unicode, and explore the problem space to come up with elegant, efficient algorithms for calculating the characters we'll need given a data structure representing a 2D grid of dots. We'll think it through in a very low level, exploring bitwise operations and how global coordinates in a canvas can be translated into local coordinates for the bits that should be set to make up an individual character, and the position of each character given the canvas width and height. This is a non-trivial problem which warrants exploring in detail and perhaps tentatively prototyping or planning multiple possible approaches for. We'll think about what math and classic algorithms can contribute to this specific problem.

To start with, please explain the task to verify your understanding, and ask any questions you might have that would help clarify it and settle on a solid direction.

[child ⬇️](#52f2c2a1-f4d8-4c75-a363-e17d0de117dc)

---

(main branch ⎇)
###### 52f2c2a1-f4d8-4c75-a363-e17d0de117dc
[parent ⬆️](#aaa20d14-8506-4527-a842-e8b226e754d5)
