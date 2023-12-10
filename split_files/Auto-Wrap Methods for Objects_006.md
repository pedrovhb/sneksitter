---
file: /home/pedro/Documents/chatgpt_export/Markdown/Auto-Wrap Methods for Objects.md
heading_stack: <root> -> 02a68d18-f2e6-4dfc-9640-eefcff9a8938 -> System -> 16f71094-696f-4659-a5b7-a5ea706f6ddd -> System -> aaa26859-01d8-49bd-b879-7d8ec5f19da1 -> User
---
# User

from wrapt import ObjectProxy
from tree_sitter_languages import get_parser

class EnhancedNode(ObjectProxy):
    def __init__(self, wrapped_node, enhanced_tree):
        super(EnhancedNode, self).__init__(wrapped_node)
        self._self_enhanced_tree = enhanced_tree

    def replace(self, new_code: str):
        start_byte = self.__wrapped__.start_byte
        end_byte = self.__wrapped__.end_byte
        source_code = self._self_enhanced_tree._self_source_code

        new_source_code = source_code[:start_byte] + new_code.encode() + source_code[end_byte:]
        self._self_enhanced_tree._update_source_code(new_source_code)

class EnhancedTree(ObjectProxy):
    def __init__(self, wrapped_tree, source_code):
        super(EnhancedTree, self).__init__(wrapped_tree)
        self._self_source_code = source_code
        self._self_history_stack = []
        self._self_redo_stack = []

    def walk(self):
        cursor = self.__wrapped__.walk()
        return EnhancedCursor(cursor, self)
    
    def _update_source_code(self, new_source_code):
        self._self_history_stack.append(self.__wrapped__)
        self._self_source_code = new_source_code

        parser = get_parser("python")
        new_tree = parser.parse(new_source_code, self.__wrapped__)
        self.__wrapped__ = new_tree

    def undo(self):
        if self._self_history_stack:
            self._self_redo_stack.append(self.__wrapped__)
            self.__wrapped__ = self._self_history_stack.pop()

    def redo(self):
        if self._self_redo_stack:
            self._self_history_stack.append(self.__wrapped__)
            self.__wrapped__ = self._self_redo_stack.pop()

class EnhancedCursor(ObjectProxy):
    def __init__(self, wrapped_cursor, enhanced_tree):
        super(EnhancedCursor, self).__init__(wrapped_cursor)
        self._self_enhanced_tree = enhanced_tree

    def node(self):
        node = self.__wrapped__.node
        return EnhancedNode(node, self._self_enhanced_tree)

