import argparse
import io
import sys

from tree_sitter import Node
from tree_sitter_languages import get_parser

from sneksitter.visitor import TSVisitor


def node_own_text(node: Node) -> bytes:
    """Return the text of the node, without the text of its children."""
    children_ranges = [(child.start_byte, child.end_byte) for child in node.children]
    text = node.text
    for start, end in reversed(children_ranges):
        text = text[:start] + text[end:]
    return text


class HtmlExplorer(TSVisitor):
    def __init__(self, root_node: Node, output: io.BytesIO = None) -> None:
        super().__init__(root_node)
        self.output = output or io.BytesIO()

    def visit_default(self, node: Node) -> None:
        if not node.is_named:
            return
        node_text = node_own_text(node)
        display = b"  " * self.crt_depth + node.type.encode()

        display = display.ljust(40) + b" | " + node_text.replace(b"\n", b"\\n") + b"\n"
        self.output.write(display)


if __name__ == "__main__":
    cli_parser = argparse.ArgumentParser()
    cli_parser.add_argument("file", type=argparse.FileType("rb"))
    cli_parser.add_argument("output", type=argparse.FileType("w"), nargs="?")
    args = cli_parser.parse_args()

    tree = get_parser("html").parse(args.file.read())
    explorer = HtmlExplorer(tree.root_node, args.output or sys.stdout.buffer)
    explorer.traverse()
