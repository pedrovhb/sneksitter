from collections import defaultdict
from itertools import chain
from pathlib import Path
from typing import List, Union, Optional, Tuple, Dict
from dataclasses import dataclass, field, asdict
from jinja2 import Environment, FileSystemLoader
import json
import logging

from sneksitter._node_codegen.sanitize_names import sanitize_identifier

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@dataclass
class TemplateFieldDefinition:
    name: str
    type: str
    default: Optional[str] = None

    def __post_init__(self) -> None:
        self.name = sanitize_identifier(self.name, for_class=False)


@dataclass
class TemplateSyntaxNodeDefinition:
    type: str
    named: bool
    original_type: str
    original_grammar_id: int
    fields: List[TemplateFieldDefinition]
    bases: List[str]

    def __post_init__(self) -> None:
        # Sort the fields so fields with defaults come last
        self.fields.sort(key=lambda f: f.default is not None)


@dataclass
class TemplateSupertypeNodeDefinition(TemplateSyntaxNodeDefinition):
    subtypes: List[str] = field(default_factory=list)


# Function to populate the templates dataclasses
def populate_template_dataclasses(
    node_types: List[dict], language_name: str
) -> Tuple[List[TemplateSyntaxNodeDefinition], List[TemplateSupertypeNodeDefinition]]:
    logger.debug(f"Populating template dataclasses for {language_name}")

    template_nodes_syntax = []
    template_nodes_supertype = []

    for i, node in enumerate(node_types):
        logger.debug(f"Processing node {i}: {node}")

        fields = []
        if "children" in node:
            type_str, default = child_type_as_field(node["children"])
            fields.append(
                TemplateFieldDefinition(
                    name="named_children",
                    type=type_str,
                    default=default,
                )
            )
        if "fields" in node:
            for field_name, field_def in node["fields"].items():
                logger.debug(f"Processing field {field_name}")

                type_str, default = child_type_as_field(field_def)
                fields.append(
                    TemplateFieldDefinition(name=field_name, type=type_str, default=default)
                )

        if "subtypes" in node:
            subtypes = [sanitize_name(st["type"], st["named"]) for st in node["subtypes"]]
            template_nodes_supertype.append(
                TemplateSupertypeNodeDefinition(
                    type=sanitize_name(node["type"], node["named"]),
                    named=node["named"],
                    original_type=node["type"],
                    original_grammar_id=i,
                    fields=fields,
                    bases=[],
                    subtypes=subtypes,
                )
            )
        else:
            template_nodes_syntax.append(
                TemplateSyntaxNodeDefinition(
                    type=sanitize_name(node["type"], node["named"]),
                    named=node["named"],
                    original_type=node["type"],
                    original_grammar_id=i,
                    fields=fields,
                    bases=[],
                )
            )
    return template_nodes_syntax, template_nodes_supertype


# Function to generate field definitions for templates
def child_type_as_field(child_type: dict) -> Tuple[str, Optional[str]]:
    logger.debug(f"Processing child type: {child_type}")

    if len(child_type["types"]) == 1:
        type_str = sanitize_name(child_type["types"][0]["type"], child_type["types"][0]["named"])
    else:
        type_str = f"T_Union[{', '.join(sanitize_name(t['type'], t['named']) for t in child_type['types'])}]"

    default = None
    if child_type["multiple"]:
        type_str = f"T_Tuple[{type_str}]"
        default = "tuple()"
    elif not child_type["required"]:
        type_str = f"T_Optional[{type_str}]"
        default = "None"

    return type_str, default


