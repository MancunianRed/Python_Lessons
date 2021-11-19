#  Форматирование: Задание 5 - 100 баллов
import random
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def dice():
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    return dice_1 + dice_2


def winner():
    while (dima := dice()) == (vova := dice()):
        print(f'Игрок Дима набрал {dima:02d} очк.\nИгрок Вова набрал '
              f'{vova:02d} очк.\nОчки у обоих игроков '
              f'совпали, перебрасываем кости\n')
    if dima > vova:
        print(f'{Fore.GREEN}Игрок Дима набрал {dima:02d} очк. You winner\n'
              f'{Fore.RESET}Игрок Вова набрал {vova:02d} очк.')
    else:
        print(f'{Fore.GREEN}Игрок Вова набрал {vova:02d} очк. You winner\n'
              f'{Fore.RESET}Игрок Дима набрал {dima:02d} очк.')


if __name__ == '__main__':
    winner()