"""
This file contains the code for generating Python dataclasses from a node-types.json file.

As per tree-sitter's documentation:


## Static Node Types

In languages with static typing, it can be helpful for syntax trees to provide specific type information about individual syntax nodes. Tree-sitter makes this information available via a generated file called `node-types.json`. This _node types_ file provides structured data about every possible syntax node in a grammar.

You can use this data to generate type declarations in statically-typed programming languages. For example, GitHub’s Semantic uses these node types files to generate Haskell data types for every possible syntax node, which allows for code analysis algorithms to be structurally verified by the Haskell type system.

The node types file contains an array of objects, each of which describes a particular type of syntax node using the following entries:

#### Basic Info

Every object in this array has these two entries:

-   `"type"` - A string that indicates which grammar rule the node represents. This corresponds to the `ts_node_type` function described above.
-   `"named"` - A boolean that indicates whether this kind of node corresponds to a rule name in the grammar or just a string literal. See above for more info.

Examples:

```
{
  "type": "string_literal",
  "named": true
}
{
  "type": "+",
  "named": false
}
```

Together, these two fields constitute a unique identifier for a node type; no two top-level objects in the `node-types.json` should have the same values for both `"type"` and `"named"`.

#### Internal Nodes

Many syntax nodes can have _children_. The node type object describes the possible children that a node can have using the following entries:

-   `"fields"` - An object that describes the possible fields that the node can have. The keys of this object are field names, and the values are _child type_ objects, described below.
-   `"children"` - Another _child type_ object that describes all of the node’s possible _named_ children _without_ fields.

A _child type_ object describes a set of child nodes using the following entries:

-   `"required"` - A boolean indicating whether there is always _at least one_ node in this set.
-   `"multiple"` - A boolean indicating whether there can be _multiple_ nodes in this set.
-   `"types"`\- An array of objects that represent the possible types of nodes in this set. Each object has two keys: `"type"` and `"named"`, whose meanings are described above.

Example with fields:

```
{
  "type": "method_definition",
  "named": true,
  "fields": {
    "body": {
      "multiple": false,
      "required": true,
      "types": [{ "type": "statement_block", "named": true }]
    },
    "decorator": {
      "multiple": true,
      "required": false,
      "types": [{ "type": "decorator", "named": true }]
    },
    "name": {
      "multiple": false,
      "required": true,
      "types": [
        { "type": "computed_property_name", "named": true },
        { "type": "property_identifier", "named": true }
      ]
    },
    "parameters": {
      "multiple": false,
      "required": true,
      "types": [{ "type": "formal_parameters", "named": true }]
    }
  }
}
```

Example with children:

```
{
  "type": "array",
  "named": true,
  "fields": {},
  "children": {
    "multiple": true,
    "required": false,
    "types": [
      { "type": "_expression", "named": true },
      { "type": "spread_element", "named": true }
    ]
  }
}
```

#### Supertype Nodes

In Tree-sitter grammars, there are usually certain rules that represent abstract _categories_ of syntax nodes (e.g. “expression”, “type”, “declaration”). In the `grammar.js` file, these are often written as hidden rules whose definition is a simple `choice` where each member is just a single symbol.

Normally, hidden rules are not mentioned in the node types file, since they don’t appear in the syntax tree. But if you add a hidden rule to the grammar’s `supertypes` list, then it _will_ show up in the node types file, with the following special entry:

-   `"subtypes"` - An array of objects that specify the _types_ of nodes that this ‘supertype’ node can wrap.

Example:

```
{
  "type": "_declaration",
  "named": true,
  "subtypes": [
    { "type": "class_declaration", "named": true },
    { "type": "function_declaration", "named": true },
    { "type": "generator_function_declaration", "named": true },
    { "type": "lexical_declaration", "named": true },
    { "type": "variable_declaration", "named": true }
  ]
}
```

Supertype nodes will also appear elsewhere in the node types file, as children of other node types, in a way that corresponds with how the supertype rule was used in the grammar. This can make the node types much shorter and easier to read, because a single supertype will take the place of multiple subtypes.

Example:

```
{
  "type": "export_statement",
  "named": true,
  "fields": {
    "declaration": {
      "multiple": false,
      "required": false,
      "types": [{ "type": "_declaration", "named": true }]
    },
    "source": {
      "multiple": false,
      "required": false,
      "types": [{ "type": "string", "named": true }]
    }
  }
}
```
"""
from __future__ import annotations

import json
import re
import textwrap
from collections import defaultdict
from pathlib import Path
from typing import TypeAlias, NamedTuple

from pydantic import BaseModel, Field

from sneksitter._node_codegen.gen_cls import GenField, GenClass
from sneksitter._node_codegen.sanitize_names import sanitize_identifier

