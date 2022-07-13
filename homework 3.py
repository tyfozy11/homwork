# task 1.
#  Зформуйте строку, яка містить певну інформацію про символ в відомому слові.
  # Наприклад "The [номер символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
  # Слово та номер отримайте за допомогою input() або скористайтеся константою.
  # Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' "

word = input('Enter the word you are interested in!---->')
number_symbol =int(input('Enter character number (starting from 0)---->'))
result = word[number_symbol]
print(result)
print('The {} symbol in word {} is "{}"!'.format(number_symbol, word, result))

# # task 2.
# # Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою).
#  # Напишіть код, який визначить кількість слів, в цих даних.

date_input = input('Enter your dates!')
print('input_result', '---->   ', date_input)
print(len(date_input.split()), '  words in this sentence.')


# task 3.
# Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сфлрмує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1.
# Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.


start_list = ['1', '2', 3, 2.4, 'False', 5.5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum', 55, 'True', 45.24234, 64]
result_list = []
for result in start_list:
     if isinstance(result,(int, float)):
      result_list.append(result)
print('Result_list--->',result_list)