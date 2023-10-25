import telebot
from telebot import types
import random


bot = telebot.TeleBot('token')
dev_id = 1


def send(message, text):
    bot.send_message(message.chat.id, text)
    bot.send_message(dev_id, f'for {message.from_user.first_name}:     ' + text)


def send_to_dev(message):
    bot.send_message(dev_id, f'from {message.from_user.first_name}:     ' + message.text)
