import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def new_email():

    email = f'{generate_random_string(5)}@mail.ru'

    return email


def new_name_password():
    name = f'{generate_random_string(10)}'

    return name
