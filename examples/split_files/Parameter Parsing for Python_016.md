# Assistant

```python
# Reproducing the existing code to align our environments.

from __future__ import annotations
from dataclasses import dataclass
from textwrap import dedent as d

import rich
import tree_sitter_languages
from pydantic import Field, BaseModel
from tree_sitter import Node

# Will implement the utils function later
# from codecranker.code_editing.utils import print_tree


class Model(BaseModel):
    class Config:
        extra = "forbid"


class Parameter(Model):
    name: bytes = Field(..., description="The name (identifier) of the parameter.")
    type: bytes | None = Field(
        None,
        description="The type annotation of the parameter, the same as it was present in the code (if at all).",
    )
    default: bytes | None = Field(
        None,
        description="The default value of the parameter, if any.",
    )
    description: str | None = Field(
        None,
        description="The description of the parameter, from the docstring.",
    )
    is_vararg: bool = Field(
        False,
        description="Whether the parameter is a vararg (e.g. *args).",
    )
    is_kwarg: bool = Field(
        False,
        description="Whether the parameter is a kwarg (e.g. **kwargs).",
    )
    is_positional_only: bool = Field(
        False,
        description="Whether the parameter is positional only (e.g. def foo(x, /, y)).",
    )
    is_keyword_only: bool = Field(
        False,
        description="Whether the parameter is keyword only (e.g. def foo(*, x)).",
    )

    @classmethod
    def from_node(
        cls,
        node: Node,
        description: str | None = None,
    ) -> Parameter:
        pass

    @classmethod
    def from_node_parameters(cls, node: Node) -> list[Parameter]:
        pass

# Placeholder for the main code block
if __name__ == "__main__":
    pass
```

[child ⬇️](#0d50a4ea-44f5-46a4-9e57-e850767a7394)

---

(main branch ⎇)
###### 0d50a4ea-44f5-46a4-9e57-e850767a7394
[parent ⬆️](#5c7e3ab1-2c64-4a6e-b418-7363f9260940)
