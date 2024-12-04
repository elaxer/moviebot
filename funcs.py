from movie import Movie
from typing import List


def search_movie(movies: List[Movie], query: str) -> List[Movie]:
    name = query.strip().lower()
    suggested_movies: List[Movie] = []

    for movie in movies:
        if name in movie.name.lower() or name in movie.genre.value.lower():
            suggested_movies.append(movie)

    return suggested_movies

def search_movie_by_rating(movies: List[Movie], rating: int) -> List[Movie]:
    suggested_movies: List[Movie] = []

    for movie in movies:
        if rating == round(movie.rating):
            suggested_movies.append(movie)

    return suggested_movies
