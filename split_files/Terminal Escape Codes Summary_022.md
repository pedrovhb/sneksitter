---
file: /home/pedro/Documents/chatgpt_export/Markdown/Terminal Escape Codes Summary.md
heading_stack: <root> -> 3992efef-506a-4339-a915-da88075a28b4 -> System -> 279db4e3-a725-4c3f-8ad7-66b2e924c4c1 -> System -> aaa2c242-6363-4e75-9e25-2d7833dbdde4 -> User -> ANSI Escape Codes for Terminal Control and Cursor Manipulation -> Cursor Positioning -> Cursor Visibility -> Save and Restore -> Scrolling -> Erasing -> Text Modification -> Tab Control -> Line and Box Drawing -> Cursor Styles -> Resetting -> Miscellaneous -> Text Attributes -> Terminal Window -> cfe613c2-5014-4dd8-874e-35d06457d7df -> Assistant
---
# Assistant

The list you provided seems to be quite comprehensive and covers a wide range of ANSI escape codes for terminal control and cursor manipulation. However, I'll point out a few additional escape codes that are commonly used:

1. **Clear Screen**: To clear the entire terminal screen, you can use the following code:
   ```
   \033[2J
   ```

2. **Clear Line**: To clear the current line where the cursor is located, you can use the following code:
   ```
   \033[K
   ```

3. **Save Cursor Position**: You can save the current cursor position using:
   ```
   \033[s
   ```

4. **Restore Cursor Position**: To restore the saved cursor position, use:
   ```
   \033[u
   ```

5. **Query Cursor Position**: To query the current cursor position, you can use:
   ```
   \033[6n
   ```

6. **Set Text Foreground and Background Color**: You can change the text's foreground and background color using escape codes like:
   ```
   \033[38;5;#m   # For foreground color (# is the color code)
   \033[48;5;#m   # For background color (# is the color code)
   ```

7. **Terminal Window Title**: To change the title of the terminal window, you can use:
   ```
   \033]0;Title Text\x07
   ```

It's important to note that the availability and interpretation of escape codes can vary between different terminal emulators and systems, so it's a good practice to test these codes in the specific environment you're working with to ensure compatibility.

---
