#### States

1. `START`: Initial state before any parameter is processed.
2. `POSITIONAL_ONLY`: After encountering `/`, all parameters must be positional-only.
3. `VARARGS`: After encountering `*args` or `*`, which implies that subsequent parameters should be keyword-only.
4. `KWARGS`: After encountering `**kwargs`.

