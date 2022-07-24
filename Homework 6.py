# Task 1.
# Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.
# Якщо перетворити не вдається функція має повернути 0.
def selection_float(basic_argument):
    try:
        verification_of_information = float(basic_argument)
        print(f'{verification_of_information} its float argument.')
        return (verification_of_information)
    except:
        print('Cannot be converted to float argument.')
        return 0
verification_of_information = selection_float('dfd')
# Task 2.
# Напишіть функцію, що приймає два аргументи. Функція повинна
# -якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
#- якщо обидва аргументи це строки - обʼєднати в одну строку та повернути
# -якщо перший строка, а другий ні - повернути dict де ключ це перший аргумент, а значення - другий
# -у будь-якому іншому випадку повернути кортеж з цих аргументів
def data_processing(first, second):
     if type(first) in (int, float) and type(second) in (int, float):
        print('Sum of multiplication first, second---->', first*second)
        return first*second
     if type(first) == (str) and type(second) == (str):
         print('Concatenation first, second----->', first+second)
         return first+second
     if type(first) == (str) and type(second) != (str):
         new_dict = dict.fromkeys([first],second)
         print('The result of creating a dictionary from first, second -------> ', new_dict)
         return new_dict
     else:
         new_list=[first, second]
         new_tuple = tuple(new_list)
         print('The result of creating a tuple from first, second--------> ', new_tuple)
         return new_tuple

checking_elements = data_processing(3, 'gfihqi')