#  Исключения: Задание 6 - 130 баллов
import colorama

colorama.initialise.init(autoreset=True)


def input_check():
    try:
        password = input('Введите код отмены операции самоуничтожения: ')
    except (ValueError, EOFError):
        return
    else:
        return password


def attempt_check():
    for i in range(3):
        if (passwrd := input_check()) is None or passwrd != 'swordfish':
            print(colorama.Fore.RED + 'Код не принят!')
        else:
            print(colorama.Fore.GREEN + 'Код принят!')
            break


print(colorama.Fore.RED + 'ВНИМАНИЕ! Запущен механизм самоуничтожения!')
attempt_check()
