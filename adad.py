import random




win, g = ['RS', 'SP', 'PR'], 'Y'
cg, ca = 0, 0

print('Начинаем игру! Для выхода из игры введете - N \n (варианты ходов: R, S или P)')
while g != 'N':
    g = input('Ваш ход: ')
    a = 'RSP'[random.randint(0, 2)]

    if (g + a) in win:
        cg += 1
        print(f'Выиграл игрок, у компьютера {a}. Счет {cg}:{ca}  (игрок:комп)')
    if (a + g) in win:
        ca += 1
        print(f'Выиграл компьютер - {a}. Счет {cg}:{ca}  (игрок:комп)')
    if a == g:
        print(f'Ничья - {g} и {a}')

print(f'\nОбщий счет - {cg}:{ca}  (игрок:комп)\n\n Увидимся! ')


def snk():
    count = counter
    iterat = game()
    while True :
        if count<=5:
            return iterat
        else:
            return f'\nГра закінчкна\nрахунок:{score_game}'

        ending = input('\nПродовжити введіть велику літеру-Y\nЗавершити гру введіть велику літеру-N ')

        # файл guess_number.py
        # импортируем модуль для работы со случайными числами
        import random

        # число попыток угадать
        guesses_made = 0

        # получаем имя пользователя из консольного ввода
        name = input('Привет! Как тебя зовут?\n')

        # получаем случайное число в диапазоне от 1 до 30
        number = random.randint(1, 30)
        print('Отлично, {0}, я загадал число между 1 и 30. Сможешь угадать?'.format(name))

        # пока пользователь не превысил число разрешенных попыток - 6
        while guesses_made < 6:

            # получаем число от пользователя
            guess = int(input('Введи число: '))

            # увеличиваем счетчик числа попыток
            guesses_made += 1

            if guess < number:
                print('Твое число меньше того, что я загадал.')

            if guess > number:
                print('Твое число больше загаданного мной.')

            if guess == number:
                break

        if guess == number:
            print('Ух ты, {0}! Ты угадал мое число, использовав {1} попыток!'.format(name, guesses_made))
        else:
            print('А вот и не угадал! Я загадал число {0}'.format(number))