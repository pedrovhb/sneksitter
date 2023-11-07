from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Union, TypeVar, ClassVar, Tuple
import json

RuleT = TypeVar("RuleT", bound="Rule")


@dataclass
class Rule:
    type: ClassVar[str]
    _rule_aliases: ClassVar[Tuple[str, ...]] = ()

    _type_mapping: ClassVar[Dict[str, type]] = {}

    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
        Rule._type_mapping[cls.type] = cls
        for alias in cls._rule_aliases:
            Rule._type_mapping[alias] = cls

    @classmethod
    def from_dict(cls: type[RuleT], data: Dict[str, Union[str, dict]]) -> RuleT:
        return cls._type_mapping[data["type"]].from_dict(data)


@dataclass
class BlankRule(Rule):
    type: ClassVar[str] = "BLANK"

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, dict]]) -> BlankRule:
        return cls()


@dataclass
class StringRule(Rule):
    type: ClassVar[str] = "STRING"
    value: str

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, dict]]) -> StringRule:
        return cls(value=data["value"])


@dataclass
class PatternRule(Rule):
    type: ClassVar[str] = "PATTERN"
    value: str

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, dict]]) -> PatternRule:
        return cls(value=data["value"])


@dataclass
class SymbolRule(Rule):
    type: ClassVar[str] = "SYMBOL"
    name: str

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, dict]]) -> SymbolRule:
        return cls(name=data["name"])


@dataclass
class TreeSitterGrammarSpecification:
    name: str
    rules: Dict[str, Rule]
    extras: Optional[List[Rule]] = None
    externals: Optional[List[Rule]] = None
    inline: Optional[List[str]] = None
    conflicts: Optional[List[List[str]]] = None
    word: Optional[str] = None
    supertypes: Optional[List[str]] = None
    precedences: Optional[List[Dict[str, Union[str, int]]]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, dict]]) -> TreeSitterGrammarSpecification:
        rules = {key: Rule.from_dict(value) for key, value in data["rules"].items()}
        extras = [Rule.from_dict(rule) for rule in data.get("extras", [])]
        externals = [Rule.from_dict(rule) for rule in data.get("externals", [])]
        return cls(
            name=data["name"],
            rules=rules,
            extras=extras,
            externals=externals,
            inline=data.get("inline"),
            conflicts=data.get("conflicts"),
            word=data.get("word"),
            supertypes=data.get("supertypes"),
        )


# Define classmethods for the remaining Rule subclasses in a similar manner.


@dataclass
class SeqRule(Rule):
    type: ClassVar[str] = "SEQ"
    members: List[Rule]

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, dict]]) -> SeqRule:
        members = [Rule.from_dict(member_data) for member_data in data["members"]]
        return cls(members=members)


# Add classmethods for the remaining Rule subclasses in a similar manner.


@dataclass
class ChoiceRule(Rule):
    type: ClassVar[str] = "CHOICE"
    members: List[Rule]

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, dict]]) -> ChoiceRule:
        members = [Rule.from_dict(member_data) for member_data in data["members"]]
        return cls(members=members)


@dataclass
class AliasRule(Rule):
    type: ClassVar[str] = "ALIAS"
    value: str
    named: bool
    content: Rule

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, dict]]) -> AliasRule:
        content = Rule.from_dict(data["content"])
        return cls(value=data["value"], named=data["named"], content=content)


@dataclass
class RepeatRule(Rule):
    type: ClassVar[str] = "REPEAT"
    content: Rule

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, dict]]) -> RepeatRule:
        content = Rule.from_dict(data["content"])
        return cls(content=content)


@dataclass
class Repeat1Rule(Rule):
    type: ClassVar[str] = "REPEAT1"
    content: Rule

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, dict]]) -> Repeat1Rule:
        content = Rule.from_dict(data["content"])
        return cls(content=content)


@dataclass
class TokenRule(Rule):
    type: ClassVar[str] = "TOKEN"
    _rule_aliases: ClassVar[Tuple[str, ...]] = ["IMMEDIATE_TOKEN"]
    content: Rule

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, dict]]) -> TokenRule:
        content = Rule.from_dict(data["content"])
        return cls(content=content)


@dataclass
class FieldRule(Rule):
    name: str
    type: ClassVar[str] = "FIELD"
    content: Rule

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, dict]]) -> FieldRule:
        content = Rule.from_dict(data["content"])
        return cls(name=data["name"], content=content)


@dataclass
class PrecRule(Rule):
    type: ClassVar[str] = "PREC"
    _rule_aliases: ClassVar[Tuple[str, ...]] = (
        "PREC_LEFT",
        "PREC_RIGHT",
        "PREC_DYNAMIC",
    )
    value: int
    content: Rule

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, dict]]) -> PrecRule:
        content = Rule.from_dict(data["content"])
        return cls(value=data["value"], content=content)


# Now, you can create instances from dictionaries like this:
data_dict = {"type": "StringRule", "value": "example"}
symbols: dict[str, Rule] = {}

string_rule = StringRule.from_dict(data_dict)
print(string_rule)  # This will print the created StringRule instance.


def log_recursive_result(func):
    """Print the result of a recursive function call with indentation corresponding
    to the current recursion level."""

    def wrapper(*args, **kwargs):
        # print("  " * wrapper.recursion_level, end="")
        # print(f"Calling {func.__name__} with args {args} and kwargs {kwargs}")
        wrapper.recursion_level += 1
        result = func(*args, **kwargs)
        wrapper.recursion_level -= 1
        print("  " * wrapper.recursion_level, end="")
        print(f"Returning {result}")
        return result

    wrapper.recursion_level = 0
    return wrapper


