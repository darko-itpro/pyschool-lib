# Create PyFlix data

## Create a Tv Show with data
During your training, you will end up creating a class `TvShow(self, name:str)` with a method
`add_episode(self, title, season_number, number, duration, year`. You can load data
using this module's data source.

### Retrieve the names of available shows
```python
import pyflix.datasource as ds

print(ds.get_shows_names())
```

### Retrieve the episodes of of a given show
```python
import pyflix.datasource as ds

for episode in ds.load_show():
    print(episode)

for episode in ds.load_show(ds.get_shows_names()[0]):
    print(episode)
```

### Create a `TvShow` object with its episodes
```python
import pyflix.datasource as ds

show_name = ds.get_shows_names()[0]
my_show = TvShow(show_name)

for ep_data in ds.load_show(show_name):
    my_show.add_episode(*ep_data[1:])
```