"критерієм перевірки буде проходження всіх ассертів"

##############################################################################
############                                                     #############
############                      TASK 1                         #############
############                                                     #############
##############################################################################
"""
написати декоратор wrap_validate, який не приймає жодних параметрів
його задача - перевірити, що функція, яку він задекорував, обовязково отримала
в своїх аргументах параметр 'password' (згадуємо про * в написанні аргументів функції)
значення 'password' повинне бути стрічкою, довжиною не менше 10 символів,
та містити в собі латинські літери (регістр не принципово), арабські цифри та знак '!"

кожну з перевірок отриманого значення паролю виконуємо в ОКРЕМІЙ функції, функції робимо
універсальними, називаємо їх (з опційними параметрами)
- is_valid_length(length=10)
- has_any_symbols(symbols='qwertyuiopasdfghjklzxcvbnm') (це приклад для латинських букв, повертає тру, якщо хоч
один символ в стрічці, аналогічно зробити для цифр та знаку оклику (у вас буде 3 виклики функції в середині декоратора
з різними параметрами)
- is_string()

якщо  'password'  відсутній - викликаємо помилку
raise AttributeError(f'no parameter "password" in arguments of function{func.__name__}')

якщо  'password'  не задовольняє вимогам валідації, написаним вище, то повертається словник виду
{ 'result': str(func(*args, **kwargs)),
  'is_secure': False,
}

якщо  'password'  задовольняє вимогам валідації, написаним вище, то повертається словник виду
{ 'result': str(func(*args, **kwargs)),
  'is_secure': True,
}

зауважте, що str(func(*args, **kwargs)) МАЄ бути довжиною не більше 100 символів
якщо даний результат буде довшим за 100 символів, то стрічка має бути обрізана до 100 символів, причому останні
три символи мають бути ... (трьома крапками)
тут ви вже й самы здогадалися написати функцію на виконання даної роботи (тут вже без підказок)
"""


def is_valid_length(string_for_length_validation: str, length=10):
    """
    This function is for checking the validity of the length of the string received in the argument. When given a
     string, it compares its length with the number of characters specified in the second argument, if the string is
     less than False. And if the length fits this condition, then True.

    :param string_for_length_validation: (str)
    :param length: (int)
    :return: (bool)
    """
    if len(string_for_length_validation) >= length:
        return True
    else:
        return False


def has_any_symbol(string: str, symbol_for=''):
    """
    A function to check strings for characters from one to the other. It takes two strings and checks for the presence
    of characters from the first string in the second, if there is at least one overlap, it returns True.
    If there are none, returns False.

    :param string:  (str)
    :param symbol_for:
    :return:
        (bool)
    """
    for symbol in string:

        if symbol in symbol_for:
            return True

    return False


def is_string(string: str):
    """
    A function to check the type. It takes one argument if the type of that argument is string - returns True.
    In other cases it will False.

    :param string: (str)
    :return:
        (bool)
    """
    if type(string) == str:
        return True
    return False


def maximum_length_of_string(string: str, maximum_length=100):
    """
    A function to check and change a string depending on its length.
    If the length of the received string is more than specified in the second argument, the function trims the extra
    characters, and replaces the last 3 with '...' and returns the corrected string, if the length is satisfactory,
    it returns the string in the form in which it was received.

    :param string:
        (str)
    :param maximum_length:
        (int)
    :return:
        (str)
    """
    if len(string) > maximum_length:
        return string[:97] + '...'
    return string


def wrap_validate(func):
    def verification_validity(*args, **kwargs):

        if not 'password' in kwargs:
            raise AttributeError(f'no parameter "password" in arguments of function{func.__name__}')


        val1 = is_string(kwargs['password'])
        val2 = has_any_symbol(kwargs['password'.casefold()], 'abcdefghijklmnopqrstuvwxyz')
        val3 = has_any_symbol(kwargs['password'], '0123456789')
        val4 = has_any_symbol(kwargs['password'], '!')
        val5 = is_valid_length(kwargs['password'])

        if val1 and val2 and val3 and val4 and val5:
            is_secure_password = True
        else:
            is_secure_password = False

        result_function = str(func(*args, **kwargs))
        final_result = maximum_length_of_string(result_function)
        return {
            'result': final_result,
            'is_secure': is_secure_password,
        }

    return verification_validity


##############################################################################
############                                                     #############
############                      TASK 2                         #############
############                                                     #############
##############################################################################
"""
написати функцію registration, яка приймає
- позиційний аргумент id, стрічка або число - не важливо,  значення за замовчуванням - відсутнє
- позиційний або іменований аргумент login, тип даних - не важливий, значення за замовчуванням - відсутнє
- позиційний або іменований аргумент notes, тип даних - не важливий, значення за замовчуванням - відсутнє
- password - тип даних - не важливий, значення за замовчуванням - відсутнє

в середині функції вставити код (зназок для отримання даних прописаний нижче)
date = datetime.date.today()

результат робити функції - стрічка
f'User {login} created account on {date} with password "{password}". Additional information: {notes}'

задекоруйте написаним в завданні 1 декоратором
# """


import datetime


@wrap_validate
def registration(login, notes, *, password: str) -> str:
    """
    The function takes two positional and one named arguments, and uses the datetime.date.today() import method.
     Forms the received data into in f-string and returns it.

    :param login: (str)
    :param notes: (str)
    :param password: (str)
    :return: (str)
    """
    date = datetime.date.today()

    return f'User {login} created account on {date} with password "{password}". Additional information: {notes}'




##############################################################################
############                                                     #############
############                      TASK 3                         #############
############                                                     #############
##############################################################################
"""
створіть умову if name == main (тут ціленаправлено написано не вірно, як вірно - ви знаєте)
в цій умові створіть assert на всі створені функції (окрім декоратора), викликайте функції з різними параметрами 
(довжина слів, різні текстовки....)
на кожну функцію, що використовується в декораторі, має бути мінімум 3 ассерта,

функцію registration перевіряйте з огляду на роботу декоратора (ключі, значення). обовязково перевірте кількість ключів, 
тип даних в значеннях, назви ключів, значення отриманого результату в залежності від переданих даних   

ВАЖЛИВО 
функцію registration ассертимо ТІЛЬКИ при передачі їй валідних даних (поля паролю)
"""

if __name__ == '__main__':

    assert registration('Serhii', 'new user', password='ewjfw1!2eetwterryey') == {'result': 'User Serhii created account on 2022-08-13 with password "ewjfw1!2eetwterryey". Additional informa...', 'is_secure': True}
    assert type(registration('we', '12', password='terryey')) == dict
    assert type(registration('we', '12', password='terryey')) == dict, 'TypeError'
    assert has_any_symbol('sfsfsff', 'qqqqq') is False, 'Not valid data!'
    assert has_any_symbol('13131343445', '1234567890') is True
    assert type(has_any_symbol('jfhsgfahf111!!', 'cxadg11745hsdjh')) == bool, 'Not str type'
    assert type(maximum_length_of_string('s'*90)) == str
    assert len(maximum_length_of_string('s'*90)) != 0
    assert type(is_string('dhfjsahfhfwifw')) == bool
    assert is_string(34234) is False
    assert is_string('sfsfwfw212') is True
    assert is_valid_length('addh') is False
    assert type(is_valid_length('131')) == bool


##############################################################################
############                                                     #############
############                      TASK 4                         #############
############                     HAVE FUN                        #############
############                                                     #############
##############################################################################


"________________________________Tried but couldn't )________________________"
"______________________________Thank you for your help!!!_______________________________"