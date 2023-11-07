from __future__ import annotations

import re
import signal
import sys
import textwrap
from contextlib import contextmanager
from dataclasses import dataclass, field
from functools import reduce
from pathlib import Path
from typing import Iterator, ContextManager

from intervaltree import IntervalTree
from tree_sitter import Node, Tree, TreeCursor

from sneksitter.utils import on_visit
from sneksitter.visitor import BaseVisitor

RE_HEADING = re.compile(r"atx_h(?P<level>\d)_marker")


@dataclass
class Heading:
    level: int
    root_node: Node
    level_start_byte: int | None = None
    title_start_byte: int | None = None
    title_end_byte: int | None = None
    content_start_byte: int | None = None
    content_end_byte: int | None = None

    parent: Heading | None = None
    children: list[Heading] = field(default_factory=list)

    def __hash__(self) -> int:
        return (
            hash(self.level)
            ^ hash(self.title_start_byte)
            ^ hash(self.title_end_byte)
            ^ hash(self.content_start_byte)
            ^ hash(self.content_end_byte)
            ^ hash(reduce(lambda x, y: x ^ hash(y), self.children, 0))
        )

    @property
    def title(self) -> str:
        """Title of the heading, without the heading #."""
        return self.root_node.text[self.title_start_byte : self.title_end_byte].decode().strip()

    @property
    def content(self) -> str:
        """Content under the heading, including the children's content."""
        return self.root_node.text[self.content_start_byte : self.content_end_byte].decode()

    @property
    def text(self) -> str:
        """Text including the heading and heading #, and the children's text."""
        return self.root_node.text[self.level_start_byte : self.content_end_byte].decode()

    @property
    def own_text(self) -> str:
        """Text including the heading and heading #, without the children's text.""" ""
        own_content_end = (
            self.children[0].level_start_byte if self.children else self.content_end_byte
        )
        return self.root_node.text[self.content_start_byte : own_content_end].decode()

    @property
    def own_content(self) -> str:
        """Content under the heading, without the children's content."""
        own_content_end = (
            self.children[0].level_start_byte if self.children else self.content_end_byte
        )
        return self.root_node.text[self.content_start_byte : own_content_end].decode()

    def iter_heading_levels(self) -> Iterator[Heading]:
        """Iterate over all headings in the tree, in order of appearance."""
        yield self
        for child in self.children:
            yield from child.iter_heading_levels()

    def print_recursive(self) -> None:
        for h in self.iter_heading_levels():
            print(" " * h.level * 3, f"[{h.level}] {h.title}")
            print(textwrap.indent(h.own_content, "  " + " " * h.level * 3 + "│ ", lambda x: True))

    def for_ml(self) -> str:
        """Return the text but masks heading level tokens so they can be used for training a
        model to detect heading levels."""
        text_children = "\n".join(child.for_ml() for child in self.children)
        text = (
            f"<h{self.level}>{self.title}</h{self.level}>\n"
            f"<c{self.level}>{self.own_content}{text_children}</c{self.level}>"
        )
        return text.strip()

    def for_ml_stripped(self) -> str:
        text_children = "\n".join(child.for_ml_stripped() for child in self.children)
        text = f"{self.title}\n{self.own_content}{text_children}"
        return text.strip()


class MarkdownHeadingContentExtractor(BaseVisitor):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._root_node = None
        self._interval_tree = IntervalTree()
        # self._stack: dict[int, list[Heading]] = defaultdict(list)
        self._stack: list[Heading] = []
        self.root_heading: Heading | None = None

    def visit_document(self, node: Node) -> None:
        self.root_heading = Heading(
            0,
            node,
            level_start_byte=0,
            title_start_byte=0,
            title_end_byte=0,
            content_start_byte=0,
            content_end_byte=len(node.text),
            parent=None,
        )
        self._stack.append(self.root_heading)
        self._root_node = node

    @on_visit(type=RE_HEADING.match)
    def visit_heading_marker(self, node: Node) -> None:
        heading_level = int(RE_HEADING.match(node.type).group("level"))
        if node.next_sibling is None:
            return

        # Get title stripping leading space, but looking out for the case of a
        # heading with no title (i.e. just a marker)
        title_start = min(
            node.next_sibling.start_byte + 1,
            node.next_sibling.end_byte,
        )

        title_end = node.next_sibling.end_byte
        content_start = title_end + 1

        heading = Heading(
            level=heading_level,
            root_node=self._root_node,
            level_start_byte=node.start_byte,
            title_start_byte=title_start,
            title_end_byte=title_end,
            content_start_byte=content_start,
            parent=self._stack[-1],
        )

        while self._stack[-1].level >= heading_level:
            prev = self._stack.pop()
            self._stack[-1].children.append(prev)
            prev.content_end_byte = node.start_byte

        self._stack.append(heading)

    def leave_document(self, node: Node) -> None:
        while len(self._stack) > 1:
            prev = self._stack.pop()
            self._stack[-1].children.append(prev)
            prev.content_end_byte = node.end_byte

        self._stack.pop().content_end_byte = node.end_byte

    def traverse(self) -> Heading:
        super().traverse()
        return self.root_heading


