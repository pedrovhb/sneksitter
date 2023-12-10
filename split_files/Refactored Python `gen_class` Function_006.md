---
file: /home/pedro/Documents/chatgpt_export/Markdown/Refactored Python `gen_class` Function.md
heading_stack: <root> -> 479c6063-4851-4e28-b58d-1485da871bb9 -> System -> e2715e40-56c8-4c79-9c73-82243a61a7a8 -> System -> aaa2565e-9a67-4751-adfd-dcd1e2555de6 -> User
---
# User

Pls find mistake:

def gen_class(
    cls_name: str,
    docstring: str | None = None,
    bases: list[str] | None = None,
    members: list[str] | None = None,
) -> str:
    bases_str = ("(" + ", ".join(bases) + ")") if bases else ""
    members_str = "\n".join(members) if members else ""
    docstring_str = f'"""{docstring}"""' if docstring else ""
    if docstring_str and members_str:
        body = f"{docstring_str}\n{members_str}"
    elif docstring_str:
        body = docstring_str
    elif members_str:
        body = members_str
    else:
        body = "pass"
    # Add indentation
    body = "\n    ".join(map(str.strip, body.splitlines()))

    return d(
        f"""
        class {cls_name}{bases_str}:
        {body}
        """
    ).strip()


[child ⬇️](#8e8a47c4-949f-4209-b8cf-827490f09d7b)

---

(main branch ⎇)
###### 8e8a47c4-949f-4209-b8cf-827490f09d7b
[parent ⬆️](#aaa2565e-9a67-4751-adfd-dcd1e2555de6)
