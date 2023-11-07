from dataclasses import dataclass
from typing import NamedTuple

from libcst.helpers import (
    parse_template_statement,
    parse_template_expression,
    parse_template_module,
)
import libcst as cst
from pydantic import BaseModel

template_class = """\
@dataclass(frozen=True, slots=True)
class {cls_name}:
    {body}
"""


template_field_default = """\
{field_name} = {field_value}
"""

template_field_annotated = """\
{field_name}: {field_type}
"""

template_field_annotated_default = """\
{field_name}: {field_type} = {field_value}
"""

template_field_classvar = """\
{field_name}: T_ClassVar[{field_type}] = {field_value}
"""


@dataclass
class GenField:
    name: cst.Name | str
    type: cst.BaseExpression | str | None = None
    default: cst.BaseExpression | str | None = None
    is_classvar: bool = False

    def __post_init__(self):
        if self.is_classvar:
            if self.type is None or self.default is None:
                raise ValueError("ClassVar fields must have a type and a default value.")

        if isinstance(self.name, str):
            self.name = cst.Name(self.name)
        if isinstance(self.type, str):
            self.type = cst.parse_expression(self.type)
        if isinstance(self.default, str):
            self.default = cst.parse_expression((self.default))

    @property
    def statement(self) -> cst.SimpleStatementLine:
        if self.is_classvar:
            return parse_template_statement(
                template_field_classvar,
                field_name=self.name,
                field_type=self.type,
                field_value=self.default,
            )

        if self.type is None:
            return parse_template_statement(
                template_field_default, field_name=self.name, field_value=self.default
            )
        elif self.default is None:
            return parse_template_statement(
                template_field_annotated, field_name=self.name, field_type=self.type
            )
        else:
            return parse_template_statement(
                template_field_annotated_default,
                field_name=self.name,
                field_type=self.type,
                field_value=self.default,
            )


@dataclass
class GenClass:
    name: cst.Name | str
    bases: list[cst.Name | str] = None
    fields: list[GenField] = None

    def __post_init__(self):
        if isinstance(self.name, str):
            self.name = cst.Name(self.name)
        if self.bases is not None:
            self.bases = [cst.Name(base) if isinstance(base, str) else base for base in self.bases]
        if self.fields is None:
            self.fields = []

        # Sort fields so that classvars come first, and non-classvars with defaults come last.
        self.fields.sort(key=lambda field: (field.is_classvar, field.default is not None))

    @property
    def statement(self) -> cst.ClassDef:
        if self.bases is None:
            return cst.ensure_type(
                parse_template_statement(template_class, cls_name=self.name, body=self.body),
                cst.ClassDef,
            )
        else:
            cls_obj = cst.ensure_type(
                parse_template_statement(
                    template_class,
                    cls_name=self.name,
                    body=cst.IndentedBlock(body=[field.statement for field in self.fields]),
                ),
                cst.ClassDef,
            )
            return cls_obj.with_changes(bases=[cst.Arg(base) for base in self.bases])

    @property
    def code(self) -> str:
        return cst.Module(body=[self.statement]).code


if __name__ == "__main__":
    name = cst.Name("Foo")
    fields = [
        GenField(name=cst.Name("a"), type=cst.Name("int"), default=cst.Integer("4")),
        GenField(name=cst.Name("b"), type=cst.Name("str"), default=cst.SimpleString(repr(""))),
        GenField(
            name="c",
            type="list[float]",
            default="4.0",
            is_classvar=True,
        ),
    ]
    cls = GenClass(name=name, fields=fields, bases=["BaseModel"])
    module = cst.Module(body=[cls.statement])
    print(module.code)
