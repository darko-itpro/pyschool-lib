# Créer des données PyFlix

## Créer une série avec des données
Durant la formation, vous finirez par créer une class `TvShow(self, name:str)` possédant une méthode
`add_episode(self, title, season_number, number, duration, year`. vous pouvez charger des données
grâce à la datasource de ce module.

### Récupérez le nom des séries disponibles
```python
import pyflix.datasource as ds

print(ds.get_shows_names())
```

### Récupérez les épisodes pour une série
```python
import pyflix.datasource as ds

for episode in ds.load_show(): # Liste tous les épisodes de toutes les séries
    print(episode)

for episode in ds.load_show(ds.get_shows_names()[0]): # Liste les épisodes pour la première série.
    print(episode)
```

### Créer un objet `TvShow` alimenté
```python
import pyflix.datasource as ds

show_name = ds.get_shows_names()[0]
my_show = TvShow(show_name)

for ep_data in ds.load_show(show_name):
    my_show.add_episode(*ep_data[1:])
```