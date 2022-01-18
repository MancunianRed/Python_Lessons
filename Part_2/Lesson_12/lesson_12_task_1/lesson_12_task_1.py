#  Пишем брутфорсер: Задание 1 - 70 баллов
from tqdm import tqdm
import zipfile
import itertools
import string
from colorama import Fore
import colorama
colorama.init(autoreset=True)


def digits_combinations():
    digits = string.digits
    passw_list = itertools.product(digits, repeat=5)
    passw_search(list(passw_list))


def passw_search(passw_list):
    zip_file = zipfile.ZipFile("secure.zip")
    total_passwds = len(passw_list)
    print(f"Total passwords to test: {total_passwds}")
    for passw in tqdm(passw_list, total=total_passwds, unit=" word/s"):
        try:
            zip_file.extractall(pwd=f"o_main_got{''.join(passw)}".encode())
        except:
            pass
        else:
            print(f"Password found: {Fore.GREEN}o_main_got{''.join(passw)}"
                  f"{Fore.RESET}")
            break


if __name__ == "__main__":
    print("Start bruteforse...")
    digits_combinations()