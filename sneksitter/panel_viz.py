import panel as pn
from panel.viewable import Viewable
from tree_sitter import Node
from tree_sitter_languages import get_parser

pn.extension("codeeditor")


sample_a_value = """\
class Foo:
    def __init__(self, value):
        self.value = value

    def add(self, a):
        return a + self.value
"""

sample_b_value = """\
class Foo:
    def __init__(self, value):
        self.value = value

    def addition(self, other):
        return other + self.value
"""

parser = get_parser("python")


# Consolidating the code into a self-contained module


class TreeSitterMarkdownRenderer:
    """
    A class to render Tree-sitter trees as markdown text.
    """

    def __init__(self, tree):
        """
        Initialize with a tree-sitter tree.
        """
        self.tree = tree

    def tree_sitter_to_anytree(self, node, parent=None, field_name=None):
        """
        Convert a tree-sitter node to an anytree Node for easier manipulation and visualization.
        Include field names where available.
        """
        from anytree import Node

        is_error = node.type == "ERROR"

        anytree_node = Node(
            f"{node.type} ({field_name})" if field_name else node.type,
            parent=parent,
            ts_node=node,
            field_name=field_name,
            is_error=is_error,
        )
        for i, child in enumerate(node.children):
            child_field_name = node.field_name_for_child(i)
            self.tree_sitter_to_anytree(child, parent=anytree_node, field_name=child_field_name)
        return anytree_node

    def render_tree_as_markdown_text(self):
        """
        Render the tree as markdown-compatible text.
        Include field names and make only named nodes bold.
        """
        from anytree import RenderTree

        def render_node(node):
            # Format each node, making only named nodes bold
            ts_node = node.ts_node
            clss = []
            if node.is_error:
                clss.append("is-error")
            if node.field_name:
                clss.append("has-field-name")
            if node.ts_node.is_named:
                clss.append("is-named")
            if clss:
                open_tag = f"<span class='{' '.join(clss)}'>"
            else:
                open_tag = "<span>"
            close_tag = "</span>"

            return f"{open_tag}{ts_node.type}{close_tag}"

        root = self.tree_sitter_to_anytree(self.tree.root_node)

        lines = []
        for pre, _, node in RenderTree(root):
            # print(pre, _, node)
            # indent = pre.count("│") * 4 * " "  # Indentation based on the level in the tree
            lines.append(f"{pre}{render_node(node)}")

        content = "\n".join(lines)

        css_style = """
            .is-error {
                color: red;
                font-weight: bold;
            }
            
            .has-field-name {
                color: green;
            }
            
            .is-named {
                font-weight: bold;
            }
        """

        return f"""
        <style>
        {css_style}
        </style>
        <pre>
        {content}
        </pre>
        """


class EditorWithTree(pn.viewable.Viewer):
    sample_code_a = pn.widgets.CodeEditor(name="Editor A", language="python", value=sample_a_value)
    sample_code_b = pn.widgets.CodeEditor(name="Editor B", language="python", value=sample_b_value)

    tree_widget_a = pn.pane.HTML(name="Tree A")

    @pn.depends("sample_code_a.value", watch=True)
    def _update_tree_a(self):
        self.tree_widget_a.object = TreeSitterMarkdownRenderer(
            parser.parse(self.sample_code_a.value.encode("utf-8"))
        ).render_tree_as_markdown_text()

    def __panel__(self) -> Viewable:
        return pn.Column(
            pn.Row(self.sample_code_a, self.sample_code_b),
            self.tree_widget_a,
        )


ui = pn.Column(EditorWithTree())

ui.servable()
