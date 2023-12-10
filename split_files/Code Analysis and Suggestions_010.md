---
file: /home/pedro/Documents/chatgpt_export/Markdown/Code Analysis and Suggestions.md
heading_stack: <root> -> 9e26d6f4-d44b-48ce-804a-b866059e8a08 -> System -> 2688ae0b-3d9e-45f7-8b73-a565f3fdc93f -> System -> aaa2bac3-68ad-45e4-a1fd-a350837ca8d1 -> User -> f831b866-ab70-403a-9851-255413e1dcc2 -> Assistant -> patch_typing Function -> Test Code
---
### Test Code

The code under `if __name__ == "__main__":` is for testing this patch.

1. **Applying the Patch**: It first applies the `patch_typing` with `verbose=True`.

2. **Importing and Using Typing Extensions**: Then it imports various types and constructs a function `doubled` that doubles the output of the function it decorates.

3. **Testing**: Finally, it tests this function by decorating an `add` function and calling it.

