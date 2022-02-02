#  Пишем фреймворк: Задание 1 - 200 баллов
import requests
from bs4 import BeautifulSoup


def get_page_data(html):
    res = BeautifulSoup(html.text, "lxml")
    line = res.find_all("loc")
    for i in line:
        print(i.text)


def get_sitemap_data():
    url = input("Enter host [https://site.com]: ")
    # ua = fake_useragent.UserAgent()
    # head = {"User-Agent": ua.random}
    if url[-1] == "/":
        page = requests.get(url + "sitemap.xml")
    else:
        page = requests.get(url + "/sitemap.xml")
    if page.status_code == 200:
        get_page_data(page)
    else:
        print("FIle 'sitemap.xml' not found")


