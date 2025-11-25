{
  description = "dev env";
  inputs = {
    nixpkgs.url = "https://flakehub.com/f/NixOS/nixpkgs/0.1"; # tracks nixpkgs unstable branch
    flakelight.url = "github:nix-community/flakelight";
    flakelight.inputs.nixpkgs.follows = "nixpkgs";
  };
  outputs =
    {
      self,
      flakelight,
      ...
    }:
    flakelight ./. {

      devShell = pkgs: {
        packages = [
          pkgs.zlib
          pkgs.postgresql_15
          pkgs.python311
          #(pkgs.python311.withPackages
          #(
          #  ps: with ps; [
          #    pillow
          #    psycopg
          #  ]
          #))
          pkgs.uv
        ];
        env = {
          LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath pkgs.pythonManylinuxPackages.manylinux1;
          DOCKER_HOST = "unix:///run/user/1000/podman/podman.sock";
        };
        shellHook = ''
          unset PYTHONPATH
          uv sync
          #. .venv/bin/activate
        '';
      };

    };
}
