---
file: /home/pedro/Documents/chatgpt_export/Markdown/Flyweight Metaclass for Models.md
heading_stack: <root> -> 644104e6-eee2-47c9-8b74-983fcdce89aa -> System -> c734da8b-007e-4793-a988-4ab6af4a8c7f -> System -> aaa21a84-fb1c-420d-a200-7e9ff8bd1dca -> User
---
# User

So I have this structure:



@dataclass(frozen=True)
class BasicNode:
    type: str
    named: bool

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BasicNode":
        return cls(type=data["type"], named=data["named"])


@dataclass(frozen=True)
class ChildType:
    required: bool
    multiple: bool
    types: tuple[BasicNode]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ChildType":
        return cls(
            required=data.get("required", False),
            multiple=data.get("multiple", False),
            types=tuple(BasicNode.from_dict(t) for t in data["types"]),
        )

    def as_annotation(self) -> str:
        if len(self.types) == 1:
            t = self.types[0].type
        else:
            t = f"Union[{', '.join(t.type for t in self.types)}]"

        if self.multiple:
            t = f"List[{t}]"
        if not self.required:
            t = f"Optional[{t}]"
        return t


@dataclass(frozen=True)
class Field:
    key: str
    type: ChildType


@dataclass(frozen=True)
class InternalNode(BasicNode):
    fields: tuple[Field]
    children: Optional[ChildType]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "InternalNode":
        fields = tuple(
            Field(k, ChildType.from_dict(v)) for k, v in data.get("fields", {}).items()
        )
        children = (
            ChildType.from_dict(data.get("children", {}))
            if data.get("children")
            else None
        )
        return cls(
            type=data["type"],
            named=data["named"],
            fields=fields,
            children=children,
        )


@dataclass(frozen=True)
class SupertypeNode(BasicNode):
    subtypes: tuple[BasicNode]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SupertypeNode":
        return cls(
            type=data["type"],
            named=data["named"],
            subtypes=tuple(
                BasicNode.from_dict(subtype) for subtype in data["subtypes"]
            ),
        )


I'd like to come up with a base class or metaclass which automatically implements the flyweight pattern with the combination of its attributes.

[child ⬇️](#cc118a5e-cea7-4eb5-8a55-2d298a0eb3e4)

---

(main branch ⎇)
###### cc118a5e-cea7-4eb5-8a55-2d298a0eb3e4
[parent ⬆️](#aaa21a84-fb1c-420d-a200-7e9ff8bd1dca)
