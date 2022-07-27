# Знову апишіть программу "Касир в кінотеатрі", яка буде виконувати наступне:
# Попросіть користувача ввести свсвій вік.
# - якщо користувачу менше 7 - вивести "Тобі ж <>! Де твої батьки?"
# - якщо користувачу менше 16 - вивести "Тобі лише <>, а це е фільм для дорослих!"
# - якщо користувачу більше 65 - вивести "Вам <>? Покажіть пенсійне посвідчення!"
# - якщо вік користувача складається з однакових цифр (11, 22, 44 і тд років, всі можливі варіанти!) - вивести "О, вам <>! Який цікавий вік!"
# - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <>, білетів всеодно нема!
# Замість <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік
# Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача.
#
# Наприклад :
# "Тобі ж 5 років! Де твої батьки?"
# "Вам 81 рік? Покажіть пенсійне посвідчення!"
# "О, вам 33 роки! Який цікавий вік!"
#
# Зробіть все за допомогою функцій! Для кожної функції пропишіть докстрінг.
# Не забувайте що кожна функція має виконувати тільки одне завдання і про правила написання коду.


max_age = 120
visitor_age = f"Вітаю, вкажіть Ваш вік (кількість повних років і це має буті ціле число від 0 до {max_age}) та натисніть 'Enter', будь ласка!"
error_input = f'Наголошую що потрібно ввести кількість повних років і це має буті ціле число від 0 до {max_age} спробуйте знову'
message_if_the_child = "Тобі ж {age} {years_ending}! Де твої батьки?"
message_if_for_adults = "Тобі лише {age} {years_ending}, а це фільм для дорослих!"
message_if_the_documents = "Вам {age} {years_ending}? Покажіть пенсійне посвідчення!"
message_if_the_no_tickets = "Незважаючи на те, що вам {age} {years_ending}, білетів все одно нема!"
but_age = "О вам {age} {years_ending}! Який цікавий вік!"


def get_visitor_age():
    """
Function that accepts data from the user and uses a loop to check it against the given conditions.
if the information is of the right type and correct form, then it is saved for further use,
if not, the function indicates a failure.

:return:str
    """
    while True:
        test_age = input(visitor_age).lstrip('0')
        if test_age.isdigit() and int(test_age) <= max_age:
            return test_age
        print(error_input)


def is_beautiful_age(age: str):
    """
Function for definitions using the len() function of duplicated numbers (11, 22...).
if there are, it returns True. If not then False.

:param age:str
:return:bool
    """
    if len(age) > 1 and (age.count(age[0]) == len(age)):
        return True
    else:
        return False


def word_case(age: str):
    """
Function to change type
from str to int and analyzing the resulting number,
determines the desired form of the word,
checking the digit on which the number received from the user ends.

:param age: str
:return: str
    """
    age_int = int(age)
    if age_int >= 5 and age_int <= 20:
        return 'років'
    if age[-1] == "1":
        return 'рік'
    if age[-1] in '234':
        return 'роки'
    return 'років'


def main():
    """
Function for processing data received from functions: get_visitor_age is_beautiful_age
word_case. After analyzing according to the given parameters,
a message is displayed depending on which of the conditions was met.

:return: str
    """
    user_age = get_visitor_age()
    beautiful_age = is_beautiful_age(user_age)
    years_ending = word_case(user_age)
    age = int(user_age)
    if beautiful_age:
        return but_age.format(age=age, years_ending=years_ending)


    elif age < 7:
        return message_if_the_child.format(age=age, years_ending=years_ending)
    elif age < 16:
        return message_if_for_adults.format(age=age, years_ending=years_ending)
    elif age > 65:
        return message_if_the_documents.format(age=age, years_ending=years_ending)
    else:
        return message_if_the_no_tickets.format(age=age, years_ending=years_ending)


print(main())
