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