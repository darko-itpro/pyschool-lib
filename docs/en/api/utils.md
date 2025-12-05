# Documentation for the pyflix.utils package

The `pyflix.utils` package is intended for displaying `TvShow` objects. It contains two
modules: `cli.py` and `rich_cli.py`. Both have the same two functions. The second is more
*rich* but requires the presence of the `rich` library. The first is a plain text version that can be
used without dependencies.

## `rich_cli` documentation
:::pyflix.utils.rich_cli

## `cli` documentation
:::pyflix.utils.cli

## Usage

This example works the same way with both modules.

```python
import pyflix.utils.rich_cli as cli

my_show = TvShow("Show Name")
my_show.add_episode('Title 1', 1, 1)
my_show.add_episode('Title 2', 1, 2)

cli.display_show(my_show)

shows = {my_show.name:my_show}
cli.display_shows(shows)
```
