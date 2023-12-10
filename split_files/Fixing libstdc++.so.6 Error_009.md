---
file: /home/pedro/Documents/chatgpt_export/Markdown/Fixing libstdc++.so.6 Error.md
heading_stack: <root> -> 8b51c095-d66a-4f7a-991d-3452994aebca -> System -> 61adaf37-62f1-42a5-a9c5-c5a1e7422948 -> System -> aaa20dd9-7a66-4881-98c5-27abc584c5d8 -> User -> ea073fdc-efd4-4cda-8ee5-0493e1c29758 -> Assistant -> 1. Use `nix-shell` to Pull in Required Dependencies:
---
### 1. Use `nix-shell` to Pull in Required Dependencies:
```bash
nix-shell -p stdenv.cc.cc.lib
```
This command pulls in the C/C++ standard library, including `libstdc++.so.6`. You can then run your application within this shell.