NodeKey: TypeAlias = tuple[str, bool]


class FieldDefinition(NamedTuple):
    name: str
    type: str
    default: str | None


def sanitize_name(node_type: str, node_named: bool, for_class: bool = True) -> str:
    sanitized_name = sanitize_identifier(node_type, for_class=for_class)
    if not node_named:
        sanitized_name = f"{sanitized_name}_A"
    return sanitized_name


class NodeReference(BaseModel):
    type: str
    named: bool

    @property
    def cls_name(self) -> str:
        return sanitize_name(self.type, self.named)


class ChildTypeDefinition(BaseModel):
    required: bool
    multiple: bool
    types: list[NodeReference]

    def __hash__(self) -> int:
        return hash((self.required, self.multiple, tuple(self.types)))

    def as_field(self) -> tuple[str, str | None]:
        if len(self.types) == 1:
            type_str = self.types[0].cls_name
        else:
            type_str = f"T_Union[{', '.join(t.cls_name for t in self.types)}]"

        default = None
        if self.multiple:
            type_str = f"T_Tuple[{type_str}]"
            default = "tuple()"
        elif not self.required:
            type_str = f"T_Optional[{type_str}]"
            default = "None"

        return type_str, default


class SyntaxNodeDefinition(BaseModel):
    type: str
    named: bool
    original_type: str
    original_grammar_id: int
    children: ChildTypeDefinition | None = None
    fields: dict[str, ChildTypeDefinition] = Field(default_factory=dict)
    bases: list[NodeKey] = Field(default_factory=list)

    @property
    def cls_name(self) -> str:
        return sanitize_name(self.type, self.named)

    def as_class(self, additional_bases: list[str] | None = None) -> str:
        fields = [
            GenField("original_node_type", "str", repr(self.original_type), is_classvar=True),
            GenField(
                "original_grammar_id", "int", repr(self.original_grammar_id), is_classvar=True
            ),
        ]
        if self.children is not None:
            type, default = self.children.as_field()
            fields.append(GenField("children", type, default))
        for field_name, field_def in self.fields.items():
            type, default = field_def.as_field()
            fields.append(GenField(field_name, type, default))

        bases = [sanitize_name(base_type, base_named) for base_type, base_named in self.bases]
        if additional_bases is not None:
            bases.extend(additional_bases)

        return GenClass(
            self.cls_name,
            bases=bases,
            fields=fields,
        ).code


class SupertypeNodeDefinition(SyntaxNodeDefinition):
    type: str
    named: bool
    original_type: str
    original_grammar_id: int
    subtypes: list[NodeReference] = Field(default_factory=list)

    def __hash__(self) -> int:
        return hash((self.type, self.named, tuple(self.subtypes)))

    @property
    def cls_name(self) -> str:
        return sanitize_name(self.type, self.named)


def generate_node_types_module(node_types: list[dict], language_name: str) -> str:
    nodes: dict[NodeKey, SyntaxNodeDefinition | SupertypeNodeDefinition] = {}
    # bases = {}

    # Initialize data structures
    base_classes = set()
    node_to_base_classes = defaultdict(set)

    for i, node in enumerate(node_types):
        key = (node["type"], node["named"])
        if "subtypes" in node:
            nodes[key] = SupertypeNodeDefinition(
                **node,
                original_type=node["type"],
                original_grammar_id=i,
            )
            base_classes.add(key)
            for subtype in node["subtypes"]:
                subtype_id = (subtype["type"], subtype["named"])
                node_to_base_classes[subtype_id].add(key)
        else:
            nodes[key] = SyntaxNodeDefinition(
                **node,
                original_type=node["type"],
                original_grammar_id=i,
            )

    # Remove redundant base classes
    for node, bases in node_to_base_classes.items():
        to_remove = set()
        for base in bases:
            to_remove.update(bases.intersection(node_to_base_classes.get(base, set())))
        bases.difference_update(to_remove)

    for node, bases in node_to_base_classes.items():
        nodes[node].bases = list(bases)

    language_cls_name = sanitize_identifier(language_name, for_class=True)
    base_node_cls_name = f"{language_cls_name}Node"

    file_header = f"""\
# This file is autogenerated by sneksitter/_node_codegen/gen_nodes_file.py
# Do not edit this file directly.
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional as T_Optional, Union as T_Union, Tuple as T_Tuple, ClassVar as T_ClassVar

from tree_sitter import Tree, Node


@dataclass(frozen=True, slots=True)
class {base_node_cls_name}:
    language: T_ClassVar[str] = {language_name!r}
    original_node_type: T_ClassVar[str]
    original_grammar_id: T_ClassVar[int]

    _class_mapping: T_ClassVar[dict[str, T_ClassVar[BashNode]]] = {{}}

    original_node: Node | None

    def __init_subclass__(cls):
        super(cls).__init_subclass__()
        cls._class_mapping[cls.original_node_type] = cls

    @classmethod
    def from_tree(cls, node: Tree) -> Program:
        root_node = node.root_node
        assert root_node.type == "program"
        return Program._from_node(root_node)

    @classmethod
    def _from_node(cls, node: Node) -> BashNode | None:
        if not node.is_named:
            return None

        if node.type not in cls._class_mapping:
            print(f"Unknown node type {{node.type!r}}")
            return None
            # raise ValueError(f"Unknown node type {{node.type}}")
        fields = {{"original_node": node}}
        for i in range(node.child_count):
            name = node.field_name_for_child(i)
            new_node = cls._from_node(node.child(i))
            if new_node is not None:
                if name is not None:
                    fields[name] = new_node
                else:
                    fields.setdefault("children", []).append(new_node)

        return cls._class_mapping[node.type](**fields)

    @property
    def text(self) -> bytes:
        return self.original_node.text

"""
    cls_strings = []
    for node in nodes.values():
        cls_strings.append(node.as_class(additional_bases=[base_node_cls_name]))

    file_footer = textwrap.dedent(
        f'''\
        if __name__ == "__main__":
            from tree_sitter_languages import get_language, get_parser
        
            parser = get_parser("{language_name}")
            tree = parser.parse(
                textwrap.dedent(
                    """\
                    #! /bin/env bash
                    echo "Hello World"
                    for i in $(seq 1 10); do
                        echo $i
                    done
                    """
                ).encode("utf-8")
            )
            print(tree.root_node)
        
            bash_tree = {language_cls_name}.from_tree(tree)
            print(bash_tree)
        '''
    )

    file_contents = file_header + "\n\n".join(cls_strings) + "\n\n" + file_footer
    return file_contents


