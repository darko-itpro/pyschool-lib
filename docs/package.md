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

### Documentation
Innutile de la paraphraser, la documentation principale est : [le Quickstart setuptools](https://setuptools.pypa.io/en/latest/userguide/quickstart.html).

### Étapes
Commencer par installer ou mettre à jour `build` :

```
pip install --upgrade build
```

Le projet doit posséder un fichier `pyproject.toml`. C'est dans ce fichier un fichier de
paramétrage pour créer l'archive.

L’archive est créée avec la commande
```
python -m build
```
Vous avez alors un répertoire `build`avec une archive `tar.gz` et une `wheel`.

### Installation
En fonction, pour l’installation avec ou sans la dépendance optionnelle, l'instruction doit
ressembler à :
```
pip install pyflix-0.0.5-py3-none-any.whl
pip install "pyflix-0.0.5-py3-none-any.whl[cli]"
```

Adaptez la partie concernant le numéro de version.

## Automatisation
Le projet inclut un fichier `makefile` comportant plusieurs actions :
 - `setup` qui atomatise l'installation et la mise à jour des dépendances.
 - `build` qui automatise le packaging en reprenant les actions décrites plus haut (hors
   installation).
 - `clean` qui supprime le répertoire dist et son contenu.

En d'autres termes, vous pouvez créer l'archive avec :
```shell
make build
```

et néttoyer votre projet (supprimer le répertoire `dist` et son contenu) avec :
```shell
make clean
```