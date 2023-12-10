import argparse
import re
import sys

from tree_sitter import Node
from tree_sitter_languages import get_parser

from sneksitter.visitor import TSTransformer

# Panel documentation has a bunch of issue links like:
#    - Support jslinking Parameterized class ([#2441](https://github.com/holoviz/panel/issues/2441))
# In this case, we'll remove both the link and the issue number text.

RE_ISSUE_LINK = re.compile(r"^#\d+$")


class MdCleaner(TSTransformer):
    def __init__(self, root_node: Node):
        super().__init__(root_node)
        self.replaced_link_count = 0
        self.replaced_image_count = 0

    def leave_link(self, node: Node) -> bytes:
        """Replace links with their text."""
        link_text_node = node.children[0]
        assert link_text_node.type == "link_text"
        self.replaced_link_count += 1

        if RE_ISSUE_LINK.match(link_text_node.text.decode()):
            return b""

        return link_text_node.text

    def leave_image(self, node: Node) -> bytes:
        """Replace images with their alt text."""
        image_description = node.children[0]
        assert image_description.type == "image_description"
        self.replaced_image_count += 1
        return b"[image: " + image_description.text + b"]"


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("file", type=argparse.FileType("rb"))
    arg_parser.add_argument("output", type=argparse.FileType("wb"), default="-")
    args = arg_parser.parse_args()

    parser = get_parser("markdown")
    tree = parser.parse(args.file.read())

    cleaner = MdCleaner(tree.root_node)
    args.output.write(cleaner.traverse())

    sys.stderr.write(
        f"Replaced {cleaner.replaced_link_count} links and {cleaner.replaced_image_count} images.\n"
    )