NodeKey: TypeAlias = tuple[str, bool]


class FieldDefinition(NamedTuple):
    name: str
    type: str
    default: str | None


def sanitize_name(node_type: str, node_named: bool, for_class: bool = True) -> str:
    sanitized_name = sanitize_identifier(node_type, for_class=for_class)
    if not node_named:
        sanitized_name = f"{sanitized_name}_A"
    return sanitized_name


class NodeReference(BaseModel):
    type: str
    named: bool

    @property
    def cls_name(self) -> str:
        return sanitize_name(self.type, self.named)


class ChildTypeDefinition(BaseModel):
    required: bool
    multiple: bool
    types: list[NodeReference]

    def __hash__(self) -> int:
        return hash((self.required, self.multiple, tuple(self.types)))

    def as_field(self) -> tuple[str, str | None]:
        if len(self.types) == 1:
            type_str = self.types[0].cls_name
        else:
            type_str = f"T_Union[{', '.join(t.cls_name for t in self.types)}]"

        default = None
        if self.multiple:
            type_str = f"T_Tuple[{type_str}]"
            default = "tuple()"
        elif not self.required:
            type_str = f"T_Optional[{type_str}]"
            default = "None"

        return type_str, default


class SyntaxNodeDefinition(BaseModel):
    type: str
    named: bool
    original_type: str
    original_grammar_id: int
    children: ChildTypeDefinition | None = None
    fields: dict[str, ChildTypeDefinition] = Field(default_factory=dict)
    bases: list[NodeKey] = Field(default_factory=list)

    @property
    def cls_name(self) -> str:
        return sanitize_name(self.type, self.named)

    def as_class(self, additional_bases: list[str] | None = None) -> str:
        fields = [
            GenField("original_node_type", "str", repr(self.original_type), is_classvar=True),
            GenField(
                "original_grammar_id", "int", repr(self.original_grammar_id), is_classvar=True
            ),
        ]
        if self.children is not None:
            type, default = self.children.as_field()
            fields.append(GenField("children", type, default))
        for field_name, field_def in self.fields.items():
            type, default = field_def.as_field()
            fields.append(GenField(field_name, type, default))

        bases = [sanitize_name(base_type, base_named) for base_type, base_named in self.bases]
        if additional_bases is not None:
            bases.extend(additional_bases)

        return GenClass(
            self.cls_name,
            bases=bases,
            fields=fields,
        ).code


class SupertypeNodeDefinition(SyntaxNodeDefinition):
    type: str
    named: bool
    original_type: str
    original_grammar_id: int
    subtypes: list[NodeReference] = Field(default_factory=list)

    def __hash__(self) -> int:
        return hash((self.type, self.named, tuple(self.subtypes)))

    @property
    def cls_name(self) -> str:
        return sanitize_name(self.type, self.named)


