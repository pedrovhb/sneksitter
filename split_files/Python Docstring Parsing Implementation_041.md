---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Docstring Parsing Implementation.md
heading_stack: <root> -> 7cf81549-956c-4cca-93d6-c48821d96908 -> System -> 6476dbd4-7f75-47f1-8b0d-9b56ca8f2c66 -> System -> aaa20e7f-9860-46c5-9c77-d930a71406c3 -> User -> 7d012bc2-71e8-4e41-929e-ddebce0ccb7f -> Assistant -> 7a848fb4-fafb-4120-84f6-6725ea253bc6 -> Assistant -> 9d7c64d3-c964-4f73-8fcc-348a8808245f -> Tool -> 7871c14c-0813-4b57-850e-b8558bb04cdd -> Assistant -> aaa26f25-a8e5-4d20-9881-caea2489d0bc -> User -> 65a2c324-69d9-44db-a6e6-e9fcccbb110b -> Assistant -> 95a4e1ea-8365-4a4f-b155-9f0fe1d7374a -> Tool -> 64ee804e-ca9f-4d24-9cb5-71547925086d -> Assistant -> a57a358d-1f70-48b4-9cb1-3a9843aa8b55 -> Tool -> 6eed57d3-d50a-4638-8473-366254e18a81 -> Assistant -> aaa29656-f7db-49b2-abf5-aa1e8ac5f3e0 -> User -> 429ae43b-adb5-4d66-a796-74c34d8064b2 -> Assistant -> Plan for Parsing and Unparsing Google-Style Docstrings -> Overview -> Components of a Google-Style Docstring -> Data Classes -> Approaches -> Parsing -> Unparsing -> Selected Approaches -> Parsing: Line-by-Line Parsing -> Unparsing: Dynamic Generation -> Special Cases
---
### Special Cases

1. **Indentation**: Google-style docstrings are sensitive to indentation, especially in the `Examples` section.
2. **Empty Sections**: Ignore sections that have no content.
3. **Type Annotations**: Handle both single types (`int`) and complex types (`List[int]`).
