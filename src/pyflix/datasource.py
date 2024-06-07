"""
Ce module est une source de données pour les différents exercices. Attention à sa configuration.

Ce module est destiné à être utilisé dans plusieurs formations et donc avec des niveaux de
compétences différents. Pour répondre à ce besoin, il est possible de modifier le comportement
en faisant appel à la fonction `datasource.set_level(level)`. Le paramètre est une des valeurs de
l'enum `datasource.Level` :
 - datasource.Level.NOOBS est le niveau débutant, c'est aussi le niveau par défaut.
 - datasource.Level.STANDARD est destiné aux formations Python standard.
 - datasource.Level.XPERT est un niveau qui peut être activé pour des données plus complexes.
 - datasource.Level.HACKER est le niveau à utiliser si vous voulez du challenge.
"""

from pathlib import Path
import random
from enum import Enum
random.seed()


class Level(Enum):
    """
    Enum permetant de configurer le niveau du module.
    """
    NOOBS = 1
    STANDARD = 2
    XPERT = 3
    HACKER = 4


_level = Level.NOOBS


def set_level(level: Level):
    """
    Permet de paramétrer cette bibliothèque pour le niveau de formation correspondant.
    """
    global _level
    _level = level


def time_loader():
    """
    Fonction simulant la collecte d'une donnée à partir d'une source de données.
    """
    return "30"


def _noob_get_start_time() -> str:
    """
    Fonction simulant la collecte de la donnée de temps à partir d'une source de données.
    L'heure retournée est toujours '20h42'
    """
    return "20h42"


def _std_get_start_time() -> str:
    """
    Fonction simulant la collecte de la donnée de temps à partir d'une source de données.
    L'heure retournée est comprise entre '19h00' et '21h38'.
    """
    start_hour = random.randint(19, 21)
    start_minutes = random.randint(0, 59 if start_hour < 21 else 38)

    value = f"{start_hour:02}h{start_minutes:02}"

    return value


def _xpert_get_start_time() -> str:
    """
    Fonction simulant la collecte de la donnée de temps à partir d'une source de données.
    L'heure retournée est comprise entre '19h00' et '21h38', le séparateur peut-être 'h' ou ':'.
    """
    value = _std_get_start_time()
    return value if random.randint(0, 9) % 2 else value.replace('h', ':')


def _hacker_get_start_time() -> str:
    """
    Fonction simulant la collecte de la donnée de temps à partir d'une source de données.
    L'heure retournée est comprise entre '19h00' et '21h38', le séparateur peut-être 'h' ou ':'.
    """
    value = _xpert_get_start_time()
    return value if random.randint(0, 9) % 2 else (value[:2] + value[-2:])


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

    if _level.value >= Level.XPERT.value:
        if random.random() > 0.95:
            season.clear()

    for episode in season:
        if random.random() > (0.8 if _level.value < Level.XPERT.value else 0.95):
            if _level.value >= Level.XPERT.value:
                is_viewed = not is_viewed
            else:
                is_viewed = False

        if is_viewed:
            episode['viewed'] = True
        else:
            if random.random() > 0.4:
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


def get_movies():
    """
    Fonction perméttant d'obtenir une liste de médias.
    """
    return [["The Philosopher's Stone", 152, True],
            ["The Chamber of Secrets", 161, True],
            ["The Prisoner of Azkaban", 142, False],
            ["the Goblet of Fire", 157, True],
            ["the Order of the Phoenix", 138, False],
            ["the Half-Blood Prince", 153, True],
            ["the Deathly Hallows – Part 1", 126, False],
            ["the Deathly Hallows – Part 2", 130, False]]


def get_start_time() -> str:
    """
    Fonction simulant la collecte de la donnée de temps à partir d'une source de données.

    Retourne une heure au format '20h42'. Pour un usage avancé, le format peut-être '20:42'
    ou '2042'.
    """
    assets = {
        Level.NOOBS: _noob_get_start_time,
        Level.STANDARD: _std_get_start_time,
        Level.XPERT: _xpert_get_start_time,
        Level.HACKER: _hacker_get_start_time
    }
    return assets[_level]()


set_level(Level.NOOBS)
