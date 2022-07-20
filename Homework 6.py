# Task 1.
# Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.
# Якщо перетворити не вдається функція має повернути 0.
# def selection_float(basic_argument):
#     try:
#         res = float(basic_argument)
#         print(f'{res} its float argument.')
#         return (res)
#     except:
#         print('its not float argument.')
#         return 0
# res = selection_float()
# print(res)
# Task 2.
# Напишіть функцію, що приймає два аргументи. Функція повинна
# -якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
#- якщо обидва аргументи це строки - обʼєднати в одну строку та повернути
# -якщо перший строка, а другий ні - повернути dict де ключ це перший аргумент, а значення - другий
# -у будь-якому іншому випадку повернути кортеж з цих аргументів
def data_processing(first, second):
    multiplication =(int, float)
    sum_str = (str)
    if multiplication :
        return first * second
        #print(first*second)
    elif sum_str:
        return first + second
res = data_processing('sdfsf', 'afafqfq')
print(res)
