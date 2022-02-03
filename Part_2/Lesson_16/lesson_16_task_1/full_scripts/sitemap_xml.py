#  Пишем фреймворк: Задание 1 - 200 баллов
import requests
from bs4 import BeautifulSoup
import Part_2.Lesson_16.lesson_16_task_1.full_scripts.input_text_check as in_text
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def get_page_data(html):
    res = BeautifulSoup(html.text, "lxml")
    line = res.find_all("loc")
    for i in line:
        print(i.text)


def get_sitemap_data():
    url = in_text.input_text("Enter host [https://site.com]: ")
    try:
        if url[-1] == "/":
            page = requests.get(url + "sitemap.xml")
        else:
            page = requests.get(url + "/sitemap.xml")
    except Exception as e:
        print(f"{Fore.RED} ==>> Error: {e}{Fore.RESET}")
    else:
        if page.status_code == 200:
            get_page_data(page)
        else:
            print("FIle 'sitemap.xml' not found")


