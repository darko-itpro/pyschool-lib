"""
Module de gestion de connexion à une base de données.

Note sur la présence de la fonction print :
Un objet ne doit pas avoir une instruction print car on ignore son contexte
d'exécution. Néanmoins, un objet comme la DAO doit conserver des "traces" des
évènements. Ceci passe communément par des loggers. Ce code étant destiné à des
formations ne traitant en général pas les loggers, un print est utilisé à la
place.
"""

import sqlite3 as sqlite
from collections import namedtuple
from pathlib import Path
import re

SQL_CREATE_EPISODES_TABLE = "CREATE TABLE IF NOT EXISTS episodes (" \
                            "e_number INT NOT NULL, " \
                            "season INT NOT NULL, " \
                            "title TEXT NOT NULL, " \
                            "duration INT, " \
                            "year INT, " \
                            "PRIMARY KEY (e_number , season))" \
                            ";"
SQL_CREATE_SHOW_TABLE = "CREATE TABLE IF NOT EXISTS show (" \
                        "key TEXT NOT NULL, " \
                        "value TEXT NOT NULL, " \
                        "PRIMARY KEY (key))" \
                        ";"

SQL_ADD_SHOW_DATA = "INSERT INTO show values (?, ?);"
SQL_GET_SHOW_DATA = "SELECT value FROM show WHERE key = ?;"

SQL_ADD_EPISODE = "INSERT INTO episodes values(?, ?, ?, ?, ?);"
SQL_GET_EPISODE = ("SELECT title, season, e_number, duration, year "
                   "FROM episodes where season = ? and e_number = ?;")
SQL_GET_ALL_EPISODES = ("SELECT title, season, e_number, duration, year "
                        "FROM episodes ORDER BY season, e_number;")
SQL_GET_EPISODES_FOR_SEASON = ("SELECT title, season, e_number, duration, year "
                               "FROM episodes where season = ? "
                               "ORDER BY e_number;")
SQL_GET_EPISODES_BETWEEN = ("SELECT  title, season, e_number, duration, year "
                            "FROM episodes where season >= ? and episode >= ? "
                            "ORDER BY season, e_number;")
SQL_COUNT_EPISODES = "SELECT COUNT(*) FROM episodes;"

KEY_SHOW_NAME = "name"

# Ce module utilise un namedtuple comme structure de données pour remplacer la classe Episode
# tout en gardant la syntaxe pour accéder aux attributs.
Episode = namedtuple("Episode", ('title', 'season_number', 'number', 'duration', 'year'),
                     defaults=[None, None])


class TvShow:
    """
    TV Show DAO (Data Access Object) pour une série.
    """

    def __init__(self, name: str):
        self._name = name.title()

        # Cette première ligne utilise les regex pour remplacer (substitute) certains caractères.
        self._db_name = Path(Path.home(), re.sub("[ .()]", "_", name)).with_suffix('.db')
        self._connect = sqlite.connect(self._db_name)

        try:
            cur = self._connect.cursor()
            cur.execute(SQL_CREATE_EPISODES_TABLE)
            cur.execute(SQL_CREATE_SHOW_TABLE)
            cur.execute(SQL_ADD_SHOW_DATA, (KEY_SHOW_NAME, self._name))

        except sqlite.Error:
            # L'erreur qui se produirait ici résulterait de l'existance des tables.
            # Nous pouvons alors considérer que les tables existent et que le nom est attribué
            cur.execute(SQL_GET_SHOW_DATA, (KEY_SHOW_NAME,))
            self._name = cur.fetchone()[0]

    def __del__(self):
        try:
            self._connect.close()

        except sqlite.Error as e:
            print("Could not close database")  # Voir docstring à propos du print
            print(e)  # Voir docstring à propos du print

    def __str__(self):
        return f'Media DB Connector ({self._db_name})'

    @property
    def name(self) -> str:
        return self._name

    def add_episode(self, title: str, ep_number: int, season_number: int,
                    duration: int|None = None, year: int|None = None) -> None:
        """
        Ajoute un épisode à la collection.

        :param title: titre de l'épisode
        :param ep_number: numério de l'épisode
        :param season_number: numéro de saison de l'épisode
        :param duration: durée en minutes d'un épisode, optionnel - non utilisé
        :param year: année de l'épisode, optionnel - non utilisé
        :raises ValueError: si l'épisode existe déjà
        """
        try:
            with self._connect:
                cur = self._connect.cursor()
                cur.execute(SQL_ADD_EPISODE, (ep_number, season_number, title, duration, year))
        except sqlite.IntegrityError as ext:
            raise ValueError(f"Episode {title} s{season_number}e{ep_number} exists") from ext

    def get_episodes(self, season:int|str|None = None):
        """
        Permet d'accéder aux épisodes en fonction de la saison.

        :param season: saison des épisodes afin de filtrer ceux-ci. Optionnel.
        :return: la liste des épisodes pour la saison si spécifiée, tous les épisodes si
        pas de paramètre. Liste vide si la saison n'existe pas.
        """
        cur = self._connect.cursor()
        if season:
            cur.execute(SQL_GET_EPISODES_FOR_SEASON, (int(season),))
        else:
            cur.execute(SQL_GET_ALL_EPISODES)

        return [Episode(*episode_data)
                for episode_data in cur.fetchall()]

    @property
    def episodes(self) -> list[Episode]:
        return self.get_episodes()

    @property
    def duration(self) -> int:
        cur = self._connect.cursor()
        cur.execute(SQL_GET_ALL_EPISODES)
        return sum((episode_data[3]
                    for episode_data in cur.fetchall()))

    def __len__(self):
        cur = self._connect.cursor()
        cur.execute(SQL_COUNT_EPISODES)
        return cur.fetchone()[0]

    def __contains__(self, item: Episode):
        cur = self._connect.cursor()
        cur.execute(SQL_GET_EPISODE, (item.season_number, item.number))
        return bool(cur.fetchone)

    def __getitem__(self, item):
        cur = self._connect.cursor()

        if isinstance(item, slice):
            start_season, start_episode = item.start if item.start else (0, 0)
            end_season, end_episode = item.stop if item.stop else (None, None)

            cur.execute(SQL_GET_ALL_EPISODES)
            episodes = [Episode(*episode_data) for episode_data in cur.fetchall()]
            episodes = [episode for episode in episodes
                        if (episode.season_number, episode.number) > (start_season, start_episode)]

            #  TODO: Deal with upper limit

            return episodes

        else:
            season_number, number = item
            cur.execute(SQL_GET_EPISODE, (season_number, number))
            if episode_data := cur.fetchone():
                return Episode(*episode_data)

            raise KeyError(f"No episode for season {season_number} number {number}")

    def __iter__(self):
        return TvShowIterator(self._db_name)


class TvShowIterator:
    """
    Itérateur sur les épisodes d'une seule série
    """

    def __init__(self, datasource):
        """
        L'implémentation de cet itérateur charge tous les épisodes dans un attribut local. Une
        alternative serait de paginer à l'aide d'un thread par exemple.
        """
        self._datasource = Path(datasource)
        if not self._datasource.exists():
            raise ValueError(f'File {datasource} does not exist')

        self._connect = sqlite.connect(self._datasource)
        cur = self._connect.cursor()
        cur.execute(SQL_GET_ALL_EPISODES)

        self._episodes = [Episode(*episode_data)
                          for episode_data in cur.fetchall()]

        self._connect.close()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self._episodes.pop(0)
        except IndexError as exc:
            raise StopIteration() from exc
