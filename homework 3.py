# task 1.
#  Зформуйте строку, яка містить певну інформацію про символ в відомому слові.
  # Наприклад "The [номер символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
  # Слово та номер отримайте за допомогою input() або скористайтеся константою.
  # Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' "
word = input('Enter the word you are interested in!')
number_symbol =int(input('Enter character number (starting from 0)'))
result = word[number_symbol]
print(result)
print('The {} symbol in word {} is "{}"!'.format(number_symbol, word, result))

# task 2.
# Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою).
 # Напишіть код, який визначить кількість слів, в цих даних.

date_input = input('Enter your dates!')
print('inpu_result', '---->   ', date_input)
print(date_input.count(' ')+1, '  words in this sentence.')
#
#
# task 3.
# Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сфлрмує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1.
# Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.
# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
#
# for lst2 in lst1:
#      if lst2.isdigit():
#           print(lst2)
word = input('Enter the word you are interested in!')
number_symbol =int(input('Enter character number (starting from 0)'))
result = word[number_symbol]
print(result)
print('The {} symbol in word {} is "{}"!'.format(number_symbol, word, result))
