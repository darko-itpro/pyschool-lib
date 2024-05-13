"""
Ce module est une source de données pour les différents exercices.
"""

from pathlib import Path
import random
random.seed()

def load_season(show_name=None, season_number=None):
    file_path = Path(__file__).resolve().parent / "assets" / "bbts12.csv"

    with open(file_path, encoding="utf-8") as bbt_file:
        bbt_file.readline()

        episodes = [_process_line(line) for line in bbt_file]

    return episodes


def get_season(user=None) -> list:
    """
    Fonction permettant d'accéder à la saison d'une série. Sans paramètre (ou avec `None`, retourne
    la liste des titres de la saison. Avec, retourne une liste d'épisodes sous forme de
    dictionnaires.

    Le nombre d'épisodes vus/non vus est aléatoire. Lors de la génération de la liste, chaque
    épisode a 80 % de chances d'être vu. Dès qu'un épisode n'a pas été vu, les suivants sont tous
    non-vus. Un épisode non vu a 60 % de chances de ne pas avoir la clef `viewed`.

    :param user: un identifiant d'utilisateur.
    :return: Si un identifant est donné, une liste d'épisodes où un épisode est représenté par un
    dictionnaire contenant les clefs `title`, `duration` et `viewed`. Si l'épisode n'a pas été vu,
    cette dernière peut être absente.
    """
    file_path = Path(__file__).resolve().parent / "assets" / "bbts12.csv"

    with open(file_path, encoding="utf-8") as bbt_file:
        bbt_file.readline()

        episodes = [_to_dict(*_process_line(line)) for line in bbt_file]

        if user is not None:
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
            if random.random() > 0.6:
                episode['viewed'] = False

def _process_line(episode_line: str):
    """
    Extrait et transtype les données à partir d'une ligne type csv.

    :param episode_line: Une ligne type csv
    :return: Un N-uplet (nom saison, saison, numéro d'épisode, titre d'épisode, durée, année)
    """
    show, season, episode, title, duration, year = episode_line.rstrip().split(';')
    return show, title, int(season), int(episode), int(duration), int(year)


def _to_dict(show, title, season, episode, duration, year):
    episode = {"title": title, "duration": duration}
    return episode
