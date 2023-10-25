import telebot
from telebot import types
import pygame
import random

from bot import bot, send, send_to_dev
from love import love
from numbers import numbers_game, guess
from cities import cities_game, name_city
from words import set_word, words

MODE = 'SELECT'


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    love_button = types.KeyboardButton('❤️ Love')
    numbers_game_button = types.KeyboardButton('🔢 Numbers')
    cities_game_button = types.KeyboardButton('🏙️ Cities')
    words_game_button = types.KeyboardButton('🔠 Words')
    keyboard.add(love_button, numbers_game_button, cities_game_button, words_game_button)

    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}', reply_markup=keyboard )


#@bot.message_handler(func=lambda x: MODE == 'LOVE')


@bot.message_handler(func=lambda x: MODE == 'NUMBERS')
def play_numbers(message):
    global MODE
    if not guess(message):
        MODE = 'SELECT'


@bot.message_handler(func=lambda x: MODE == 'CITIES')
def play_cities(message):
    global MODE
    if not name_city(message):
        MODE = 'SELECT'


@bot.message_handler(func=lambda x: MODE == 'WORDS')
def play_words(message):
    global MODE
    if not words(message):
        MODE = 'SELECT'


@bot.message_handler(content_types=['text'])
def message_processing(message):
    global MODE
    if message.text == '❤️ Love':
        love(message)
        MODE = 'LOVE'
    elif message.text == '🔢 Numbers':
        MODE = 'NUMBERS'
        numbers_game(message)
    elif message.text == '🏙️ Cities':
        MODE = 'CITIES'
        cities_game(message)
    elif message.text == '🔠 Words':
        MODE = 'WORDS'
        set_word(message)
    else:
        send(message, "I'm not advanced enough to understand this message")
    print(MODE)

bot.polling(none_stop=True)
