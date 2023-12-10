---
file: /home/pedro/Documents/chatgpt_export/Markdown/Layout Object Cheat Sheet.md
heading_stack: <root> -> 1f15d2ca-65e8-455c-b617-eada3a50d984 -> System -> a46ba8e6-e266-4af7-bdb9-05708a267308 -> System -> aaa2f88e-481e-4d89-aced-3cda388b92d1 -> User -> 7a63f637-a1f4-4a1a-bfb9-206cd3a3a835 -> Assistant -> 34809d24-bdaa-495f-ab14-fe84ac12228c -> Tool -> a1fa7c8a-f8d2-43c7-a4e5-b471af4f90cd -> Assistant -> 722a93e2-0b4b-4d34-ba86-b4786ffcb230 -> Tool -> b603ced7-0ac2-4271-ba3e-5f4d0f5e66f0 -> Assistant -> cc840f0a-8cf3-4d48-9691-7d7553a41651 -> Tool -> a944f953-b42f-4311-bc28-136aa77c3d6a -> Assistant -> aaa261c4-bade-4fb5-9148-965066172375 -> User -> e1438703-177f-4dcd-94c8-0d1565b17299 -> Assistant -> aaa29fff-c9db-4654-be04-c52171747a49 -> User -> 75640d6c-055d-4bc0-98a0-e55c8a8d7135 -> Assistant -> 9d40620b-df3a-4b20-bb18-86037f14408b -> Tool -> 94c63589-57d2-4742-b438-216467b95db6 -> Assistant -> 8c043996-ac0d-40da-b930-4f8a7794b864 -> Tool -> 05f6be4d-6760-4715-aaca-cd429c0a08ef -> Assistant -> 4ddf54d9-96c7-4007-9140-de2e7963d0d9 -> Tool -> 5455c438-1e5e-4941-a013-7522739e2556 -> Assistant -> 616ddcf1-86cc-4239-be07-2ec49fa6e498 -> Assistant
---
# Assistant

```yaml
Layout:
  short_description: |
    A class in the Rich library used to divide the terminal screen into sections, each holding independent content.
  long_description: |
    The `Layout` class in the Rich library can be used to create visually appealing terminal interfaces by dividing the terminal screen into multiple sections. Each section can hold independent content, making it easier to organize information in a structured manner.
  usage_explanation: |
    - Create a `Layout` instance.
    - Use methods like `split_column()` or `split_row()` to divide the layout.
    - Access sub-layouts using their name as a key.
    - Update renderables in a layout using `update()` or set them while creating sub-layouts.
    - Control size using `size` and `ratio` attributes, and visibility using the `visible` attribute.
  examples: |
    - Basic Layout:
        from rich import print
        from rich.layout import Layout
        layout = Layout()
        print(layout)
    - Splitting Layout:
        layout.split_column(Layout(name="upper"), Layout(name="lower"))
        layout["lower"].split_row(Layout(name="left"), Layout(name="right"))
    - Setting Renderables:
        from rich.panel import Panel
        layout["right"].split(Layout(Panel("Hello")), Layout(Panel("World!")))
    - Fixed Size:
        layout["upper"].size = 10
    - Ratio:
        layout["upper"].size = None
        layout["upper"].ratio = 2
  use_when_you_need_to:
    - Create structured terminal interfaces.
    - Display multiple pieces of information separately within the same terminal screen.
    - Create interactive terminal applications.
    - Have control over the size and visibility of different sections of the terminal interface.
    - Dynamically update content within a structured layout.
  see_also:
    - Live Display: For creating full-screen terminal applications.
    - Panel: To create bordered boxes around text or other renderables within a layout.
    - Rich renderables: Various renderables that can be used within a layout to display content.
```

[child ⬇️](#aaa20a5a-d1c2-4331-9d2e-324b72585677)

---

(main branch ⎇)
###### aaa20a5a-d1c2-4331-9d2e-324b72585677
[parent ⬆️](#616ddcf1-86cc-4239-be07-2ec49fa6e498)
