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
visitor_age = "Вітаю, вкажіть Ваш вік (кількість повних років і це має буті ціле число від 0 до 120 ) та натисніть 'Enter', будь ласка!"
error_input='Наголошую що потрібно ввести кількість повних років і це має буті ціле число від 0 до 120, спробуйте знову'
print(visitor_age)
age2=input('Вводити тут---->')
max_age = 120
age2=int(age2)
def information_input(age1=age2):
    max_age = 120
    age1 = int(age2)
    age1=int
    try:
        if type(age1) != (int):
         return error_input
    except:
        if age1 <= 0 and age1 > max_age:
         return error_input()
    return age1
res_1=information_input()
print(res_1)

def sort_age(age_input=information_input()):
    max_age = 120
    if type (age_input) != (int):
        return information_input('eee')
    if age_input<=0 and age_input> max_age:
        return information_input()
def interesting_age(number=information_input()):
     number = str
     print(type(number))
     if len(number) > 1 and (number.count(number[0]) == len(number)):
         print(f"О, вам {number}! Який цікавий вік!")
         return
res_2 =interesting_age(res_1)

def condition_check(age=information_input()):
    message_if_the_child = (f"Тобі ж {age}! Де твої батьки?")
    message_if_for_adults = (f"Тобі лише {age}, а це фільм для дорослих!")
    message_if_the_documents = (f"Вам {age}?Покажіть пенсійне посвідчення!")
    message_if_the_no_tickets = (f"Незважаючи на те, що вам {age}, білетів всеодно нема!")
    if age<7:
      print(message_if_the_child)
    elif age<16:
     print(message_if_for_adults)
    elif age>65:
     print(message_if_the_documents)
    else:
     print(message_if_the_no_tickets)
res = condition_check(res_1)

# ages1=[1,21,31,41,51,61,71,81,91,101]
# ages2=[2,3,4,22,23,24,32,33,34,42,43,44,52,53,54,62,63,64,72,73,74,82,83,84,92,93,94,102,103,104]
# form_1='рік'
# form_2='роки'
# form_3='років'
# numb =input('puss')
# for numb in ages1 and ages2:
#     if numb in ages1:
#         print(form_1)
#     elif numb in ages2:
#         print(form_2)
#     else:
#         print(form_3)
