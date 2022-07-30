from random import randint

entrance = 'Вітаю, виберіть один з варіантів зазначених нижче!'
print(entrance)
choices = "1 - камінь, 2 - ножиці, 3 - папір. "
score_plyer, score_comp = 0, 0


def player_choice():
    while True:
        player = int(input(choices))
        condition = (
            player == 1,
            player == 2,
            player == 3,
        )
        if any(condition):
            return player


def players(wer=player_choice()):
    player = wer
    if player == 1:
        return 'Ви обрали камінь.'
    if player == 2:
        return 'Ви обрали ножиці.'
    if player == 3:
        return 'Ви обрали папір.'


def comp_choice(comp=randint(1, 3)):
    computer = comp
    if computer == 1:
        return "Комп'ютер обрав камінь."
    if computer == 2:
        return "Комп'ютер обрав ножиці."
    if computer == 3:
        return "Комп'ютер обрав папір."


def gema():
    player = players()
    comp = comp_choice()
    in_favor_of_the_player = (player == 3,
                              comp == 1,
                              player == 2,
                              comp == 3,
                              player == 1,
                              comp == 2,
                              )
    in_favor_of_the_computer = (player == 1,
                                comp == 3,
                                player == 1,
                                comp == 3,
                                player == 3,
                                comp == 2,
                                )
    if player == comp:
        return 0
    if all(in_favor_of_the_player):
        return 1
    if all(in_favor_of_the_computer):
        return 2


def determine_the_winner():
    win = gema()
    if win == 0:
        return "Нічия!"
    if win == 1:
        # score_plyer += 1
        return "Ви виграли!"
    if win == 2:
        # score_comp += 1
        return "Переміг комп'ютер!"


re = determine_the_winner()
