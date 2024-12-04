from enum import Enum, unique


@unique
class Genre(Enum):
    THRILLER = 'Триллер'
    DRAMA = 'Драма'
    COMEDY = 'Комедия'
