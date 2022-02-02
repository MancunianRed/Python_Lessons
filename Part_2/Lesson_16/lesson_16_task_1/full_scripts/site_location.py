#  Пишем фреймворк: Задание 1 - 200 баллов
import pygeoip
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def get_city():
    ip = input("Enter IP: ")
    gi = pygeoip.GeoIP(r"C:\Users\proic\Desktop\Python\Part 2\16 - Пишем "
                       r"фреймворк\GeoIPSity_logo\GeoIPCity.dat")
    try:
        city = gi.record_by_addr(ip)
        for key in city:
            if city[key] is None or city[key] == 0:
                continue
            else:
                print(f"{key+':':<15} {Fore.LIGHTBLUE_EX}{city[key]}{Fore.RESET}")
    except Exception as e:
        print(f"Please enter correct IP {Fore.RED}==>> Error: {e}{Fore.RESET}")
