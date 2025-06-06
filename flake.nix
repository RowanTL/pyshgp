{
  # May not be the most "nix" way to accomplish this, but works for now.
  description = "Basic PyshGP flake";
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };
  outputs = { nixpkgs, ... }:
  let system = "x86_64-linux"; pkgs = import nixpkgs { system = "${system}"; config.allowUnfree = true; }; in
  {
    devShells."${system}".default =
      pkgs.mkShellNoCC {
        buildInputs = [ pkgs.bashInteractive ];
        packages = with pkgs; [
          python311
          python311Packages.pip
          python311Packages.ruff
          (vscode-with-extensions.override {
            vscodeExtensions = with vscode-extensions; [
              ms-python.python
            ];
          })
          jetbrains.pycharm-community
          
          # Add gcc and stdenv for libstdc++
          gcc
          stdenv.cc.cc.lib
          zlib
        ];
        shellHook = ''
          export SHELL=${pkgs.lib.getExe pkgs.bashInteractive}
          
          # Add libstdc++ to LD_LIBRARY_PATH
          # export LD_LIBRARY_PATH=${pkgs.stdenv.cc.cc.lib}/lib:$LD_LIBRARY_PATH
          export LD_LIBRARY_PATH=${pkgs.stdenv.cc.cc.lib}/lib:${pkgs.zlib}/lib:$LD_LIBRARY_PATH
          
          python -m venv .venv
          source .venv/bin/activate
          pip install -r requirements-with-dev.txt
          pip install -e .
        '';
      };
  };
}