def generate_node_types_module(node_types: list[dict], language_name: str) -> str:
    nodes: dict[NodeKey, SyntaxNodeDefinition | SupertypeNodeDefinition] = {}
    # bases = {}

    # Initialize data structures
    base_classes = set()
    node_to_base_classes = defaultdict(set)

    for i, node in enumerate(node_types):
        key = (node["type"], node["named"])
        if "subtypes" in node:
            nodes[key] = SupertypeNodeDefinition(
                **node,
                original_type=node["type"],
                original_grammar_id=i,
            )
            base_classes.add(key)
            for subtype in node["subtypes"]:
                subtype_id = (subtype["type"], subtype["named"])
                node_to_base_classes[subtype_id].add(key)
        else:
            nodes[key] = SyntaxNodeDefinition(
                **node,
                original_type=node["type"],
                original_grammar_id=i,
            )

    # Remove redundant base classes
    for node, bases in node_to_base_classes.items():
        to_remove = set()
        for base in bases:
            to_remove.update(bases.intersection(node_to_base_classes.get(base, set())))
        bases.difference_update(to_remove)

    for node, bases in node_to_base_classes.items():
        nodes[node].bases = list(bases)

    language_cls_name = sanitize_identifier(language_name, for_class=True)
    base_node_cls_name = f"{language_cls_name}Node"

    file_header = f"""\
# This file is autogenerated by sneksitter/_node_codegen/gen_nodes_file.py
# Do not edit this file directly.
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional as T_Optional, Union as T_Union, Tuple as T_Tuple, ClassVar as T_ClassVar

from tree_sitter import Tree, Node


@dataclass(frozen=True, slots=True)
class {base_node_cls_name}:
    language: T_ClassVar[str] = {language_name!r}
    original_node_type: T_ClassVar[str]
    original_grammar_id: T_ClassVar[int]

    _class_mapping: T_ClassVar[dict[str, T_ClassVar[BashNode]]] = {{}}

    original_node: Node | None

    def __init_subclass__(cls):
        super(cls).__init_subclass__()
        cls._class_mapping[cls.original_node_type] = cls

    @classmethod
    def from_tree(cls, node: Tree) -> Program:
        root_node = node.root_node
        assert root_node.type == "program"
        return Program._from_node(root_node)

    @classmethod
    def _from_node(cls, node: Node) -> BashNode | None:
        if not node.is_named:
            return None

        if node.type not in cls._class_mapping:
            print(f"Unknown node type {{node.type!r}}")
            return None
            # raise ValueError(f"Unknown node type {{node.type}}")
        fields = {{"original_node": node}}
        for i in range(node.child_count):
            name = node.field_name_for_child(i)
            new_node = cls._from_node(node.child(i))
            if new_node is not None:
                if name is not None:
                    fields[name] = new_node
                else:
                    fields.setdefault("children", []).append(new_node)

        return cls._class_mapping[node.type](**fields)

    @property
    def text(self) -> bytes:
        return self.original_node.text

"""
    cls_strings = []
    for node in nodes.values():
        cls_strings.append(node.as_class(additional_bases=[base_node_cls_name]))

    file_footer = textwrap.dedent(
        f'''\
        if __name__ == "__main__":
            from tree_sitter_languages import get_language, get_parser

            parser = get_parser("{language_name}")
            tree = parser.parse(
                textwrap.dedent(
                    """\
                    #! /bin/env bash
                    echo "Hello World"
                    for i in $(seq 1 10); do
                        echo $i
                    done
                    """
                ).encode("utf-8")
            )
            print(tree.root_node)

            bash_tree = {language_cls_name}.from_tree(tree)
            print(bash_tree)
        '''
    )

    file_contents = file_header + "\n\n".join(cls_strings) + "\n\n" + file_footer
    return file_contents


if __name__ == "__main__":
    from rich import get_console

    console = get_console()

    node_types_dir = Path(__file__).parent / "node_types"
    broken_languages = {"erlang"}

    for node_types_file in Path(__file__).parent.glob("node_types/*.json"):
        if "bash" not in node_types_file.name:
            continue
        language = re.search(r"node-types-(.+)\.json", node_types_file.name).group(1)
        language = language.replace("-", "_")
        if language in broken_languages:
            print(f"Skipping {language} because it's broken")
            continue

        print(f"Generating node types for {language}")
        node_types = json.loads(node_types_file.read_text())
        file_contents = generate_node_types_module(node_types, language)

        dst_path = Path(__file__).parent / "generated_node_classes" / f"node_types_{language}.py"
        dst_path.parent.mkdir(exist_ok=True)
        dst_path.write_text(file_contents)
        print(f"Generated {dst_path}")

        # todo:
        #  - add a base class to generated classes
        #  - topo sort the definitions by base class
        #  - add a `node` field
