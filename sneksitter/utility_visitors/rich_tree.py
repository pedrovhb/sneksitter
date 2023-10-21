from __future__ import annotations

import colorsys
import inspect
import random
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


class _PredicateHighlight(NamedTuple):
    """A predicate highlight for a tree node."""

    predicate: Callable[[Node], bool]
    color: str

    @classmethod
    def from_value(
        cls,
        value: Callable[[Node], bool],
        idx: int = 0,
    ) -> _PredicateHighlight:
        """Create a predicate highlight from a value."""
        color = _random_color_for_value(value) if isinstance(value, Hashable) else idx
        return cls(predicate=value, color=color)

    def get_predicate_display(self) -> str:
        """Get the display for the predicate."""

        name = getattr(self.predicate, "__name__", None)

        if name == "<lambda>":
            return inspect.getsource(self.predicate).strip()
        if name is not None:
            return name
        return repr(self.predicate)


class RichTreeBuilder(BaseVisitor):
    named_only = False
    METADATA_PROVIDERS = (FieldNameMetadataProvider,)

    def __init__(self, *predicate_highlights: Callable[[Node], bool]) -> None:
        super().__init__()
        self._tree: RichTree = RichTree("root")
        self._stack: list[RichTree] = [self._tree]

        self.predicate_highlights = [
            _PredicateHighlight.from_value(pred, i)
            for i, pred in enumerate(predicate_highlights)
        ]

    show_node_text_types = {"identifier", "string", "number", "attribute"}

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

        # if (interval_data := provider.get(FieldNameMetadataProvider)) is not None:
        #     parts.append(Text(f" [{interval_data}]", style="green"))
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

    def get_tree(self, tree: Tree) -> RichTree:
        """Class method to traverse the tree and call the visitor's methods."""
        self.traverse(tree)
        # Add the predicate match attr_path, if there are any predicate highlights
        if self.predicate_highlights:
            match_key = Group(
                *(
                    Text(
                        f"● {pred.get_predicate_display()}",
                        style=f"bold {pred.color}",
                    )
                    for pred in self.predicate_highlights
                ),
            )
            self._tree.add(match_key)
        return self._tree


if __name__ == "__main__":
    import rich

    parser = tree_sitter_languages.get_parser("python")

    # source = Path(__file__).read_bytes()

    source = """
    from __future__ import annotations
    
    def foo(bar: int) -> None:
        pass
        
    def closure_factory() -> Callable[[int], int]:
        def closure(x: int) -> int:
            return x + 1
        return closure
    
    class Bar:
        def __init__(self, x: int) -> None:
            self.x = x
            
        async def with_closure(self) -> None:
            closure = closure_factory()
            def inner() -> None:
                pass
            inner()
            return closure(1)
    """

    tree = parser.parse(textwrap.dedent(source).encode())

    is_method = Q(parent__type="class_definition", type="function_definition")
    # is_function = Q(type="function_definition")
    # is_method = is_in_class & is_function

    rich_tree = RichTreeBuilder(
        # lambda n: n.type == "identifier",
        # Q(type="function_definition"),
        # +Q(type="function_definition"),
        # -Q(type="function_definition") & Q(type="identifier"),
        # +Q(type="function_definition"),
        # -Q(type="function_definition"),
        # -+Q(type="function_definition"),
        is_method,
        # is_function,
        # is_in_class,
        # ++Q(type="function_definition"),
    ).get_tree(tree)

    console = rich.get_console()
    console.print(rich_tree)

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
