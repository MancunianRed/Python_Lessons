#  Пишем фреймворк: Задание 1 - 200 баллов
import requests
import socket
from dns import reversename, resolver
import Part_2.Lesson_16.lesson_16_task_1.full_scripts.input_text_check as in_text
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def reverse_ip():
    api = "http://api.hackertarget.com/reverseiplookup/"
    var = in_text.input_text("Enter IP or Domain: ")
    try:
        ip = socket.gethostbyname(var)
        pwn = requests.request("GET", api, params={"q": ip})
        reversed_dns = str(resolver.resolve(str(reversename.from_address(ip)),
                                            "PTR")[0]).rstrip('.')
    except Exception as e:
        print(f"{Fore.RED} ==>> Error: {e}{Fore.RESET}")
    else:
        print(f"Found domain hosted on the same web server "
              f"as {reversed_dns} ({ip})")
        print(pwn.text)

