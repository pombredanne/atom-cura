# Atom Cura Configuration

Cura has radically changed its configuration format in 2016, making it
incompatible with previous version.

This repository contains a port of [Atom's original Cura
configuration](http://www.atom3dp.com/wp-content/uploads/2015/06/CURA_ATOMSettings_r3.zip)
to the new format.

## What does it provides?

The configuration provides two files

- [dist/atom.stl](dist/atom.stl), the 3D model for the Atom's bed
- [dist/atom.json](dist/atom.json) the Cura 2.0 printer configuration

## How to install?

### Manually

Copy the [dist/atom.stl](dist/atom.stl) to Cura's `resources/meshes` directory. And
copy the [dist/atom.json](dist/atom.json) to Cura's `marchines` directory. The location
of both directories depend on the operating system.

On Linux, the _meshes_ are installed in `/usr/share/cura/resources/meshes` while
the *printers configurations* are installed in `~/.local/share/cura/machines`.

### Automatically (Linux)

If you have `make` and `cura` installed, you can run

```
make install
```

to automatically install the settings.

