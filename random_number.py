from random import randint
import time


def time_of_function(function):
    def wrapped(*args):
        start_time = time.time()
        res = function(*args)
        print('The game lasted', int(time.time() - start_time), 'second')
        return res
    return wrapped


def guesses_made():
    while True:
        try:
            return int(input('\nEnter for how many moves you want to withdraw\n------->'))
        except:
            print('It\'s not int')


def get_random_number():
    """
    Returns:
        (int)
    """
    number = randint(1, 101)
    return number


def get_number_from_user():
    """
    Returns:
        (int)
    """
    while True:
        try:
            return int(input('Enter int: '))
        except:
            print('It\'s not int')


def check_numbers(to_guess, user_number):
    """

    Args:
        to_guess (int):
        user_number (int):

    Returns:
        (bool):
    """
    print(f'---> {to_guess}')
    if to_guess == user_number:
        return True
    else:
        return False

@time_of_function
def game():
    number_to_guess = get_random_number()
    guesses= guesses_made()

    while guesses > 0:
        guesses -= 1
        user_number = get_number_from_user()
        if check_numbers(number_to_guess, user_number):
            return 'You WIN!!!!'
    return '\nSorry.\nThe attempts are over, you did not guess'

print(game())