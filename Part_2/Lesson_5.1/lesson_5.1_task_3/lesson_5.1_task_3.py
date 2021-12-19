#  Многопоточность: Задание 3 - 30 баллов
import time
from multiprocessing import Pool
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def count(*num):
    for i in num:
        if i == "Старт!" or i == "Время вышло!":
            print(f"{Fore.RED}\r{i:-^12}", end="")
            time.sleep(1)
        else:
            a = f"{i:02d}"
            print(f"{Fore.LIGHTMAGENTA_EX}\r{a:-^12}", end="")
            time.sleep(1)


if __name__ == "__main__":
    count_list = ["Старт!", 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, "Время вышло!"]
    pool = Pool(1)
    pool.apply(count, args=count_list)

