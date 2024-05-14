# Un projet pour illustrer le packaging

Ce projet a pour objectif de présenter une application Python prête à être packagée.

## Documentation
La documentation principale est : [le Quickstart setuptools](https://setuptools.pypa.io/en/latest/userguide/quickstart.html).

## Étapes
Commencer par installer ou mettre à jour `build` :

```
pip install --upgrade build
```

Le projet doit posséder un fichier `pyproject.toml`. C'est dans ce fichier qu'est paramétré
tout ce qui est nécessaire pour créer l'archive.

L’archive est crée avec la commande
```
python -m build
```
Vous avez alors un répertoire `build`avec une archive `tar.gz` et une `wheel`.

## Installation
En fonction, pour l’installation avec ou sans la dépendance optionnelle :
```
pip install pyflix-0.0.1-py3-none-any.whl
pip install "pyflix-0.0.1-py3-none-any.whl[rich]"
```
