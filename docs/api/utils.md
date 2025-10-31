from pyflix.media_db import TvShow

# Documentation du package pyflix.utils

Le package `pyflix.utils` est destiné à l'affichage d'objets de type `TvShow`. Il contient 2
modules : `cli.py` et `rich_cli.py`. Les deux ont les mêmes deux fonctions. Le second est plus
*riche* mais nécessite la présence de la bibliothèque `rich`. Le premier est une version pur texte
utilisable sans dépendance.


## Documentation du module `rich_cli`
:::pyflix.utils.rich_cli

## Documentation du module `cli`
:::pyflix.utils.cli

## Exemple d'usage

Cet exemple fonctionne de la même manière avec les deux modules.

```python
import pyflix.utils.rich_cli as cli

my_show = TvShow("Show Name")
my_show.add_episode('Title 1', 1, 1)
my_show.add_episode('Title 2', 1, 2)

cli.display_show(my_show)

shows = {my_show.name:my_show}
cli.display_shows(shows)
```
