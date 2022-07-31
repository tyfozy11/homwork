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


guesses_made = 5


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
    if to_guess-user_number>=10 or to_guess+user_number>=10:
         print( "ice")

    if to_guess == user_number:
        return True

    else:
        return False

@time_of_function
def game():
    number_to_guess = get_random_number()
    global guesses_made

    while guesses_made > 0:
        guesses_made -= 1
        user_number = get_number_from_user()
        if check_numbers(number_to_guess, user_number):
            print('You WIN!!!!')


    print('The attempts are over, you did not guess')


game()
