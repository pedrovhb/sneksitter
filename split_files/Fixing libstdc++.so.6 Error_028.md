---
file: /home/pedro/Documents/chatgpt_export/Markdown/Fixing libstdc++.so.6 Error.md
heading_stack: <root> -> 8b51c095-d66a-4f7a-991d-3452994aebca -> System -> 61adaf37-62f1-42a5-a9c5-c5a1e7422948 -> System -> aaa20dd9-7a66-4881-98c5-27abc584c5d8 -> User -> ea073fdc-efd4-4cda-8ee5-0493e1c29758 -> Assistant -> 1. Use `nix-shell` to Pull in Required Dependencies: -> 2. Package Your Application with Nix: -> 3. Patching Executables: -> 4. Manually Setting `LD_LIBRARY_PATH`: -> 5. Using `buildFHSUserEnv`: -> aaa229be-90f4-4b40-9a01-b8a94e259917 -> User -> 3d96fcd1-1912-45ce-86c1-e52ab56c3c23 -> Assistant -> 1. Update `LD_LIBRARY_PATH` within PyCharm -> 2. Use Nix-Managed Python Interpreter -> 3. Patch the Python Interpreter -> 4. Use `nix-shell` as Interpreter -> 5. Additional `makeWrapper` Arguments -> aaa2405d-e594-4acb-add9-d482301c177a -> User -> 60e5b9c9-2cf6-40b5-849f-a96661727c48 -> Assistant -> 1. Custom `nix-shell` Environment -> 2. Patching `RPATH` on the Fly
---
### 2. Patching `RPATH` on the Fly
You could write a small wrapper script to patch the `RPATH` of the Python shared object files inside the virtual environment. This is a more automated approach but requires extra setup.

