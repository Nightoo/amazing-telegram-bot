from bot import send, bot


def love(message):
    send(message, f'I love you, {message.from_user.first_name}')