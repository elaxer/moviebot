#!/usr/bin/python$

import telebot
from telebot.types import CallbackQuery, ReplyKeyboardMarkup, KeyboardButton
from genre import Genre
from funcs import search_movie, search_movie_by_rating
from movies import movies
from bot import display_movie

ACCESS_TOKEN = ''

bot = telebot.TeleBot(ACCESS_TOKEN)

chats_movies = {}

@bot.message_handler(commands=['start'])
def send_welcome(message: telebot.types.Message):
    bot.reply_to(message, 'Добро пожаловать в бот поиска кинофильмов, созданный в рамках практической работы университета КиНЭУ!')

@bot.callback_query_handler(func=lambda query: True)
def callback(query: CallbackQuery):
    if 'to' not in query.data: 
        return

    if query.message.chat.id not in chats_movies.keys():
        return
    
    page = int(query.data.split(' ')[1])
    suggested_movies = chats_movies[query.message.chat.id]
    display_movie(bot, query.message.chat.id, suggested_movies, page)

    bot.delete_message(query.message.chat.id, query.message.id)

@bot.message_handler(commands=['movie_search'])
def movie_search(message: telebot.types.Message):
    movie_name = message.text.split(' ', 1)[1]
    suggested_movies = search_movie(movies, movie_name)

    chats_movies[message.chat.id] = suggested_movies

    display_movie(bot, message.chat.id, suggested_movies, 1)

@bot.message_handler(commands=['movie_by_rating'])
def movie_by_rating(message: telebot.types.Message):
    movie_rating = int(message.text.split(' ', 1)[1])
    suggested_movies = search_movie_by_rating(movies, movie_rating)

    chats_movies[message.chat.id] = suggested_movies

    display_movie(bot, message.chat.id, suggested_movies, 1)

@bot.message_handler(commands=['genres'])
def genres(message: telebot.types.Message):
    keyboard = ReplyKeyboardMarkup()
    for genre in Genre:
        keyboard.add(KeyboardButton('/movie_search ' + genre.value))

    bot.send_message(message.chat.id, 'Выберите интересующий вас жанр', reply_markup=keyboard)


bot.infinity_polling()