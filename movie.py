from genre import Genre


class Movie:
    def __init__(self, name: str, genre: Genre, description: str, year: int, poster_url: str, rating: float, budget: int) -> None:
        self.name = name
        self.genre = genre
        self.description = description
        self.year = year
        self.poster_url = poster_url
        self.rating = rating
        self.budget = budget
