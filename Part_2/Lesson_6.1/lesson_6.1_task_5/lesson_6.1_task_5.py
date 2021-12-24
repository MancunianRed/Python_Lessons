#  Работа с сетью: Задание 5 - 100 баллов
import requests
from colorama import Fore

url_list = ["https://www.rk-ny.org/whatsnew.php?id=1",
            "https://www.genecards.org/cgi-bin/carddisp.pl?gene=ID1",
            "http://www.meggieschneider.com/php/detail.php?id=1",
            "https://kodamo.org/product.php?id=1"]

sql_injection = "\'"

for url_from_list in url_list:
    res = requests.get(url_from_list + sql_injection)
    if "error in your SQL syntax" in res.text:
        print(f"{res.url} ===> {Fore.GREEN}Vulnerable!{Fore.RESET}")
    else:
        print(f"{res.url} ===> {Fore.RED}Not Vulnerable!{Fore.RESET}")
