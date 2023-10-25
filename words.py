import pygame
import random
from bot import bot, send, send_to_dev
from telebot import types
GAME = False
LENGTH = 5
TRIES = 6
LETTER_SIZE = 100
WIDTH = LENGTH * LETTER_SIZE
HEIGHT = TRIES * LETTER_SIZE
CURRENT_TRY = 0
WORD = ''


font = 0
screen = 0
msg = 0
letters = []


def set_word(message):
    global WORD, GAME, screen, font, letters
    GAME = True
    send(message, 'Guess the word!')

    words_file = open('russian_words.txt', encoding='utf-8', mode='r')
    words_ = words_file.readlines()
    WORD = random.choice(words_).rstrip().upper()

    pygame.init()
    font = pygame.font.Font(None, 120)
    screen = pygame.Surface((WIDTH, HEIGHT))
    screen.fill((0, 0, 0))
    pygame.image.save(screen, "words.png")
    letters = [[Letter('black', '0', 0, 0, False) for i in range(LENGTH)] for i in range(TRIES)]


class Letter:
    def __init__(self, color, symbol, x, y, drawable):
        self.color = color
        self.symbol = symbol
        self.x = x
        self.y = y
        self.drawable = drawable

    def draw(self):
        if self.drawable:
            symb = font.render(self.symbol, 0, 'black')
            pygame.draw.rect(screen, pygame.Color(self.color), (self.x, self.y, LETTER_SIZE, LETTER_SIZE))
            screen.blit(symb, (self.x + 20, self.y + 14))





def words(message):
    global GAME, WORD, CURRENT_TRY, msg, screen

    user_word = message.text.upper()
    send_to_dev(message)

    words_file = open('russian_words.txt', encoding='utf-8', mode='r')
    words_ = words_file.readlines()
    words_ = [w.rstrip().upper() for w in words_]
    if len(user_word) != LENGTH:
        send(message, 'The word should be ' + str(LENGTH) + ' letters long')
    elif user_word not in words_:
        send(message, "I don't know this word")
    else:
        uw = ''

        counts = []

        for i in range(len(user_word)):
            if user_word[i] == WORD[i]:
                letters[CURRENT_TRY][i] = Letter(
                    'green', user_word[i], i * LETTER_SIZE, CURRENT_TRY * LETTER_SIZE, True)
                counts.append(WORD[i])
                uw += '1'

            elif user_word[i] not in WORD:
                letters[CURRENT_TRY][i] = Letter(
                    'gray', user_word[i], i * LETTER_SIZE, CURRENT_TRY * LETTER_SIZE, True)
                uw += '0'
            else:
                uw += user_word[i]

        if not uw.isdigit():

            for pos in range(LENGTH):
                if uw[pos] not in '01' and counts.count(uw[pos]) != WORD.count(uw[pos]):
                    letters[CURRENT_TRY][pos] = Letter(
                        'yellow', uw[pos], pos * LETTER_SIZE, CURRENT_TRY * LETTER_SIZE, True)
                    counts.append(uw[pos])
                elif uw[pos] not in '01' and counts.count(uw[pos]) == WORD.count(uw[pos]):
                    letters[CURRENT_TRY][pos] = Letter(
                        'gray', uw[pos], pos * LETTER_SIZE, CURRENT_TRY * LETTER_SIZE, True)

        for words_ in letters:
            for letter in words_:
                letter.draw()

        CURRENT_TRY += 1
        pygame.image.save(screen, "words.png")
        image = open("words.png", 'rb')
        if CURRENT_TRY == 1:
            msg = bot.send_photo(message.chat.id, image)
        else:
            img = types.InputMediaPhoto(image)
            bot.edit_message_media(chat_id=message.chat.id, message_id=msg.id, media=img)
            if CURRENT_TRY == 2:
                bot.delete_message(message.chat.id, message.id - 3)
            else:
                bot.delete_message(message.chat.id, message.id - 2)
        image.close()

    if user_word != WORD and CURRENT_TRY == TRIES:
        GAME = False
        send(message, 'Answer: ' + WORD + ' Better luck next time!')
        CURRENT_TRY = 0

    if user_word == WORD:
        GAME = False
        if CURRENT_TRY == 1:
            send(message, 'Impossible')
        if CURRENT_TRY == 2:
            send(message, 'Amazing')
        if CURRENT_TRY == 3:
            send(message, 'Nice')
        if CURRENT_TRY == 4:
            send(message, 'Good')
        if CURRENT_TRY == 5:
            send(message, 'OK')
        if CURRENT_TRY == 6:
            send(message, 'Congrats!')
        CURRENT_TRY = 0
    return GAME
