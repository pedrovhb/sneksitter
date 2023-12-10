---
file: /home/pedro/Documents/chatgpt_export/Markdown/Flyweight Metaclass for Models.md
heading_stack: <root> -> 644104e6-eee2-47c9-8b74-983fcdce89aa -> System -> c734da8b-007e-4793-a988-4ab6af4a8c7f -> System -> aaa21a84-fb1c-420d-a200-7e9ff8bd1dca -> User -> cc118a5e-cea7-4eb5-8a55-2d298a0eb3e4 -> Assistant -> aee36206-2846-4af8-97fc-c08ea32d04f7 -> Assistant -> fe5d834e-f4ba-4d75-a77b-b419a41172d6 -> Tool -> 3cc5cb2f-9bf2-4ec7-b730-4b7a6e37379d -> Assistant -> aaa2c0bf-efc0-41ea-9394-4821c3fecdd6 -> User -> 7770a31d-c47b-48a5-9a87-cd318296e663 -> Assistant
---
# Assistant

```python
from dataclasses import dataclass, field
from typing import Any, Dict, Optional, Tuple, Union

# Apply the Flyweight metaclass
@dataclass(frozen=True, eq=True)
class BasicNode(metaclass=FlyweightMeta):
    type: str
    named: bool

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BasicNode":
        return cls(type=data["type"], named=data["named"])


@dataclass(frozen=True, eq=True)
class ChildType(metaclass=FlyweightMeta):
    required: bool
    multiple: bool
    types: Tuple[BasicNode]

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


@dataclass(frozen=True, eq=True)
class Field(metaclass=FlyweightMeta):
    key: str
    type: ChildType


@dataclass(frozen=True, eq=True)
class InternalNode(BasicNode, metaclass=FlyweightMeta):
    fields: Tuple[Field]
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


@dataclass(frozen=True, eq=True)
class SupertypeNode(BasicNode, metaclass=FlyweightMeta):
    subtypes: Tuple[BasicNode]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SupertypeNode":
        return cls(
            type=data["type"],
            named=data["named"],
            subtypes=tuple(
                BasicNode.from_dict(subtype) for subtype in data["subtypes"]
            ),
        )
```

[child ⬇️](#186f96c5-6c2e-4c78-90de-dfcc8ee777fc)

---

(main branch ⎇)
###### 186f96c5-6c2e-4c78-90de-dfcc8ee777fc
[parent ⬆️](#7770a31d-c47b-48a5-9a87-cd318296e663)
