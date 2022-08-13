
def is_valid_length(string_for_length_validation: str, length=10):
    if len(string_for_length_validation) >= length:
        return True
    else:
        return False


def has_any_symbol(string: str, symbol_for=''):
    for symbol in string:

        if symbol in symbol_for:
            return True

    return False


def is_string(string: str):
    if type(string) == str:
        return True
    return False


def maximum_length_of_string(string: str, length=100):
    if len(string) > length:
        return string[:97] + '...'
    return string


def wrap_validate(func):
    def verification_validity(*args, **kwargs):

        if not 'password' in kwargs:
            raise AttributeError(f'no parameter "password" in arguments of function{func.__name__}')

        result_function = func(*args, **kwargs)
        val1 = is_string(kwargs['password'])
        val2 = has_any_symbol('ewjfw12!eetwterryey', 'abcdefghijklmnopqrstuvwxyz')
        val3 = has_any_symbol('ewjfw12!eetwterryey', '0123456789')
        val4 = has_any_symbol('ewjfw12!eetwterryey', '!')

        if (val1 and val2 and val3 and val4) == True:
            return {'result': str(func(*args, **kwargs)),
                    'is_secure': True,
                    }
        return {'result': str(func(*args, **kwargs)),
                'is_secure': False,
                }

    return verification_validity


import datetime


@wrap_validate
def registration(id, login, notes, password: str) -> str:
    date = datetime.date.today()

    return f'User {login} created account on {date} with password "{password}". Additional information: {notes}'


if __name__ == '__main__':
    print(registration('1231', 'qwheq', '342424', password='ewjfw12!eetwterryey'))
