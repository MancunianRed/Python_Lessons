#  Работа с сетью: Задание 2 - 40 баллов
import requests
import colorama
from colorama import Fore
colorama.init(autoreset=True)

uri_url = ["https://codeby.net/forums/", "https://geekprank.com/hacker/typer/",
           "https://bowandtie.ru/muzhskie-shlyapyi", "https://xakep.ru/",
           "https://sdelaicomp.ru/wi-fi/oshibka"]

for host in uri_url:
    res = requests.get(host, allow_redirects=False)
    if res.status_code == 200:
        print(f"{host} {Fore.GREEN}{res.status_code}{Fore.RESET} Success!")
    elif res.status_code == 301:
        print(f"{host} {Fore.LIGHTBLUE_EX}{res.status_code}{Fore.RESET} Success!")
    elif res.status_code == 404:
        print(f"{host} {Fore.RED}{res.status_code}{Fore.RESET} Not found!")

