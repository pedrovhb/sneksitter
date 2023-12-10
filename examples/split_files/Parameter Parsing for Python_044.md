# Assistant

The `Parameter` class has been successfully defined, along with the `from_node` method that takes a tree-sitter `Node` and an optional description string as arguments. This method uses the utility functions to extract relevant details like the parameter's name, type annotation, and default value.

Next, let's work on the `from_node_parameters` method. This method is a bit more complex because it must consider the surrounding context to correctly identify special types of parameters like varargs, kwargs, positional-only, and keyword-only parameters. I'll extend the `Parameter` class to include this method.

[child ⬇️](#85be84c2-c571-404d-a8a3-2fff899ffe84)

---

(main branch ⎇)
###### 85be84c2-c571-404d-a8a3-2fff899ffe84
[parent ⬆️](#4463286e-818a-4e1d-b7e1-265d5121f5bf)
