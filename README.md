# Un projet pour illustrer le packaging

Ce projet a deux objectifs :
- présenter une application Python prête à être packagée.
- fournir un package avec du code pour les exercices.

Une [documentation est en cours de réalisation](https://darko-itpro.github.io/pyschool-lib/).

## Illustration du packaging
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

## Un projet de support pour les exercices
Vous assistez à ma formation avec un projet pour les exercices. Vous avez été dirigé sur cette
page pour compléter les dépendances. Suivez alors les instructions suivantes.

### Récupérez une archive
Allez sur la page des [releases](https://github.com/darko-itpro/pyschool-lib/releases). Choisissez
la plus récente et sélectionnez le fichier au format wheel. Ceci déclenchera son téléchargement.

### Installez la dépendance
Exécutez simplement en adaptant le numéro de version la commande du type :
```
pip install pyflix-0.2.0-py3-none-any.whl
```

Avec PyCharm, vous pouvez aussi passer par le gestionnaire de dépendances.

### Installation avec les dépendances optionnelles
Vous pouvez installer cette bibliothèque avec ses dépendances optionnelles pour l'invite en ligne
de commande. Utilisez l'instruction suivante :
```
pip install "pyflix-0.2.0-py3-none-any.whl[cli]"
```

Ceci aura pour conséquence d'installer en plus les dépendances optionnelles qui sont référencées
par le *groupe* `cli`. En l'occurence, il s'agit de `rich` et `questionary`.

Voir ci-dessous pour son utilisation

### Durant vos exercices
Les sujets d'exercice feront référence à des packages fournis par cette bibliothèque.

Notez cependant que vous avez deux modules très similaires : `pyflix.utils.cli` et
`pyflix.utils.rich_cli` qui possèdent exactement les mêmes fonctions. La différence est que le
deuxième utilise la bibliothèque [rich](https://rich.readthedocs.io/en/stable/introduction.html)
pour un affichage *riche*. Ces deux modules possèdent les mêmes fonctions afin d'afficher une
série. Pour utiliser le module `pyflix.utils.rich_cli`, vous devez installer la bilbiothèque avec
les dépendances optionnelles comme indiqué ci-dessus. 
