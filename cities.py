import random
from bot import send, send_to_dev

CURRENT_CITY = ''
ALREADY_NAMED = []
CITIES_GAME = False


def cities_game(message):
    global CITIES_GAME, CURRENT_CITY, ALREADY_NAMED
    send(message, 'Cities (Russian)')
    send(message, 'Name the city that starts with the last letter of the city I choose')
    send(message, 'Type "Give Up" to give up')
    send(message, 'I go first!')
    cities_file = open('russian_cities.txt', encoding = 'utf-8', mode = 'r')
    cities = cities_file.readlines()
    CURRENT_CITY = random.choice(cities).rstrip().lower()
    send(message, CURRENT_CITY.upper()[0] + CURRENT_CITY[1:].lower())
    ALREADY_NAMED.append(CURRENT_CITY)
    CITIES_GAME = True


def name_city(message):
    send_to_dev(message)
    global CITIES_GAME, CURRENT_CITY, ALREADY_NAMED
    cities_file = open('russian_cities.txt', encoding = 'utf-8', mode = 'r')
    cities = cities_file.readlines()
    cities = [city.rstrip().lower() for city in cities]
    fit = []

    user_city = message.text.lower()

    if user_city == 'give up':
        send(message, 'Better luck next time!')
        CITIES_GAME = False
        ALREADY_NAMED = []
    elif user_city not in cities:
        send(message, "I don't know this city, try another one!")
    elif user_city[0] != CURRENT_CITY[-1]:
        send(message, "Doesn't suit, try another one!")
    elif user_city in ALREADY_NAMED:
        send(message, 'Already named, try another one!')
    else:
        ALREADY_NAMED.append(user_city)
        current_last_letter = user_city[-1]
        for el in cities:
            if el.lower()[0] == current_last_letter:
                fit.append(el)
        for el in fit:
            if el in ALREADY_NAMED:
                fit.remove(el)
        if len(fit) != 0:
            current_city = random.choice(fit)
            send(message, current_city.upper()[0]+ current_city[1:].lower())
            CURRENT_CITY = current_city
            ALREADY_NAMED.append(CURRENT_CITY)

            user_possibilities = []
            for el in cities:
                if el.lower()[0] == CURRENT_CITY[-1]:
                    user_possibilities.append(el)
            for el in user_possibilities:
                if el in ALREADY_NAMED:
                    user_possibilities.remove(el)
            if len(user_possibilities) == 0:
                send(message, 'No cities left!')
        else:
            send(message, "I don't know a city that suits. You won!")
            CITIES_GAME = False
            ALREADY_NAMED = []
    cities_file.close()
    return CITIES_GAME
