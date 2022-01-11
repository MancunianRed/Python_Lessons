#  Пишем конвертеры для полезных нагрузок: Задание 3 - 100 баллов
import requests
import sys
import os
from colorama import Fore
import colorama
import argparse
from multiprocessing import Pool
from multiprocessing import Lock
import re
from fake_useragent import UserAgent
import base64
import urllib.parse
colorama.init(autoreset=True)

DIRS = []
DOMAIN = []
COUNTER = 0
QUANTITY = ""


def greetings():
    """Функция отображает приветствие пользователя"""
    print(f'''{Fore.GREEN}
╔═══╗╔══╗╔═══╗     ╔═══╗╔╗─╔╗╔════╗╔════╗╔═══╗╔═══╗
╚╗╔╗║╚╣║╝║╔═╗║     ║╔══╝║║─║║╚══╗═║╚══╗═║║╔══╝║╔═╗║
─║║║║─║║─║╚═╝║     ║╚══╗║║─║║──╔╝╔╝──╔╝╔╝║╚══╗║╚═╝║
─║║║║─║║─║╔╗╔╝     ║╔══╝║║─║║─╔╝╔╝──╔╝╔╝─║╔══╝║╔╗╔╝
╔╝╚╝║╔╣║╗║║║╚╗     ║║───║╚═╝║╔╝═╚═╗╔╝═╚═╗║╚══╗║║║╚╗
╚═══╝╚══╝╚╝╚═╝     ╚╝───╚═══╝╚════╝╚════╝╚═══╝╚╝╚═╝
          {Fore.RESET}''')


def check_wordlist_file(args):
    """Функция проверяет наличие файла со словарём"""
    if not os.path.isfile(args.w):
        print(f"{args.w}\nФайл со словарём не найден.")
        sys.exit(0)
    fill_dirs_from_file(args)


def check_site_annotaion(args):
    """Функция проверяет есть ли коннект с хостом"""
    url_list = list(args.u.partition("FUZZ"))
    ua = UserAgent()
    try:
        if args.head is None:
            response = requests.get(url_list[0], headers={"User-Agent": ua.random}, timeout=1)
            response.raise_for_status()
        else:
            my_list = [item.strip() for item in args.head.split(",")]
            response = requests.get(url_list[0], headers={x.split(":")[0].strip(): x.split(":")[1].strip() for x in my_list}, timeout=1)
            response.raise_for_status()
        if response.status_code == 200:
            print('OK!')
    except (requests.exceptions.HTTPError, requests.exceptions.Timeout) as e:
        print('ERROR: %s' % e)
    else:
        return url_list


def check_args_qnt(args, parser):
    """Функция проверяет количество аргументов"""
    if args.u is None or args.w is None:
        parser.print_help()
        sys.exit(0)
    print(f"проверка количества аргументов прошла успешно аргумент "
          f"-u {args.u} и "
          f"аргумент -w {args.w}")


def check_app_keys(args, parser):
    """Функция проверяет правильность аргументов"""
    global DOMAIN
    # Количество аргументов
    check_args_qnt(args, parser)
    # Доступность файла словаря
    check_wordlist_file(args)
    # Доступность хоста
    DOMAIN = check_site_annotaion(args)
    print(f"\nРаботаем с сайтом {args.u}. Путь к словарю {args.w}\n")


def fill_dirs_from_file(args):
    global QUANTITY
    """Функция читает файл с адресами папок в список"""
    with open(args.w, "r") as reader:
        for line in reader.readlines():
            if args.b64 is True:
                code_line = base64.b64encode(line.strip().encode("utf-8"))
                DIRS.append(str(code_line, "utf-8"))
            elif args.uenc is True:
                code_line = urllib.parse.quote(line.strip())
                DIRS.append(code_line)
            else:
                DIRS.append(line.strip())
    QUANTITY = str(len(DIRS))
    print("\nЗагружено строк из словаря: " + QUANTITY + "\n")


def save_to_file(url_result):
    file_name = "result.txt"
    with open(file_name, "a") as writer:
        writer.write(url_result + "\n")


def get_site_dirs(DIRS):
    """Функция проверки директорий"""
    global COUNTER
    global DOMAIN
    global QUANTITY
    try:
        DOMAIN[1] = DIRS.strip()
        if re.match(r"#", DOMAIN[1]) or re.match(r"\s", DOMAIN[1]) or (DOMAIN[1] == ""):
            pass
        else:
            if DOMAIN[2] != "/":
                target_url = "".join(DOMAIN).strip() + "/"
            else:
                target_url = "".join(DOMAIN).strip()
            host_answer = requests.get(target_url)
            COUNTER += 1
            answer_code = {404: f"{COUNTER:08d} of {QUANTITY}\t{host_answer.status_code}\t{target_url}{' '*50}",
                           403: f"{COUNTER:08d} of {QUANTITY}\t{Fore.RED}{host_answer.status_code}{Fore.RESET}\t"
                                f"{target_url}{' '*100}"}
            if host_answer.status_code == 404:
                lock.acquire()
                print(answer_code.get(host_answer.status_code), end="\r")
                lock.release()
            elif host_answer.status_code == 403:
                lock.acquire()
                print(answer_code.get(host_answer.status_code))
                save_to_file(f"{COUNTER:08d} of {QUANTITY}\t{host_answer.status_code}\t  {target_url}")
                lock.release()
            else:
                lock.acquire()
                print(f"{COUNTER:08d} of {QUANTITY}\t{Fore.GREEN}{host_answer.status_code}{Fore.RESET}\t{target_url}"
                      f"{' '*100}")
                save_to_file(f"{COUNTER:08d} of {QUANTITY}\t{host_answer.status_code}\t  {target_url}")
                lock.release()
    except KeyboardInterrupt:
        print(f'  {Fore.RED}ERROR: manually stop Ctrl+C{Fore.RESET}')


def init(l):
    global lock
    lock = l


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dir Fuzzer", usage="Script "
                                                                     "options")
    parser.add_argument("-u", help="Enter domain https://site.com")
    parser.add_argument("-w", help="Name and path of the wordlist")
    parser.add_argument("-t", help="Threads quantity", type=int)
    parser.add_argument("-b64", help="encode to base64", action="store_true")
    parser.add_argument("-uenc", help="encode to urlencode", action="store_true")
    parser.add_argument("-head", help="HTTP headers", type=str)
    args = parser.parse_args()
    greetings()
    check_app_keys(args, parser)
    l = Lock()
    try:
        with Pool(args.t, initializer=init, initargs=(l, )) as pool:
            pool.map(get_site_dirs, DIRS)
    except KeyboardInterrupt:
        print("Error")































