## A project to illustrate the packaging

This project has two objectives:
- to present a Python application ready to be packaged.
- to provide a package with code for the exercises.

A [documentation is currently being written](https://darko-itpro.github.io/pyschool-lib/).

## Packaging illustration
### Documentation

No need to paraphrase, the main documentation is: [the Quickstart setuptools](https://setuptools.pypa.io/en/latest/userguide/quickstart.html).

### Steps
First install or updat `build`:
```
pip install --upgrade build
```

The project must have a `pyproject.toml` file. This file contains the settings for creating the archive.

The archive is created with the command
```
python -m build
```

You will then have a `build` directory with a `tar.gz` archive and a `wheel`.

### Installation
Depending on whether you are installing with or without the optional dependency, the command should
look like this:
```
pip install pyflix-0.0.5-py3-none-any.whl
pip install "pyflix-0.0.5-py3-none-any.whl[cli]"
```

Adjust the section concerning the version number.

## Automation
The project includes a `makefile` file containing several actions:
- `setup`, which automates the installation and updating of dependencies.
- `build`, which automates packaging by repeating the actions described above (excluding
   installation).
- `clean`, which deletes the dist directory and its contents.

In other words, you can create the archive with:

```shell
make build
```
and clean up your project (delete the `dist` directory and its contents) with:
```shell
make clean
```

## Support material for the activities 
You are attending my training course with a project for the activities. You have been directed to this
page to complete the dependencies. Please follow the instructions below.

### Retrieve an archive
Go to the [releases](https://github.com/darko-itpro/pyschool-lib/releases) page. Choose
the most recent one and select the file in wheel format. This will trigger its download.

### Install the dependency
Simply run the command, adapting the version number, as follows:
```
pip install pyflix-0.2.0-py3-none-any.whl
```

With PyCharm, you can also use the dependency manager.

### Installation with optional dependencies
You can install this library with its optional dependencies with the command prompt.

Use the following instruction:
```
pip install "pyflix-0.2.0-py3-none-any.whl[cli]"
```

This will also install the optional dependencies referenced
by the `cli` *group*. In this case, these are `rich` and `questionary`.

See below for how to use it.

### During your activities
Some subjects will refer to packages provided by this library.

Note, however, that you have two very similar modules: `pyflix.utils.cli` and
`pyflix.utils.rich_cli`, which have exactly the same functions. The difference is that the
second one uses the [rich](https://rich.readthedocs.io/en/stable/introduction.html) library
for *rich* display. These two modules have the same functions for displaying a
Tv Show. To use the `pyflix.utils.rich_cli` module, you must install the library with
the optional dependencies as indicated above. 

