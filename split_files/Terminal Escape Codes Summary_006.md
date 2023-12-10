---
file: /home/pedro/Documents/chatgpt_export/Markdown/Terminal Escape Codes Summary.md
heading_stack: <root> -> 3992efef-506a-4339-a915-da88075a28b4 -> System -> 279db4e3-a725-4c3f-8ad7-66b2e924c4c1 -> System -> aaa2c242-6363-4e75-9e25-2d7833dbdde4 -> User
---
# User

What's missing from the list?

### ANSI Escape Codes for Terminal Control and Cursor Manipulation

#### Cursor Positioning
- Cursor Up by N Cells: `\033[N A`
- Cursor Down by N Cells: `\033[N B`
- Cursor Forward by N Cells: `\033[N C`
- Cursor Back by N Cells: `\033[N D`
- Cursor Next Line by N Lines: `\033[N E`
- Cursor Previous Line by N Lines: `\033[N F`
- Cursor Horizontal Absolute to Column N: `\033[N G`
- Cursor Position to X;Y: `\033[Y;X H` or `\033[Y;X f`
- Cursor Position to Row N: `\033[N d`

#### Cursor Visibility
- Hide Cursor: `\033[?25l`
- Show Cursor: `\033[?25h`

#### Save and Restore
- Save Cursor Position: `\033[s`
- Restore Cursor Position: `\033[u`
- Save Cursor Position and Attributes: `\0337`
- Restore Cursor Position and Attributes: `\0338`

#### Scrolling
- Scroll Up N Lines: `\033[N S`
- Scroll Down N Lines: `\033[N T`

#### Erasing
- Erase Up: `\033[K`
- Erase Down: `\033[J`
- Erase All: `\033[2J`
- Erase End of Line: `\033[K`
- Erase Start of Line: `\033[1K`
- Erase Line: `\033[2K`
- Erase Up (cursor to top of screen): `\033[1J`
- Erase Down (cursor to end of screen): `\033[J`

#### Text Modification
- Insert N Spaces: `\033[N @`
- Delete N Characters: `\033[N P`

#### Tab Control
- Horizontal Tab (HT): `\033[I`
- Backward Tab (BT): `\033[Z`

#### Line and Box Drawing
- Start Line Drawing Mode: `\033(0`
- End Line Drawing Mode: `\033(B`

#### Cursor Styles
- Set Cursor Style (block): `\033[2 q`
- Set Cursor Style (underline): `\033[4 q`
- Set Cursor Style (bar): `\033[6 q`

#### Resetting
- Reset Terminal to Initial State: `\033c`

#### Miscellaneous
- Query Cursor Position: `\033[6n`

#### Text Attributes
- Reset All Attributes: `\033[0m`
- Set Bold: `\033[1m`
- Set Dim: `\033[2m`
- Set Italic: `\033[3m`
- Set Underline: `\033[4m`
- Set Blink: `\033[5m`
- Set Inverse: `\033[7m`
- Set Hidden: `\033[8m`
- Set Strikethrough: `\033[9m`
- Set Foreground Color: `\033[38;5;#m` (# is color code)
- Set Background Color: `\033[48;5;#m` (# is color code)

#### Terminal Window
- Change Window Title: `\033]0;Title Text\x07`


[child ⬇️](#cfe613c2-5014-4dd8-874e-35d06457d7df)

---

(main branch ⎇)
###### cfe613c2-5014-4dd8-874e-35d06457d7df
[parent ⬆️](#aaa2c242-6363-4e75-9e25-2d7833dbdde4)
