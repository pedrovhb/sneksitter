---
file: /home/pedro/Documents/chatgpt_export/Markdown/Fixing libstdc++.so.6 Error.md
heading_stack: <root> -> 8b51c095-d66a-4f7a-991d-3452994aebca -> System -> 61adaf37-62f1-42a5-a9c5-c5a1e7422948 -> System -> aaa20dd9-7a66-4881-98c5-27abc584c5d8 -> User -> ea073fdc-efd4-4cda-8ee5-0493e1c29758 -> Assistant -> 1. Use `nix-shell` to Pull in Required Dependencies: -> 2. Package Your Application with Nix: -> 3. Patching Executables: -> 4. Manually Setting `LD_LIBRARY_PATH`: -> 5. Using `buildFHSUserEnv`:
---
### 5. Using `buildFHSUserEnv`:
As a last resort, you can use `buildFHSUserEnv` to create an isolated environment that mimics a more traditional FHS (Filesystem Hierarchy Standard) Linux environment, which includes these libraries.

Pick the approach that best suits your needs. Since you're well-versed with NixOS, you probably understand the implications of each. Would you like to dive deeper into any of these solutions?

[child ⬇️](#aaa229be-90f4-4b40-9a01-b8a94e259917)

---

(main branch ⎇)
###### aaa229be-90f4-4b40-9a01-b8a94e259917
[parent ⬆️](#ea073fdc-efd4-4cda-8ee5-0493e1c29758)