@log_recursive_result
def parse_rule(rule_name: str, rule_value: Rule) -> str:
    match rule_value:
        case RepeatRule(content):
            return f"List[{parse_rule(rule_name, content)}]"
        case SymbolRule(name):
            symbols[name] = rule_value
            return name
        case ChoiceRule(members):
            is_optional = False
            union_members = [member for member in members if not isinstance(member, BlankRule)]
            if len(union_members) < len(members):
                is_optional = True
            union_str = ", ".join(parse_rule(rule_name, member) for member in union_members)
            if len(union_members) > 1:
                return f"Union[{union_str}]"
            if is_optional:
                return f"Optional[{union_str}]"
            return union_str
        case SeqRule(members):
            tuple_str = ", ".join(parse_rule(rule_name, member) for member in members)
            return f"Tuple[{tuple_str}]"
        case StringRule(value):
            return f"Literal['{value}']"
        case Repeat1Rule(content):
            return f"List[{parse_rule(rule_name, content)}]"

        #     if is_optional and len(members) > 2:
        #         return f"({ored})?"
        #     elif is_optional:
        #         return f"Optional[{ored}]"
        #     return f"({ored})"
        # case SeqRule(members):
        #     return " ".join(parse_rule(rule_name, member) for member in members)
        # case StringRule(value):
        #     return repr(value)
        # case BlankRule():
        #     return "<blank>"
        # case Repeat1Rule(content):
        #     return f"({parse_rule(rule_name, content)})+"
        # case FieldRule(name, content):
        #     return f"{name}={parse_rule(rule_name, content)}"
        # case PrecRule(value, content):
        #     return f"({parse_rule(rule_name, content)}){value}"
        case _:
            raise ValueError(f"Unknown rule type: {rule_value}")


# @log_recursive_result
# def parse_rule(rule_name: str, rule_value: Rule) -> str:
#     match rule_value:
#         case RepeatRule(content):
#             return f"({parse_rule(rule_name, content)})*"
#         case SymbolRule(name):
#             symbols[name] = rule_value
#             return name
#         case ChoiceRule(members):
#             is_optional = any(isinstance(member, BlankRule) for member in members)
#             ored = " | ".join(parse_rule(rule_name, member) for member in members if not isinstance(member, BlankRule))
#             if is_optional and len(members) > 2:
#                 return f"({ored})?"
#             elif is_optional:
#                 return f"{ored}?"
#             return f"({ored})"
#         case SeqRule(members):
#             return " ".join(parse_rule(rule_name, member) for member in members)
#         case StringRule(value):
#             return repr(value)
#         case BlankRule():
#             return "<blank>"
#         case Repeat1Rule(content):
#             return f"({parse_rule(rule_name, content)})+"
#         case FieldRule(name, content):
#             return f"{name}={parse_rule(rule_name, content)}"
#         case PrecRule(value, content):
#             return f"({parse_rule(rule_name, content)}){value}"
#         case _:
#             raise ValueError(f"Unknown rule type: {rule_value}")

# so
# string rules are anonymouses
# symbol rules are named
# choice rules are unions
# seq rules mean list
# blank rules mean optional, when or'd
# repeat rules mean list
# repeat1 rules mean list, min 1
# field rules mean named, a

# so so so
# types contains ~the same info node-types.json would, BUT
# we can also infer non-field anonymous children type from it.
# So we can

# SO
# [<Node type="def", start_point=(1, 0), end_point=(1, 3)>,
#  <Node type=identifier, start_point=(1, 4), end_point=(1, 7)>,
#  <Node type=parameters, start_point=(1, 7), end_point=(1, 9)>,
#  <Node type=":", start_point=(1, 9), end_point=(1, 10)>,
#  <Node type=block, start_point=(2, 4), end_point=(2, 8)>]
# ->
# class FunctionDefinition(Node):
#    ts_node_type: ClassVar[str] = "function_definition"
#    ts_named: ClassVar[bool] = True
#
#    def __init__(self, identifier: Identifier, parameters: Parameters, block: Block, def_: Def_A | None=None, colon: Colon_A | None=None):
#        self.identifier = identifier
#        self.parameters = parameters
#        self.block = block
#
#        self.def_ = Def_A() if def_ is None else def_
#        self.colon = Colon_A() if colon is None else colon
#
#        self.children = (self.def, self.identifier, self.parameters, self.colon, self.block)
#        self.named_children = (self.identifier, self.parameters, self.block)
#
#    @classmethod
#    def from_ts_node(cls, ts_node: Node) -> FunctionDefinition:
#        identifier = Identifier.from_ts_node(ts_node.children[1])
#        parameters = Parameters.from_ts_node(ts_node.children[2])
#        block = Block.from_ts_node(ts_node.children[4])
#        return cls(identifier, parameters, block)

if __name__ == "__main__":
    # with open("ts-python-grammar.json", "r") as fd:
    with open("/home/pedro/Downloads/grammars/css_grammar.json", "r") as fd:
        data = json.load(fd)
        data.pop("PREC", None)
        grammar = TreeSitterGrammarSpecification.from_dict(data)
    import rich

    con = rich.get_console()
    # con.print(grammar)

    for rule_name, rule in grammar.rules.items():
        con.print(f"{rule_name}: {parse_rule(rule_name, rule)}")
