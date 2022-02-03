#  Пишем фреймворк: Задание 1 - 200 баллов
import pygeoip
import colorama
from colorama import Fore
import Part_2.Lesson_16.lesson_16_task_1.full_scripts.input_text_check as in_text
colorama.init(autoreset=True)


def get_city():
    ip = in_text.input_text("Enter IP: ")
    try:
        gi = pygeoip.GeoIP("GeoIPCity.dat")
        city = gi.record_by_addr(ip)
    except Exception as e:
        print(f"Please enter correct IP {Fore.RED}==>> Error: {e}{Fore.RESET}")
    else:
        for key in city:
            if city[key] is None or city[key] == 0:
                continue
            else:
                print(
                    f"{key+':':<16}{Fore.LIGHTBLUE_EX}{city[key]}{Fore.RESET}")
