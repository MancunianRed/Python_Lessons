#  Пишем фреймворк: Задание 1 - 200 баллов
import whois
import Part_2.Lesson_16.lesson_16_task_1.full_scripts.input_text_check as in_text
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def who_is():
    add = in_text.input_text("Enter domain: ")
    try:
        domain = whois.query(add)
    except Exception as e:
        print(f"{Fore.RED}==>> Error: {e}{Fore.RESET}")
    else:
        res = domain.__dict__
        for i in res:
            print(f"{i}: {res[i]}")
