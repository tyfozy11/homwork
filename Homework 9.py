from random import randint
import time


# 1. Візьміть гру з заняття і доопрацюйте її наступним чином:
#   -всі функції в окремий файл
#   -додайте підказки привгадуванні (якщо різниця між числом користувача і загаданим більше 10 - вивести "Холодно",
#     якщо 5-10 - "Тепло", якщо 1-4 "Гаряче")
#   -додайте можливість на початку програми вказати кількість спроб вгадування.
#     користувач має вгадати число за вказану кількість спроб
# 2. Напишіть декоратор, який вимірює і виводить на екран час виконання функції в секундах і задекоруйте ним
#    основну функцію гри. Після закінчення гри декоратор має сповістити, скільки тривала гра.
def time_of_function(function):
    def wrapped(*args):
        start_time = time.time()
        res = function(*args)
        print('The game lasted', int(time.time() - start_time), 'second')
        return res

    return wrapped


def guesses_made():
    """
    The function takes input from the user, then checks with a while loop and a try construct:
    except: for the correctness of the input, if necessary, notifying the user of an error

    :return:
        (int)
    """
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
    tips = to_guess - user_number
    while True:
        if abs(tips) >= 10:
            return "ice"

        elif abs(tips) <= 10 and abs(tips) >= 5:
            print('norm')

        elif abs(tips) <= 4 and abs(tips) >= 1:
            print('yes')

        if to_guess == user_number:
            return True

        else:
            return False


@time_of_function
def game():
    number_to_guess = get_random_number()
    guesses_mad = guesses_made()

    while guesses_mad > 0:
        guesses_mad -= 1
        user_number = get_number_from_user()
        if check_numbers(number_to_guess, user_number):
            print('You WIN!!!!')

    print('The attempts are over, you did not guess')


game()
