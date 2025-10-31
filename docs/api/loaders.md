# Documentation du package pyflix.loaders

Le package `pyflix.loaders` contient un module `file_helpers` qui permet de charger les informations
d'épisodes à partir d'un fichier csv ou de noms de fichiers vidéo.

## Détails de la fonction `load_from_csv`
La fonction `load_from_csv` charge les données à partir d'un fichier csv. Le séparateur doit être
le point-virgule (`;`) et le fichier doit avoir l'en-tête :

| "tvshow"   | "season" | "ep_number" | "ep_title" | "duration" | "year" |
|------------|---|---|---|---|---|

## Détails de la fonction `load_from_filenames`
la fonction `load_from_filenames` extrait les informations à partir du nom du fichier vidéo.
Celui-ci doit avoir la structure : `nom_serie-sXXeYY-titre_episode.ext`.

 * `nom_serie` est une chaine contenant le nom de la série, les `_` seront remplacés par des
   espaces.
 * `XX` est un entier représentant le numéro de la saison sur 2 digits. La saison 1 sera `01`.
 * `YY` est un entier représentant le numéro de l'épisode sur 2 digits. L'épisode 1 sera `01`.
 * `titre_episode` est une chaine contenant le titre de l'épisode, les `_` seront remplacés par des
   espaces.

---
:::pyflix.loaders.file_helpers