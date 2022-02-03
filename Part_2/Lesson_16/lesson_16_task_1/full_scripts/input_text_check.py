#  Пишем фреймворк: Задание 1 - 200 баллов
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def input_text(text):
    try:
        input_text = input(text)
    except Exception as e:
        print(f"{Fore.RED} ==>> Error: {e}{Fore.RESET}")
    else:
        return input_text
