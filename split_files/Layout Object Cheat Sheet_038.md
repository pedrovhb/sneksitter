---
file: /home/pedro/Documents/chatgpt_export/Markdown/Layout Object Cheat Sheet.md
heading_stack: <root> -> 1f15d2ca-65e8-455c-b617-eada3a50d984 -> System -> a46ba8e6-e266-4af7-bdb9-05708a267308 -> System -> aaa2f88e-481e-4d89-aced-3cda388b92d1 -> User -> 7a63f637-a1f4-4a1a-bfb9-206cd3a3a835 -> Assistant -> 34809d24-bdaa-495f-ab14-fe84ac12228c -> Tool -> a1fa7c8a-f8d2-43c7-a4e5-b471af4f90cd -> Assistant -> 722a93e2-0b4b-4d34-ba86-b4786ffcb230 -> Tool -> b603ced7-0ac2-4271-ba3e-5f4d0f5e66f0 -> Assistant -> cc840f0a-8cf3-4d48-9691-7d7553a41651 -> Tool -> a944f953-b42f-4311-bc28-136aa77c3d6a -> Assistant -> aaa261c4-bade-4fb5-9148-965066172375 -> User -> e1438703-177f-4dcd-94c8-0d1565b17299 -> Assistant -> aaa29fff-c9db-4654-be04-c52171747a49 -> User -> 75640d6c-055d-4bc0-98a0-e55c8a8d7135 -> Assistant -> 9d40620b-df3a-4b20-bb18-86037f14408b -> Tool -> 94c63589-57d2-4742-b438-216467b95db6 -> Assistant -> 8c043996-ac0d-40da-b930-4f8a7794b864 -> Tool -> 05f6be4d-6760-4715-aaca-cd429c0a08ef -> Assistant -> 4ddf54d9-96c7-4007-9140-de2e7963d0d9 -> Tool
---
# Tool

```python
# Layout【32†¶】

Rich offers a 【33†Layout】 class which can be used to divide the screen area in to parts, where each part may contain independent content. It can be used with 【34†Live Display】 to create full-screen “applications” but may be used standalone.

To see an example of a Layout, run the following from the command line:

    python -m rich.layout

## Creating layouts【21†¶】

To define a layout, construct a Layout object and print it:

    from rich import print
    from rich.layout import Layout

    layout = Layout()
    print(layout)

This will draw a box the size of the terminal with some information regarding the layout. The box is a “placeholder” because we have yet to add any content to it. Before we do that, let’s create a more interesting layout by calling the 【35†split_column()】 method to divide the layout in to two sub-layouts:

    layout.split_column(
        Layout(name="upper"),
        Layout(name="lower")
    )
    print(layout)

This will divide the terminal screen in to two equal sized portions, one on top of the other. The `name` attribute is an internal identifier we can use to look up the sub-layout later. Let’s use that to create another split, this time we will call 【36†split_row()】 to split the lower layout in to a row of two sub-layouts:

    layout["lower"].split_row(
        Layout(name="left"),
        Layout(name="right"),
    )
    print(layout)

You should now see the screen area divided in to 3 portions; an upper half and a lower half that is split in to two quarters.

    ╭─────────────────────────────── 'upper' (84 x 13) ────────────────────────────────╮
    │                                                                                  │
    │                                                                                  │
    │                                                                                  │
    │                                                                                  │
    │                                                                                  │
    │          {'size': None, 'minimum_size': 1, 'ratio': 1, 'name': 'upper'}          │
    │                                                                                  │
    │                                                                                  │
    │                                                                                  │
    │                                                                                  │
    │                                                                                  │
    ╰──────────────────────────────────────────────────────────────────────────────────╯
    ╭─────────── 'left' (42 x 14) ───────────╮╭────────── 'right' (42 x 14) ───────────╮
    │                                        ││                                        │
    │                                        ││                                        │
    │                                        ││                                        │
    │         {                              ││         {                              │
    │             'size': None,              ││             'size': None,              │
    │             'minimum_size': 1,         ││             'minimum_size': 1,         │
    │             'ratio': 1,                ││             'ratio': 1,                │
    │             'name': 'left'             ││             'name': 'right'            │
    │         }                              ││         }                              │
    │                                        ││                                        │
    │                                        ││                                        │
    │                                        ││                                        │
    ╰────────────────────────────────────────╯╰────────────────────────────────────────╯

You can continue to call split() in this way to create as many parts to the screen as you wish.

## Setting renderables【22†¶】

The first position argument to `Layout` can be any Rich renderable, which will be sized to fit within the layout’s area. Here’s how we might divide the “right” layout in to two panels:

    from rich.panel import Panel

    layout["right"].split(
        Layout(Panel("Hello")),
        Layout(Panel("World!"))
    )

You can also call 【37†update()】 to set or replace the current renderable:

    layout["left"].update(
        "The mystery of life isn't a problem to solve, but a reality to experience."
    )
    print(layout)

## Fixed size【23†¶】

You can set a layout to use a fixed size by setting the `size` argument on the Layout constructor or by setting the attribute. Here’s an example:

    layout["upper"].size = 10
    print(layout)

This will set the upper portion to be exactly 10 rows, no matter the size of the terminal. If the parent layout is horizontal rather than vertical, then the size applies to the number of characters rather that rows.

## Ratio【24†¶】

In addition to a fixed size, you can also make a flexible layout setting the `ratio` argument on the constructor or by assigning to the attribute. The ratio defines how much of the screen the layout should occupy in relation to other layouts. For example, let’s reset the size and set the ratio of the upper layout to 2:

    layout["upper"].size = None
    layout["upper"].ratio = 2
    print(layout)

This makes the top layout take up two thirds of the space. This is because the default ratio is 1, giving the upper and lower layouts a combined total of 3. As the upper layout has a ratio of 2, it takes up two thirds of the space, leaving the remaining third for the lower layout.

A layout with a ratio set may also have a minimum size to prevent it from getting too small. For instance, here’s how we could set the minimum size of the lower sub-layout so that it won’t shrink beyond 10 rows:

    layout["lower"].minimum_size = 10

## Visibility【25†¶】

You can make a layout invisible by setting the `visible` attribute to False. Here’s an example:

    layout["upper"].visible = False
```

[child ⬇️](#5455c438-1e5e-4941-a013-7522739e2556)

---

(main branch ⎇)
###### 5455c438-1e5e-4941-a013-7522739e2556
[parent ⬆️](#4ddf54d9-96c7-4007-9140-de2e7963d0d9)
