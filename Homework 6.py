# Task 1.
# Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.
# Якщо перетворити не вдається функція має повернути 0.
# def selection_float(basic_argument):
#     try:
#         verification_of_information = float(basic_argument)
#         print(f'{verification_of_information} its float argument.')
#         return (verification_of_information)
#     except:
#         print('its not float argument.')
#         return 0
#verification_of_information = selection_float()
# print(verification_of_information)
# Task 2.
# Напишіть функцію, що приймає два аргументи. Функція повинна
# -якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
#- якщо обидва аргументи це строки - обʼєднати в одну строку та повернути
# -якщо перший строка, а другий ні - повернути dict де ключ це перший аргумент, а значення - другий
# -у будь-якому іншому випадку повернути кортеж з цих аргументів
def data_processing(first, second):
    multiplication =(int, float)
    sum_str = (str(first, second))
    my_dict = {first=str: second=}
    if multiplication :
        return first * second
        #print(first*second)
    elif sum_str:
        return first + second
res = data_processing('3', '5')
print(res)
