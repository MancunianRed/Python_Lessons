#  Форматирование: Задание 5 - 100 баллов
import random
import colorama
colorama.init(autoreset=True)


def dice():
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    return dice_1 + dice_2


def winner():
    dima = dice()
    vova = dice()
    if dima > vova:
        print(colorama.Fore.GREEN + f'Игрок Дима набрал {dima:02d} очк. You '
                                    f'winner')
        print(f'Игрок Вова набрал {vova:02d} очк.')
    elif vova > dima:
        print(colorama.Fore.GREEN + f'Игрок Вова набрал {vova:02d} очк. You '
                                    f'winner')
        print(f'Игрок Дима набрал {dima:02d} очк.')
    else:
        print(f'Игрок Дима набрал {dima:02d} очк.\nИгрок Вова набрал '
              f'{vova:02d} очк.\nОчки у обоих игроков '
              f'совпали, перебрасываем кости')


if __name__ == '__main__':
    winner()