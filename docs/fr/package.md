# Le packaging

## Qu'est-ce qu'un package ?
Un *package Python* est, sommairement, un *bundle* de code Python compressé dans un fichier au
format particulier qui permet d'être diffusé à d'autres personnes et d'être installé avec un outil
comme `pip`.

Nous avons actuellement 2 type d'archives :

 * Les packages de sources au format `.tar.gz` qui est un instantané des sources accompagnées d'un
   fichier manifest et de métadonnées.
 * Un package au format *Wheel* (`.whl`) qui est une amélioration des `Egg` et donc le format
   actuel. Il peut contenir des extensions précompilées.

## Les *nouveaux* standards
Les standards actuels pour spécifier les métadonnées utilisent le fichier `pyproject.toml` et un
backend. Ils reposent sur les [PEP 517](https://peps.python.org/pep-0517/) et
[PEP 621](https://peps.python.org/pep-0621/).

## Le fichier pyproject.toml
La PyPA maintient [les spécifications techniques](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
du fichier `pyproject.toml` ainsi qu'un document plus fonctionnel pour
[écrire votre pyproject.toml](https://packaging.python.org/en/latest/specifications/pyproject-toml/#pyproject-toml-spec). 

## Création d'un package, les outils *standards*
### Documentation
Innutile de la paraphraser, la documentation principale est : [le Quickstart setuptools](https://setuptools.pypa.io/en/latest/userguide/quickstart.html).

### Prérequis
Le projet doit posséder un fichier `pyproject.toml`. Ce fichier de paramétrage contient toutes les
informations pour créer l'archive.

### Étapes
Commencez par installer ou mettre à jour `build` :

```
pip install --upgrade build
```

L’archive est créée avec la commande :
```
python -m build
```
Vous avez alors un répertoire `build`avec une archive `tar.gz` et une `wheel`.

## Création d'un package, avec uv
uv est un outil récent de gestion de projet et de dépendances.

Avec uv, exécutez simplement :
```
uv build
```

uv récupérera les dépendances si nécessaire.

## Installation du package
En fonction, pour l’installation avec ou sans la dépendance optionnelle, l'instruction doit
ressembler à :
```
pip install pyflix-0.0.5-py3-none-any.whl
pip install "pyflix-0.0.5-py3-none-any.whl[cli]"
```

Adaptez la partie concernant le numéro de version.

## Automatisation
Le projet inclut un fichier `makefile` comportant plusieurs actions :

 - `.venv/bin/activate` : automatise l'installation et la mise à jour des dépendances avec `pip`.
 - `build` : automatise le packaging en reprenant les actions décrites plus haut en utilisant
   les outils *standard*.
 - `clean` : supprime le répertoire `dist` et son contenu.

Le makefile se veut ne reposer que sur les outils standards de Python, les deux premières commandes
utilisent pip et setuptools.

En d'autres termes, vous pouvez créer l'archive avec :
```shell
make build
```

et nettoyer votre projet (supprimer le répertoire `dist` et son contenu) avec :
```shell
make clean
```