#### Transitions

- `START -> POSITIONAL_ONLY`: On encountering `/`
- `START -> VARARGS`: On encountering `*args` or `*`
- `POSITIONAL_ONLY -> VARARGS`: On encountering `*args` or `*`
- `VARARGS -> KWARGS`: On encountering `**kwargs`

