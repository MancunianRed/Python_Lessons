#  Пишем фреймворк: Задание 1 - 200 баллов
import socket
import Part_2.Lesson_16.lesson_16_task_1.full_scripts.input_text_check as in_text
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def get_ip():
    host = in_text.input_text("Enter the host name: ")
    if "://" in host:
        host = host.split("://")[1]
    host = host.replace("/", "")
    try:
        remote_ip = socket.gethostbyname(host)
    except:
        print(f"Host name {Fore.LIGHTRED_EX}{host}{Fore.RESET}, does not exist")
    else:
        print(f"IP Address of {Fore.LIGHTMAGENTA_EX}{host}{Fore.RESET} is "
              f"{Fore.LIGHTBLUE_EX}{remote_ip}{Fore.RESET}")
