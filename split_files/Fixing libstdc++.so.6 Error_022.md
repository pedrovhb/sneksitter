---
file: /home/pedro/Documents/chatgpt_export/Markdown/Fixing libstdc++.so.6 Error.md
heading_stack: <root> -> 8b51c095-d66a-4f7a-991d-3452994aebca -> System -> 61adaf37-62f1-42a5-a9c5-c5a1e7422948 -> System -> aaa20dd9-7a66-4881-98c5-27abc584c5d8 -> User -> ea073fdc-efd4-4cda-8ee5-0493e1c29758 -> Assistant -> 1. Use `nix-shell` to Pull in Required Dependencies: -> 2. Package Your Application with Nix: -> 3. Patching Executables: -> 4. Manually Setting `LD_LIBRARY_PATH`: -> 5. Using `buildFHSUserEnv`: -> aaa229be-90f4-4b40-9a01-b8a94e259917 -> User -> 3d96fcd1-1912-45ce-86c1-e52ab56c3c23 -> Assistant -> 1. Update `LD_LIBRARY_PATH` within PyCharm -> 2. Use Nix-Managed Python Interpreter -> 3. Patch the Python Interpreter -> 4. Use `nix-shell` as Interpreter -> 5. Additional `makeWrapper` Arguments
---
### 5. Additional `makeWrapper` Arguments
In your `installPhase`, you're setting `LD_LIBRARY_PATH` for the `jetbrains-pycharm` wrapper script. You might also try adding the path to `libstdc++.so.6` here.

```nix
makeWrapper \
  $out/share/bin/pycharm.sh \
  $out/bin/jetbrains-pycharm \
  --prefix LD_LIBRARY_PATH : ${stdenv.cc.cc.lib}/lib:$out/lib \
  --set GATEWAY_JDK "${pkgs.jdk}" \
  --set JETBRAINSCLIENT_JDK "${pkgs.jetbrains.jdk.home}"
```

Note: Replace `${stdenv.cc.cc.lib}/lib` with the actual path where `libstdc++.so.6` resides.

Would you like to explore any of these options in more detail?

[child ⬇️](#aaa2405d-e594-4acb-add9-d482301c177a)

---

(main branch ⎇)
###### aaa2405d-e594-4acb-add9-d482301c177a
[parent ⬆️](#3d96fcd1-1912-45ce-86c1-e52ab56c3c23)
