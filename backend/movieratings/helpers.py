import requests
import json


def memoized_query_movie():
    # movies = {}
    movies = {
        4:  {
            "producer": "Gary Kurtz, Rick McCallum",
            "title": "A New Hope",
            "created": "2014-12-10T14:23:31.880Z",
            "episode_id": 4,
            "director": "George Lucas",
            "release_date": "1977-05-25",

        },
        5: {
            "producer": "Gary Kurtz, Rick McCallum",
            "title": "The Empire Strikes Back",
            "created": "2014-12-12T11:26:24.656Z",
            "episode_id": 5,
            "director": "Irvin Kershner",
            "release_date": "1980-05-17",
        },
        6: {
            "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
            "title": "Return of the Jedi",
            "created": "2014-12-18T10:39:33.255Z",
            "episode_id": 6,
            "director": "Richard Marquand",
            "release_date": "1983-05-25",
        },
        1: {
            "producer": "Rick McCallum",
            "title": "The Phantom Menace",
            "created": "2014-12-19T16:52:55.740Z",
            "episode_id": 1,
            "director": "George Lucas",
            "release_date": "1999-05-19",
        },
        2: {
            "producer": "Rick McCallum",
            "title": "Attack of the Clones",
            "created": "2014-12-20T10:57:57.886Z",
            "episode_id": 2,
            "director": "George Lucas",
            "release_date": "2002-05-16",
        },
        3: {
            "producer": "Rick McCallum",
            "title": "Revenge of the Sith",
            "created": "2014-12-20T18:49:38.403Z",
            "episode_id": 3,
            "director": "George Lucas",
            "release_date": "2005-05-19",
        },
        7: {
            "producer": "Rick McCallum",
            "title": "The Force Awakens",
            "created": "2014-12-20T18:49:38.403Z",
            "episode_id": 7,
            "director": "George Lucas",
            "release_date": "2005-05-19",
        }
    }

    def helper(id):
        if id in movies:
            return movies[id]

        res = requests.get("https://swapi.co/api/films")

        if (res.status_code != 200):
            raise Exception("could not fetch movies")

        obj = json.loads(res.content)

        for movie in obj['results']:
            movies[movie['episode_id']] = movie

        return movies[id]

    return helper


query_movie = memoized_query_movie()