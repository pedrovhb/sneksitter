
[Tree-sitter](https://tree-sitter.github.io/tree-sitter) is a very flexible parser generator tool and library.
It has bindings for several languages, and parsers for more languages than you can name off the top of your head, probably.
A binding enables you to use tree-sitter as a library with a given language, and a parser is what allows you to transform a string of code into a tree of nodes.
For instance, you may use the Python binding to parse a CSS file, and get a tree of nodes that represent the CSS file. It'll look something like this:

```tree-sitter
# to do: add tree-sitter tree here
```

Tree-sitter is pretty fast, as it's meant for use in text editors.
It can do incremental parsing, which means that if you change a file, it can update the tree without having to re-parse the whole file.
That contributes to making it so fast it can be used for highlighting on each keystroke with nearly imperceptible latency.

On the other side of compromises made, a different library that I also like a lot is `libcst`.
It's a Python library that allows you to parse Python code, and then modify it and re-generate it.
It has pretty different goals from tree-sitter, so there's not many head-to-head comparisons that can be made, but roughly speaking - 
