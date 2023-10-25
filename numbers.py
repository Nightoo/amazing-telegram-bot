import random
from bot import send, send_to_dev
NUMBERS_GAME = False
NUMBER = 0


def numbers_game(message):
    global NUMBERS_GAME, NUMBER
    send(message, 'The BinarySearchGame')
    send(message, 'Guess a number between 1 and 10')
    NUMBERS_GAME = True
    NUMBER = random.randint(1, 10)


def guess(message):
    global NUMBERS_GAME, NUMBER
    send_to_dev(message)
    if message.text.isdigit():
        g = int(message.text)
        if g <= 0 or g >= 11:
            send(message, 'Out of borders')
        elif g == NUMBER:
            send(message, 'WIN')
            NUMBERS_GAME = False
        elif g < NUMBER:
            send(message, 'Too small')
        elif g > NUMBER:
            send(message, 'Too big')
    else:
        send(message, 'Not a number')
    return NUMBERS_GAME
