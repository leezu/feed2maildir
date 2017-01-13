{ pkgs ? import <nixpkgs> {} }:

with pkgs;

pythonPackages.buildPythonPackage {
  name = "feed2maildirsimple";
  version = "0.4.0";

  src = ./.;

  propagatedBuildInputs = [
    pythonPackages.python
    pythonPackages.dateutil
    pythonPackages.feedparser
  ];
}
