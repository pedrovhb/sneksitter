from pathlib import Path

from sneksitter._node_codegen.gen_nodes_file_jinja import _main

_main()
from sneksitter._node_codegen.generated_code import python_node_types as l
from sneksitter._node_codegen.generated_code.python_base_visitor import BasePythonNodeVisitor


class MyVisitor(BasePythonNodeVisitor):
    def __init__(self) -> None:
        super().__init__()
        self._cls_stack = []
        self._func_stack = []
        self._func_params_stack = []

    def visit_FunctionDefinition(self, node: l.FunctionDefinition) -> bool | None:
        if not node.name.original_node.text.decode().startswith(("visit_", "leave_")):
            print(f"found function definition for {node.name.original_node.text.decode()}")
            return True
        return False

    def visit_Parameters(self, node: l.Parameters) -> bool | None:
        for param in node.children:
            print(f"  found parameter `{param.original_node.text.decode()}`")


# tree = get_parser("python").parse(b"def foo():\n    pass")
from tree_sitter import Language, Parser

Language.build_library(
    # Store the library in the `build` directory
    "/home/pedro/.local/tree-sitter/my-languages.so",
    # Include one or more languages
    [
        "/home/pedro/.local/tree-sitter/tree-sitter-python",
    ],
)
PY_LANGUAGE = Language("/home/pedro/.local/tree-sitter/my-languages.so", "python")
parser = Parser()
parser.set_language(PY_LANGUAGE)

# for file in Path("/home/pedro/projs/asynkets").rglob("*.py"):
#     tree = parser.parse(Path(file).read_bytes())
#
#     node = l.BasePythonNode.from_node(tree.root_node)
#
#     visitor = MyVisitor()
#     visitor.traverse(node)

sample_code = b"""
def foo():
    pass
    
for i in range(10):
    def bar():
        pass
    bar()
"""

# tree = parser.parse(Path(__file__).read_bytes())
tree = parser.parse(sample_code)
node = l.BasePythonNode.from_node(tree.root_node)
visitor = MyVisitor()
visitor.traverse(node)
