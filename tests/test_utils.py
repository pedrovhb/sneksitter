import pytest
import tree_sitter
import os

from tree_sitter import Tree
from tree_sitter_languages import get_language, get_parser

from sneksitter.utils import ts_traverse_bfs


@pytest.fixture(scope="session")
def ts_language_python() -> tree_sitter.Language:
    return get_language("python")


@pytest.fixture(scope="session")
def ts_parser_python() -> tree_sitter.Parser:
    return get_parser("python")


@pytest.fixture
def ts_python_tree(ts_parser_python) -> Tree:
    source_code = """
    import antigravity
    from dataclasses import dataclass
    
    @dataclass
    class Foo(Bar):
        some_attribute: int
        another_attribute: str = "default value"
    
        @classmethod
        def some_method(cls):
            pass
    
    def some_function(*args: int, **kwargs: str):
        foo = Foo(args[0])
        for i in range(len(args)):
            print(i)
        return foo
    
    
    if __name__ == "__main__":
        some_function(1, 2, 3, 4, 5)
    """
    tree = ts_parser_python.parse(bytes(source_code, "utf8"))
    return tree


def test_ts_traverse_bfs(ts_python_tree: Tree):
    seen_node_types = set()
    max_depth = 0
    for node, depth in ts_traverse_bfs(ts_python_tree.root_node):
        seen_node_types.add(node.type)
        max_depth = max(max_depth, depth)

    assert all(
        t in seen_node_types
        for t in ("class_definition", "function_definition", "identifier")
    )
    assert max_depth == 8
