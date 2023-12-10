from pathlib import Path

from tree_sitter import Node
from tree_sitter_languages import get_parser

from sneksitter.visitor import TSTransformer, TSVisitor


class HtmlLinkFinder(TSVisitor):



class MarkdownAggregator(TSTransformer):
    def leave_atx_heading(self, node: Node) -> bytes:
        return b"#" + node.text


if __name__ == "__main__":
    md_files_path = Path("/home/pedro/projs/ready/markget/read_ready/fastapi-tiangolo-com")
    md_files = list(md_files_path.glob("**/*.md"))

    parser = get_parser("markdown")

    processed_files = []

    # Push headings one level down
    for file in md_files:
        tree = parser.parse(file.read_bytes())
        visitor = MarkdownAggregator(tree.root_node)
        result = visitor.traverse()
        processed_files.append((file, result))

    # print(processed_files[0][1].decode())
    total_file = []
    for file, result in processed_files:
        title = f"# {file.relative_to(md_files_path)}".encode()
        total_file.append(b"\n\n")
        total_file.append(result)
        total_file.append(b"\n\n")

    Path("aggregated_total.md").write_bytes(b"".join(total_file))
