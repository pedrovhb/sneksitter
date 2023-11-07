from __future__ import annotations

import argparse
import colorsys
import inspect
import random
import sys
import textwrap
from pathlib import Path
from typing import TypeVar, Type, Callable, Hashable, NamedTuple

import tree_sitter_languages
from rich.console import ConsoleRenderable, Group
from rich.text import Text
from tree_sitter import Node, Tree

from sneksitter.metadata import FieldNameMetadataProvider, MetadataProvider
from sneksitter.q import Q
from sneksitter.visitor import BaseVisitor

try:
    from rich.tree import Tree as RichTree
except ImportError:
    raise ImportError(
        "The `rich` package is required to use the RichTreeBuilder. "
        "Please install it with `pip install rich`."
    )

_T = TypeVar("_T")


# Initialize a golden ratio counter

ii = 0


def _random_color_for_value(value: Hashable, hue_split: int = 12) -> str:
    """Get a random color for a value.

    The value is randomized, but consistent across runs. This is done by seeding the random number generator
    with the hash of the value.

    Args:
        value: The value to get a random color for.

    Returns:
        A random color for the value, as a hex string.
    """
    prev_random_state = random.getstate()
    random.seed(hash(value))
    hue = random.randint(0, hue_split) / hue_split
    saturation = 0.7
    lightness = random.choice((0.4, 0.7))

    rgb = colorsys.hls_to_rgb(hue, lightness, saturation)
    random.setstate(prev_random_state)
    return f"#{int(rgb[0] * 255):02x}{int(rgb[1] * 255):02x}{int(rgb[2] * 255):02x}"


class RichTreeBuilder(BaseVisitor):
    show_node_text_types = {"identifier", "string", "number", "attribute"}

    def __init__(self, tree: Tree) -> None:
        super().__init__(tree)
        self._rich_tree: RichTree = RichTree("root")
        self._stack: list[RichTree] = [self._rich_tree]
        self._field_name_provider = FieldNameMetadataProvider()

    def _add_node(self, node_display: ConsoleRenderable) -> None:
        prev = self._stack[-1]
        new = prev.add(node_display)
        self._stack.append(new)

    def _format_node_display(
        self,
        node: Node,
    ) -> ConsoleRenderable:
        match_color = None
        match_indicators = []

        for pred in (p for p in self.predicate_highlights if p.predicate(node)):
            match_color = match_color or pred.color
            match_indicators.append(Text("●", style=f"bold {pred.color}"))

        match_color = match_color or "white"
        parts = [
            *match_indicators,
            "  ",
            Text(node.type, style=match_color),
        ]

        # if (field_name := provider.get(FieldNameMetadataProvider)) is not None:
        #     parts.append(Text(f" [{field_name}]", style="green"))
        if node.type in self.show_node_text_types:
            parts.append(
                Text(
                    "\t" + node.text.decode().splitlines()[0],
                    style="yellow",
                    overflow="ellipsis",
                    justify="right",
                ),
            )

        return Text.assemble(*parts)

    def visit(self, node: Node) -> None:
        self._add_node(self._format_node_display(node))

    def leave(self, node: Node) -> None:
        self._stack.pop()

    def traverse(self, *args: object, **kwargs: object) -> _T:
        super().traverse(*args, **kwargs)
        return self._rich_tree


language_map = {
    ".py": "python",
    ".pyi": "python",
    ".pyw": "python",
    ".js": "javascript",
    ".jsx": "javascript",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".rs": "rust",
    ".cpp": "c++",
    ".h": "c++",
    ".c": "c",
    ".java": "java",
    ".php": "php",
    ".rb": "ruby",
    ".cs": "csharp",
    ".go": "go",
    ".swift": "swift",
    ".sh": "bash",
    ".kt": "kotlin",
    ".hs": "haskell",
    ".lua": "lua",
    ".r": "r",
    ".pl": "perl",
    ".m": "objective-c",
    ".md": "markdown",
    ".html": "html",
    ".css": "css",
    ".json": "json",
    ".yaml": "yaml",
    ".toml": "toml",
    ".xml": "xml",
    ".sql": "sql",
    ".scala": "scala",
    ".clj": "clojure",
    ".jl": "julia",
    ".rst": "rst",
    ".tex": "latex",
}


def cli_tool() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "source",
        help="The source code to parse",
        type=Path,
        default=Path("-"),
    )
    parser.add_argument("--language", "-l", help="The language to parse", default="auto")
    parser.add_argument(
        "--named-only",
        help="Only show named nodes",
        action="store_true",
    )
    args = parser.parse_args()

    if args.language == "auto":
        if args.source == Path("-"):
            raise ValueError(
                "Cannot automatically detect language when reading from stdin. "
                "Please specify the language with the --language/-l option."
            )

        source_path = Path(args.source.name)
        suffix = source_path.suffixes[-1] if source_path.suffixes else ""

        args.language = language_map.get(suffix)
        if args.language is None:
            raise ValueError(
                f"Could not automatically detect language for file with extension {suffix}. "
                "Please specify the language with the --language/-l option."
            )
    parser = tree_sitter_languages.get_parser(args.language)
    if args.source == Path("-"):
        contents = sys.stdin.buffer.read()
    else:
        contents = args.source.read_bytes()

    tree = parser.parse(contents)
    rich_tree = RichTreeBuilder(tree).traverse()

    import rich

    console = rich.get_console()
    console.print(rich_tree)


if __name__ == "__main__":
    cli_tool()

    # root
    # └── module
    #     ├── future_import_statement
    #     │   ├── from
    #     │   ├── __future__
    #     │   ├── import
    #     │   └── dotted_name [field: name]
    #     │       └── identifier `annotations`
    #     ├── import_from_statement
    #     │   ├── from
    #     │   ├── dotted_name [field: module_name]
    #     │   │   └── identifier `pathlib`
    #     │   ├── import
    #     │   └── dotted_name [field: name]
    #     │       └── identifier `Path`
    #     ├── import_from_statement
    #     │   ├── from
    # ...