def generate_node_types_module(node_types: List[dict], language_name: str) -> str:
    # Generate the entire Python module using the full module template
    full_module_template = env.get_template("node_types_module.py.j2")
    syntax_nodes, supertype_nodes = populate_template_dataclasses(node_types, language_name)
    base_node_cls_name = sanitize_name(f"base_{language_name}_node", True)

    # Build a mapping of node type to base classes
    node_to_base_classes = defaultdict(set)
    for node in supertype_nodes:
        for subtype in node.subtypes:
            node_to_base_classes[subtype].add(node.type)

    # Remove redundant base classes
    for node, bases in node_to_base_classes.items():
        to_remove = set()
        for base in bases:
            to_remove.update(bases.intersection(node_to_base_classes.get(base, set())))
        print(f"Removing {to_remove} from {node}")
        bases.difference_update(to_remove)

    for node in chain(syntax_nodes, supertype_nodes):
        if bases := node_to_base_classes[node.type]:
            node.bases = list(bases)
        else:
            node.bases = [base_node_cls_name]

    generated_full_module_code = full_module_template.render(
        language_name=language_name,
        base_node_cls_name=sanitize_name(f"base_{language_name}_node", True),
        syntax_nodes=[asdict(node) for node in syntax_nodes],
        supertype_nodes=[asdict(node) for node in supertype_nodes],
    )
    return generated_full_module_code


def generate_language_base_visitor_module(node_types: List[dict], language_name: str) -> str:
    # Generate the entire Python module using the full module template
    full_module_template = env.get_template("language_base_visitor.py.j2")
    syntax_nodes, supertype_nodes = populate_template_dataclasses(node_types, language_name)
    base_node_cls_name = sanitize_name(f"base_{language_name}_node", True)

    # Build a mapping of node type to base classes
    node_to_base_classes = defaultdict(set)
    for node in supertype_nodes:
        for subtype in node.subtypes:
            node_to_base_classes[subtype].add(node.type)

    # Remove redundant base classes
    for node, bases in node_to_base_classes.items():
        to_remove = set()
        for base in bases:
            to_remove.update(bases.intersection(node_to_base_classes.get(base, set())))
        print(f"Removing {to_remove} from {node}")
        bases.difference_update(to_remove)

    for node in chain(syntax_nodes, supertype_nodes):
        if bases := node_to_base_classes[node.type]:
            node.bases = list(bases)
        else:
            node.bases = [base_node_cls_name]

    generated_full_module_code = full_module_template.render(
        language_name=language_name,
        base_node_cls_name=sanitize_name(f"base_{language_name}_node", True),
        syntax_nodes=[asdict(node) for node in syntax_nodes],
        supertype_nodes=[asdict(node) for node in supertype_nodes],
    )
    return generated_full_module_code


def sanitize_name(node_type: str, node_named: bool, for_class: bool = True) -> str:
    if not node_type.strip():
        print("Empty node type")
    sanitized_name = sanitize_identifier(node_type, for_class=for_class)
    if not node_named:
        sanitized_name = f"{sanitized_name}_A"
    return sanitized_name


def _main() -> None:
    generated_code_output_dir = Path(__file__).parent / "generated_code"

    for language in "python", "latex", "regex":
        # Load the tree-sitter node-types.json file
        node_types_file = Path(__file__).parent / f"node_types/node-types-{language}.json"
        node_types_json = node_types_file.read_text()
        node_types = json.loads(node_types_json)

        # Generate code from templates
        generated_code_node_types = generate_node_types_module(node_types, language)
        node_types_result_path = generated_code_output_dir / f"{language}_node_types.py"
        node_types_result_path.write_text(generated_code_node_types)
        print(f"Generated code for {language} node types saved to {node_types_result_path}")

        generated_code_base_visitor = generate_language_base_visitor_module(node_types, language)
        base_visitor_result_path = generated_code_output_dir / f"{language}_base_visitor.py"
        base_visitor_result_path.write_text(generated_code_base_visitor)
        print(f"Generated code for {language} base visitor saved to {base_visitor_result_path}")


template_dir = Path(__file__).parent / "templates"
env = Environment(
    loader=FileSystemLoader(template_dir),
    keep_trailing_newline=True,
    trim_blocks=True,
    lstrip_blocks=True,
    autoescape=False,
    auto_reload=True,
)
env.filters["string_literal"] = json.dumps


if __name__ == "__main__":
    _main()
