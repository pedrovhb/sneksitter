from io import BytesIO
from pathlib import Path

from anytree import PreOrderIter
from intervaltree import IntervalTree
from tree_sitter import Parser

from sneksitter.fray.buf import SNode
from sneksitter.fray.utils import Position, Range


def _build_nodes_itree(snode: SNode) -> IntervalTree:
    itree = IntervalTree()
    for node in PreOrderIter(snode):
        node_range = Range.from_ts_node(node)
        if node_range in itree:
            itree[node_range.start : node_range.end][node.type] = node
        else:
            itree[node_range.start : node_range.end] = {node.type: node}

    return itree


class Editor:
    """A class that represents a text editor.

    There's an underlying BytesIO object which handles the bytes buffer,
    and the Editor class further provides intelligent cursor management
    and text manipulation methods.
    """

    def __init__(
        self,
        initial_text: bytes,
        parser: Parser,
    ) -> None:
        self._text = initial_text
        self._parser = parser
        self._cursor = Position(0, 0)
        self._ts_tree = self._parser.parse(self._text)
        self._snode_root = SNode.from_ts_node(self._ts_tree.root_node)
        self._nodes_itree = _build_nodes_itree(self._snode_root)

    def edit_node(self, node: SNode, replacement: bytes) -> None:
        # 1. Get the original range of the node.
        # 2. Calculate the new range of the node.
        # 3. Calculate the updated positions of the nodes that come
        #    after the edited node.
        # 4. Update the text of the node and editor.
        # 5. Parse a new ts tree from the updated code.  (later on, do this efficiently editing the tree)
        # 6. Match the new ts tree to the old one, look

        pass

    @property
    def cursor(self) -> Position:
        return self._cursor

    @cursor.setter
    def cursor(self, position: Position):
        self._cursor = position


if __name__ == "__main__":
    from tree_sitter_languages import get_parser

    parser = get_parser("python")
    code = Path("single_sample.py").read_bytes()

    editor = Editor(code, parser)
