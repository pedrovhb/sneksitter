---
file: /home/pedro/Documents/chatgpt_export/Markdown/Fixing libstdc++.so.6 Error.md
heading_stack: <root> -> 8b51c095-d66a-4f7a-991d-3452994aebca -> System -> 61adaf37-62f1-42a5-a9c5-c5a1e7422948 -> System -> aaa20dd9-7a66-4881-98c5-27abc584c5d8 -> User -> ea073fdc-efd4-4cda-8ee5-0493e1c29758 -> Assistant
---
# Assistant

The error `OSError: libstdc++.so.6: cannot open shared object file: No such file or directory` usually occurs when the system is unable to locate the `libstdc++.so.6` shared library. This library is a part of the GNU Compiler Collection (GCC) and is commonly required for running applications compiled with `g++`.

In NixOS, this can be a bit tricky because the system adheres to a purely functional deployment model. Libraries aren't stored in global, standard directories like `/usr/lib` or `/usr/local/lib`. Instead, each package lives in its own isolated directory in the Nix store, and symlinks are created to stitch everything together.

Here are some potential solutions:

### 1. Use `nix-shell` to Pull in Required Dependencies:
```bash
nix-shell -p stdenv.cc.cc.lib
```
This command pulls in the C/C++ standard library, including `libstdc++.so.6`. You can then run your application within this shell.

### 2. Package Your Application with Nix:
If you're developing an application, you can specify `gcc` or `stdenv.cc.cc.lib` as a build input in your `default.nix`, so that the `libstdc++.so.6` dependency is handled automatically.

### 3. Patching Executables:
Use `patchelf` to set the `RPATH` of the binary to point to the directory containing `libstdc++.so.6`.

```bash
patchelf --set-rpath 'path/to/libstdc++.so.6' /path/to/your/program
```

### 4. Manually Setting `LD_LIBRARY_PATH`:
Though not recommended, especially not on NixOS, you can manually set `LD_LIBRARY_PATH` to include the directory containing `libstdc++.so.6`.

```bash
export LD_LIBRARY_PATH=/path/to/libstdc++.so.6:$LD_LIBRARY_PATH
```

### 5. Using `buildFHSUserEnv`:
As a last resort, you can use `buildFHSUserEnv` to create an isolated environment that mimics a more traditional FHS (Filesystem Hierarchy Standard) Linux environment, which includes these libraries.

Pick the approach that best suits your needs. Since you're well-versed with NixOS, you probably understand the implications of each. Would you like to dive deeper into any of these solutions?

[child ⬇️](#aaa229be-90f4-4b40-9a01-b8a94e259917)

---

(main branch ⎇)
###### aaa229be-90f4-4b40-9a01-b8a94e259917
[parent ⬆️](#ea073fdc-efd4-4cda-8ee5-0493e1c29758)
