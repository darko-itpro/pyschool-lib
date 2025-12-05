# Packaging

## What is a package?
A Python package is, in short, a bundle of Python code compressed into a file with a specific format 
that allows it to be distributed to others and installed with a tool such as pip.

We currently have two types of archives:

 * Source packages in `.tar.gz` format, which are snapshots of the sources accompanied by a
   manifest file and metadata.
 * Packages in *Wheel* format (`.whl`), which are an improvement on `Egg` and are therefore the current format.
   They can contain precompiled extensions.

## The *new* standards
The current standards for specifying metadata use the `pyproject.toml` file and a
backend. They are based on [PEP 517](https://peps.python.org/pep-0517/) and
[PEP 621](https://peps.python.org/pep-0621/).

## The pyproject.toml file
PyPA maintains [the technical specifications](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
for the `pyproject.toml` file as well as a more functional document for
[writing your pyproject.toml](https://packaging.python.org/en/latest/specifications/pyproject-toml/#pyproject-toml-spec). 

## Creating a package, the *standard* tools
### Documentation
No need to paraphrase it, the main documentation is: [the setuptools Quickstart](https://setuptools.pypa.io/en/latest/userguide/quickstart.html).

### Prerequisites
The project must have a `pyproject.toml` file. This configuration file contains all the
information needed to create the archive.

### Steps
Start by installing or updating `build`:
```
pip install --upgrade build
```

The package is created with:
```
python -m build
```
You will then have a `build` directory with a `tar.gz` archive and a `wheel`.

## Creating a package with uv
uv is a recent project and dependency management tool.

With uv, simply run:
```
uv build
```

uv will retrieve the dependencies if necessary.

## Installing the package
Depending on whether you are installing with or without the optional dependency, the command should
look like this:
```
pip install pyflix-0.0.5-py3-none-any.whl
pip install "pyflix-0.0.5-py3-none-any.whl[cli]"
```

Adapt the line according to your version number.

## Automation
The project includes a `makefile` file which containing several actions:

 - `.venv/bin/activate`: automates the installation and updating of dependencies with `pip`.
 - `build`: automates packaging by running the actions described above using
  standard tools.
 - `clean`: deletes the `dist` directory and its contents.

The makefile is designed to rely only on standard Python tools, the first two commands
use pip and setuptools.

In other words, you can create the archive with:
```shell
make build
```

and clean up your project (delete the `dist` directory and its contents) with :
```shell
make clean
```