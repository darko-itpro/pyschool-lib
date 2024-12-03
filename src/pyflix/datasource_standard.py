"""
Ce module est une source de données pour les différents exercices. Attention à sa configuration.
"""

from pathlib import Path
import random
random.seed()

from .datasource import time_loader, get_movies, get_shows_names, load_show, _to_dict, _is_show, _process_line


def get_start_time() -> str:
    """
    Fonction simulant la collecte de la donnée de temps à partir d'une source de données.
    L'heure retournée est comprise entre '19h00' et '21h38'.
    """
    start_hour = random.randint(19, 21)
    start_minutes = random.randint(0, 59 if start_hour < 21 else 38)

    value = f"{start_hour:02}h{start_minutes:02}"

    return value


def get_season(show_name: str = None, user: str = None) -> list[dict]:
    """
    Fonction permettant d'accéder à la saison d'une série. Sans paramètre (ou avec `None`),
    retourne la liste des titres de la saison. Avec, retourne une liste d'épisodes sous forme
    de dictionnaires.

    Le nombre d'épisodes vus/non vus est aléatoire. Lors de la génération de la liste, chaque
    épisode a 80 % de chances d'être vu. Dès qu'un épisode n'a pas été vu, les suivants sont tous
    non-vus. Un épisode non vu a 60 % de chances de ne pas avoir la clef `viewed`.

    :param show_name: le nom d'une série, si omis, il s'agira de Big Bang Theory
    :param user: un identifiant d'utilisateur.
    :return: Si un identifant est donné, une liste d'épisodes où un épisode est représenté par un
    dictionnaire contenant les clefs `title`, `duration` et `viewed`. Si l'épisode n'a pas été vu,
    cette dernière peut être absente.
    """
    file_path = Path(__file__).resolve().parent / "assets" / "tv_shows.csv"

    with open(file_path, encoding="utf-8") as bbt_file:
        bbt_file.readline()

        if user is None and show_name is None:
            episodes = [_process_line(line)[1]
                        for line in bbt_file
                        if _is_show(line, show_name)]
        elif user is not None:
            episodes = [_to_dict(*_process_line(line))
                        for line in bbt_file
                        if _is_show(line, show_name)]
            _randomize_viewed(episodes)

    return episodes


def _randomize_viewed(season: list) -> None:
    """
    Ajoute de manière aléatoire une clef `viewed` à une liste d'épisodes.

    Un épisode a 80% de chance d'être vu. Dès qu'un épisode n'est pas vu, les suivants sont
    également non-vus. Un épisode non-vu a 60% de chances de ne pas avoir la clef `viewed`.

    :param season: Une liste de dictionnaires
    """
    is_viewed = True

    for episode in season:
        if random.random() > 0.8:
            is_viewed = False

        if is_viewed:
            episode['viewed'] = True
        else:
            if random.random() > 0.4:
                episode['viewed'] = False
