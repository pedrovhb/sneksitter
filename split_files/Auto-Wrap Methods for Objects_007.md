---
file: /home/pedro/Documents/chatgpt_export/Markdown/Auto-Wrap Methods for Objects.md
heading_stack: <root> -> 02a68d18-f2e6-4dfc-9640-eefcff9a8938 -> System -> 16f71094-696f-4659-a5b7-a5ea706f6ddd -> System -> aaa26859-01d8-49bd-b879-7d8ec5f19da1 -> User -> Test code
---
# Test code
source_code = b"print('Hello, world!')"
parser = get_parser("python")
tree = parser.parse(source_code)
enhanced_tree = EnhancedTree(tree, source_code)

cursor = enhanced_tree.walk()
cursor.goto_first_child()
enhanced_node = cursor.node()

print("Before replace:")
print(enhanced_tree._self_source_code.decode())

enhanced_node.replace("print('Hi')")
print("After replace:")
print(enhanced_tree._self_source_code.decode())

enhanced_tree.undo()
print("After undo:")
print(enhanced_tree._self_source_code.decode())

enhanced_tree.redo()
print("After redo:")
print(enhanced_tree._self_source_code.decode())


---

How can we hook into the wrapped objects so we always have them return the wrapped enhanced version of whatever objects they usually did, without manually wrapping every method?

[child ⬇️](#9bb4a2f9-42fa-443c-a853-8b9f8dd57093)

---

(main branch ⎇)
###### 9bb4a2f9-42fa-443c-a853-8b9f8dd57093
[parent ⬆️](#aaa26859-01d8-49bd-b879-7d8ec5f19da1)
