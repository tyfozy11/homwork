import random

POSSIBLE_COMBINATIONS = {
    'папір': 'камінь',
    'ножиці': 'папір',
    'камінь': 'ножиці',
}

score_game = {
    'нічия': 0,
    'комп\'ютер': 0,
    'гравець': 0,
}


def computer_choice():
    """
    Function for random selection of one of the options in the dictionary POSSIBLE_COMBINATIONS.

    :return:
        (str)
    """
    choice = random.choice(list(POSSIBLE_COMBINATIONS))
    return choice


def player_choice():
    """

    The function takes input from the user, then checks with a while loop and a try construct:
    except: for the correctness of the input, if necessary, notifying the user of an error

    :return:
        (str)
    """
    variant = list(POSSIBLE_COMBINATIONS)
    while True:
        try:
            choice_player = int(input(

                f'Вітаю, виберіть один з варіантів зазначених нижче!\n\n'
                f'для вибору {variant[0]}- введіть 0\n'
                f'для вибору {variant[1]}- введіть 1\n'
                f'для вибору {variant[2]}- введіть 2\n\n'
                f'Введіть ваш варіат тут---->  '))
        except ValueError:
            print('Ведено не вірне значення, спробуйте звону.')
        else:
            if choice_player <= 2:
                return variant[choice_player]
            else:
                print('Не вірно, наголошую, що потрібно ввести саме 0, 1 або 2!\nCпробуйте ще.')


def game():
    """

    The function compares the results obtained in the comp_choice and player_choice functions.
    Outputs a message corresponding to the result and adds the data to the score_game dictionary.

    :return:
        (str)
    """

    computer = computer_choice()
    player = player_choice()

    if computer == player:
        score_game['нічия'] += 1
        return "нічия"

    if POSSIBLE_COMBINATIONS[computer] == player:
        score_game['комп\'ютер'] += 1
        print(player)
        return f'\nПереміг комп\'ютер!\n(комп\'ютер обрав {computer}, ваш вибір {player})'
    score_game['гравець'] += 1
    return f'\nВи перемогли!!\n(комп\'ютер обрав {computer}, ваш вибір {player})'


if __name__ == '__main__':
    print(game(), '\n\nРахунок:  \n', score_game)
