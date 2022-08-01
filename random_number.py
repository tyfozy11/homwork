from random import randint
import time


def time_of_function(function):
    """
    Function for decorating functions.

    :param function:
            (function)
    :return:
          (function)
    """

    def nested_time_function(*args, **kwargs):
        """
        A function for measuring how long (in seconds) the function called in it was executed
        and displays information about the result.

        :param args:
        :param kwargs:
        :return:
                (function)
        """
        start_time = time.time()
        decorated_object = function(*args, **kwargs)
        finish_time = int(time.time() - start_time)
        print(f'\nThe game lasted {finish_time} second')
        return decorated_object

    return nested_time_function


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
    A function that returns the number obtained as a result of the work of the built-in randint
    function in the given range.

    Returns:
        (int)
    """
    random_number = randint(1, 101)
    return random_number


def get_number_from_user():
    """
    The function takes input from the user, then checks with a while loop and a try construct:
    except: for the correctness of the input, if necessary, notifying the user of an error

    Returns:
        (int)
    """
    while True:
        try:
            return int(input('Enter int: '))
        except:
            print('\nIt\'s not int')


def check_numbers(to_guess, user_number):
    """
    Function for comparing numbers received in get_number_from_user and get_random_number functions.
    After that, going through the given conditions returns the result corresponding to the condition that worked out.

    :param to_guess:
                (int)
    :param user_number:
                (int)
    :return:
        (bool)
    """
    tips = to_guess - user_number

    if abs(tips) >= 10:
        print("coldly")
    elif abs(tips) <= 10 and abs(tips) >= 5:
        print('warmer')
    elif abs(tips) <= 4 and abs(tips) >= 1:
        print('hot')

    if to_guess == user_number:
        return True
    else:
        return False


@time_of_function
def game():
    """
    This function, using the data obtained as a result of the work of the get_random_number
     and get_number_from_user functions, using the while loop, checks the equality of these values
     to each other until they are equal or the number of loop passes ends. at the end, messages are
      displayed in accordance with the result of the loop.

    :return:
        (str)
    """
    number_to_guess = get_random_number()
    guesses = guesses_made()

    while guesses > 0:
        guesses -= 1
        user_number = get_number_from_user()
        if check_numbers(number_to_guess, user_number):
            return 'You WIN!!!!'
    return f'\nSorry.\nThe attempts are over, you did not guess.\nThe given number was {number_to_guess}.\nTry again :)'


if __name__ == '__main__':
    print(game())