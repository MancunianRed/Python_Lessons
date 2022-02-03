#  Пишем фреймворк: Задание 1 - 200 баллов
import requests
import fake_useragent
import Part_2.Lesson_16.lesson_16_task_1.full_scripts.input_text_check as in_text
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def get_page_data(html):
    res = html.text
    print(res)


def request_robots_data():
    url = in_text.input_text("Enter host [https://site.com]: ")
    ua = fake_useragent.UserAgent()
    head = {"User-Agent": ua.random}
    try:
        if url[-1] == "/":
            page = requests.get(url + "robots.txt", headers=head)
        else:
            page = requests.get(url + "/robots.txt", headers=head)
    except Exception as e:
        print(f"{Fore.RED}==> Error: {e}{Fore.RESET}")
    else:
        if page.status_code != 404:
            get_page_data(page)
        else:
            print("FIle 'robots.txt' not found")



