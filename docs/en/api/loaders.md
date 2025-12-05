# Documentation for the pyflix.loaders package

The `pyflix.loaders` package contains a `file_helpers` module that allows you to load episode information
from a CSV file or video file names.

## Details of the `load_from_csv` function
The `load_from_csv` function loads data from a csv file. The separator must be
a semicolon (`;`) and the file must have the following header:

| "tvshow"   | "season" | "ep_number" | "ep_title" | "duration" | "year" |
|------------|---|---|---|---|---|

## Details of the `load_from_filenames` function
The `load_from_filenames` function extracts information from the video file name.
The file name must have the following structure: `series_name-sXXeYY-episode_title.ext`.

 * `series_name` is a string containing the name of the series. The `_` will be replaced by
   spaces.
 * `XX` is an integer representing the season number with 2 digits. Season 1 will be `01`.
 * `YY` is an integer representing the episode number with 2 digits. Episode 1 will be `01`.
 * `episode_title` is a string containing the episode title. The `_` will be replaced by
   spaces.

---
:::pyflix.loaders.file_helpers