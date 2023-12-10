# Assistant

The `tree_sitter_languages` library's `Language` object (`lang` in our case) does not directly expose methods to retrieve the grammar or the valid regular expressions for each type of node. The available methods mainly concern field and node IDs, query functionalities, and parse state transitions.

However, the `tree-sitter` project, upon which `tree_sitter_languages` is built, generates parsers based on a context-free grammar defined in a `.scm` (S-expression) file for each language. These grammar files are usually part of the language's tree-sitter repository and define the rules for parsing the language. They include constructs that could be considered akin to regular expressions for each type of node.

If you're interested in the underlying grammar, you could refer to the original `.scm` files in the tree-sitter repository for Python, which should be publicly accessible.

Would you like to explore the available methods further, or do you have a different direction in mind?

[child ⬇️](#aaa22663-e915-48c4-bea7-373bfc8baa8b)

---

(main branch ⎇)
###### aaa22663-e915-48c4-bea7-373bfc8baa8b
[parent ⬆️](#fbabf230-e744-4690-ad63-eca029735b67)
