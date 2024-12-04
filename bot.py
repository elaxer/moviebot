from telebot import TeleBot
from movie import Movie
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from typing import List


def display_movie(bot: TeleBot, chat_id: int, movies: List[Movie], page: int) -> None:
    movie = movies[page - 1]

    keyboard = _get_keyboard(len(movies), page)

    bot.send_photo(chat_id, photo=movie.poster_url, reply_markup=keyboard, caption=f'''
Название: {movie.name}
Жанр: {movie.genre.value}
Рейтинг: {movie.rating}
Год: {movie.year}
Бюджет: {movie.budget}$

{movie.description}
''')
    
def _get_keyboard(movies_count: int, page: int) -> InlineKeyboardMarkup:
    if movies_count <= 1:
        return None
    
    buttons = []
    if page != 1:
        buttons.append(InlineKeyboardButton('<<', callback_data=f'to {page - 1}'))

    buttons.append(InlineKeyboardButton(f'{page}/{movies_count}', callback_data="None"))
        
    if page != movies_count:
        buttons.append(InlineKeyboardButton('>>', callback_data=f'to {page + 1}'))

    keyboard = InlineKeyboardMarkup()
    keyboard.add(*buttons)

    return keyboard