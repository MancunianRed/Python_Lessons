#  Пишем фреймворк: Задание 1 - 200 баллов
from dns import reversename, resolver
import Part_2.Lesson_16.lesson_16_task_1.full_scripts.input_text_check as in_text
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def dns_reverse():
    ip = in_text.input_text("Enter ip: ")
    try:
        rev_name = reversename.from_address(ip)
        reversed_dns = resolver.resolve(str(rev_name), "PTR")[0]
    except Exception as e:
        print(f"{Fore.RED}==> Error: {e}{Fore.RESET}")
    else:
        print(reversed_dns)
