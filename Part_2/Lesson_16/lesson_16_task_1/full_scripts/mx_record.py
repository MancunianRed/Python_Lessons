#  Пишем фреймворк: Задание 1 - 200 баллов
import dns.resolver
import Part_2.Lesson_16.lesson_16_task_1.full_scripts.input_text_check as in_text
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def mx_record():
    address = in_text.input_text("Enter host: ")
    try:
        my_resolver = dns.resolver.Resolver(configure=False)
        my_resolver.nameservers = ["8.8.8.8", "1.1.1.1"]
        answers = my_resolver.resolve(address, "MX")
    except Exception as e:
        print(f"{Fore.RED} ==> Error: {e}{Fore.RESET}")
    else:
        for rdata in answers:
            print("MX record:", rdata.exchange)