if __name__ == "__main__":
    from tree_sitter_languages import get_parser

    parser = get_parser("markdown")
    # source = Path("/home/pedro/projs/coding_lang_data/repos/nlvm/README.md").read_bytes()
    md_tests = (
        """\
        b4 it all
        
        # Header with Special Characters !@#$%^&*()

        ## Sub-header with Emoji 😄👍

        ### Sub-sub-header with Non-ASCII Characters ñöü
        """,
        """\
        This document explains some advanced features of Asyncio.

        # What is Asyncio anyway?

        Now we'll get to the content.

        ## Asyncio is cool

        This is a list of reasons why asyncio is cool:



        - It offers a simple API
        - It goes fast
        - It kills aliens
        - Doesn't afraid of anything

        ### On killing aliens

        Aliens are bad, and asyncio is good. This is proven by an experiment
        conducted at the University of Science in 2017. In this experiment,
        scientists shocked the world by showing that asyncio is good at killing
        aliens.

        The experiment consisted of the following steps:

        1. Create an alien
        2. Create an asyncio event loop
        3. Have the alien attack the event loop
        4. The event loop defends itself
        5. The alien dies


        ### On not being afraid of anything

        Asyncio is not afraid of anything. This follows from the simple
        fact that asyncio is an implementation of an event loop, and event
        loops cannot have feelings such as fear (or love, for that matter).

        ## Asyncio is bad

        Your information is wrong; in fact, asyncio is not bad.

        # Conclusion

        Asyncio is good.
        """,
        """\
        ## Caveats

        This shouldn't be used while intoxicated.

        ### Effects of use while intoxicated

        Use while intoxicated may...

        ## Recommendations

        The following...
        """,
    )
    # for source in md_tests:
    #     source = textwrap.dedent(source).encode()
    #     root_node = parser.parse(source)
    #
    #     visitor = MarkdownHeadingContentExtractor(parser)
    #     root_heading = visitor.traverse(root_node)
    #     root_heading.print_recursive()
    #     print("-*_*" * 30)
    #     print(root_heading.for_ml())
    #     print("-*_*" * 30)
    #     print(root_heading.for_ml_stripped())
    #     print("-*_*" * 30)
    # exit()
    # print("----")
    files = [
        Path("/home/pedro/projs/transformers/docs/source/en/pipeline_tutorial.md"),
        *(Path("/home/pedro/Documents/chatgpt_export/Markdown/").rglob("*.md"))
        # Path("/home/pedro/Documents/ChatGPT Data/Markdown/X11 forwarding on remote..md"),
    ]

    def split_to_multiple(source: bytes) -> Iterator[bytes]:
        tree = parser.parse(source)
        visitor = MarkdownHeadingContentExtractor(tree)
        root_heading = visitor.traverse()

        for node in root_heading.iter_heading_levels():
            yield node

    output_dir = Path("split_files")
    output_dir.mkdir(exist_ok=True)
    gn = iter(files)
    while True:
        n = next(gn)
        if n.name == "Grouping Tree-sitter Results Hierarchically.md":
            break
    for file in gn:
        if file.name in (
            "FastF1 Library Documentation Search.md",
            "New chat.md",
            "Python Code Analysis_ Tree-sitter.md",
            "File Management Framework Design.md",
            "Grouping Tree-sitter Results Hierarchically.md",
        ):
            continue
