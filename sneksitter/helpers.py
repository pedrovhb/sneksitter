from textwrap import dedent as d
from tree_sitter import Parser, Node
from tree_sitter_languages import get_parser

from sneksitter.transformer import BaseTransformer
from sneksitter.utils import CodeT, normalize_code


def parse_template_expression(
    template_expression: str | bytes,
    parser: Parser,
    **names: Node,
) -> Node:
    """Parse a template expression and return a Node representing the expression with values interpolated in."""
    if isinstance(template_expression, str):
        template_expression = template_expression.encode()

    filled_template_expression = template_expression.decode().format(**normalized_names)
    return parser.parse(filled_template_expression.encode()).root_node


if __name__ == "__main__":
    template_expression_cls = d(
        """
        @dataclass
        class $cls_name$:
            $cls_attributes$
        """
    )

    class TemplateTransformer(BaseTransformer):
        def __init__(self, parser: Parser, substitutions: dict[str, CodeT]) -> None:
            super().__init__(parser)
            self._is_in_template = False
            self._template_nodes = []
            self.substitutions = substitutions

        def visit_ERROR(self, node: Node) -> None:
            print("ERROR")
            self._is_in_template = True

        def leave_ERROR(self, node: Node) -> CodeT | None:
            self._is_in_template = False
            return ""

        def visit(self, node: Node) -> None:
            if self._is_in_template:
                self._template_nodes.append(node)

        def leave_identifier(self, node: Node) -> CodeT | None:
            if self._is_in_template:
                print(f"Found identifier {node.text.decode()}")
                if sub := self.substitutions.get(node.text.decode()):
                    return sub
                raise ValueError(f"Could not find substitution for {node.text.decode()}")
            return None

    parser = get_parser("python")
    transformer = TemplateTransformer(parser, {"cls_name": "Foo", "cls_attributes": "bar: int"})
    tree = parser.parse(template_expression_cls.encode())
    transformer.traverse(tree.walk())
    print(tree.root_node.text.decode())

    exit()
    template_expression_attr = "{interval_data}: {field_type}"
    template_expression_attr_default = "{interval_data}: {field_type} = {default_value}"

    clss = {
        "Foo": [
            ("some_attribute", "int"),
            ("another_attribute", "str", '"default value"'),
            ("yet_another_attribute", "str", '"default value 2"'),
        ],
        "Bar": [("is_pub", "bool", "False")],
    }

    parser = get_parser("python")

    for cls_name, cls_attributes in clss.items():
        parsed_attrs = []
        for attr in cls_attributes:
            match attr:
                case (attr_name, attr_type):
                    parsed_attrs.append(
                        parse_template_expression(
                            template_expression_attr,
                            parser,
                            field_name=attr_name,
                            field_type=attr_type,
                        )
                    )
                case (attr_name, attr_type, default_value):
                    parsed_attrs.append(
                        parse_template_expression(
                            template_expression_attr_default,
                            parser,
                            field_name=attr_name,
                            field_type=attr_type,
                            default_value=default_value,
                        )
                    )

        cls_attributes_str = "\n".join(node.text.decode() for node in parsed_attrs)

        parsed_cls = parse_template_expression(
            template_expression_cls,
            parser,
            cls_name=cls_name,
            cls_attributes=cls_attributes_str,
        )
        print(parsed_cls.text.decode())


# if templates had to be queries...
