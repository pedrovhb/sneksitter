---
file: /home/pedro/Documents/chatgpt_export/Markdown/Fixing libstdc++.so.6 Error.md
heading_stack: <root> -> 8b51c095-d66a-4f7a-991d-3452994aebca -> System -> 61adaf37-62f1-42a5-a9c5-c5a1e7422948 -> System -> aaa20dd9-7a66-4881-98c5-27abc584c5d8 -> User -> ea073fdc-efd4-4cda-8ee5-0493e1c29758 -> Assistant -> 1. Use `nix-shell` to Pull in Required Dependencies: -> 2. Package Your Application with Nix: -> 3. Patching Executables: -> 4. Manually Setting `LD_LIBRARY_PATH`: -> 5. Using `buildFHSUserEnv`: -> aaa229be-90f4-4b40-9a01-b8a94e259917 -> User
---
# User

I'm running Pycharm, and it keeps happening when I call Python with certain libraries installed. Adding stdenv.cc.cc.lib to the build inputs in the default.nix for Pycharm didn't work. Any other ideas?

with import <nixpkgs> {};
{
  my-pycharm = pkgs.stdenv.mkDerivation rec {
    pname = "jetbrains-pycharm";
    version = "2023.2.1";
  
    src = builtins.fetchurl {
      url = "https://download.jetbrains.com/python/pycharm-professional-${version}.tar.gz";
    };
  
    nativeBuildInputs = [ pkgs.autoPatchelfHook pkgs.makeWrapper ];
    buildInputs = [
      pkgs.jetbrains.jdk
      pkgs.zlib
      pkgs.glib
      pkgs.glibc
      pkgs.libxcrypt
      pkgs.musl
      pkgs.xorg.libX11
      pkgs.xorg.libXi
      pkgs.xorg.libXrender
      pkgs.freetype
      pkgs.alsa-lib
      pkgs.xorg.libXtst
      pkgs.glibc
      pkgs.linux-pam
      pkgs.cups

      pkgs.gcc-unwrapped.lib
      pkgs.gcc
      pkgs.python310
      pkgs.python310Packages.setuptools
      pkgs.python310Packages.pip
      pkgs.poetry
      
      pkgs.python310Packages.black
      pkgs.python310Packages.aiohttp
      
      pkgs.pyright
      pkgs.python310Packages.coverage
      pkgs.python310Packages.pytest
      pkgs.python310Packages.pytest-asyncio

      pkgs.stdenv.cc.cc.lib
    ];
  
    installPhase = ''
      mkdir -p $out/share
      cp -r . $out/share
      rm -r $out/share/jbr
  
      makeWrapper \
        $out/share/bin/pycharm.sh \
        $out/bin/jetbrains-pycharm \
        --prefix LD_LIBRARY_PATH : $out/lib \
        --set GATEWAY_JDK "${pkgs.jdk}" \
        --set JETBRAINSCLIENT_JDK "${pkgs.jetbrains.jdk.home}"
    '';
  };
  
}

[child ⬇️](#3d96fcd1-1912-45ce-86c1-e52ab56c3c23)

---

(main branch ⎇)
###### 3d96fcd1-1912-45ce-86c1-e52ab56c3c23
[parent ⬆️](#aaa229be-90f4-4b40-9a01-b8a94e259917)
