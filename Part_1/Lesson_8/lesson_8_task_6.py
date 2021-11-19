#  Исключения: Задание 6 - 130 баллов

import signal
import sys
import colorama
import vlc
from time import sleep

colorama.initialise.init(autoreset=True)


def handler(x, y):
    print('\n' + colorama.Fore.CYAN + "БА-БАХ!!!")
    sys.exit()


def input_check():
    try:
        password = input('Введите код отмены операции самоуничтожения: ' +
                         colorama.Fore.RED)
    except (ValueError, EOFError):
        return
    else:
        return password


def attempt_check():
    for index in range(3):
        if (passwrd := input_check()) is None or passwrd != 'swordfish':
            print(colorama.Fore.RED + 'Код не принят!')
            if index == 2:
                print(colorama.Fore.CYAN + "БА-БАХ!!!")
                sys.exit()
        else:
            print(colorama.Fore.LIGHTGREEN_EX + 'Операция самоуничтожения '
                                                'отменена!')
            break


p = vlc.MediaPlayer("alarm.mp3")
p.play()
sleep(10)
print(colorama.Fore.RED + 'ВНИМАНИЕ! Запущен механизм самоуничтожения!')
signal.signal(signal.SIGALRM, handler)
signal.alarm(30)
attempt_check()
signal.alarm(0)
