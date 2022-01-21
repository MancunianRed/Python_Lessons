#  Пишем парсер: Задание 1 - 50 баллов
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_request(url):
    user_agent = UserAgent().random
    try:
        res = requests.get(url, params=user_agent).text
    except Exception as e:
        print("Error", e)
    else:
        soup = BeautifulSoup(res, "lxml")
        names_print(soup)


def names_print(soup):
    list_of_names = soup.find("div", id="pt").find_all("a")
    for name in list_of_names[0:9]:
        print(name.text)


if __name__ == "__main__":
    url = "https://vdoh.ru/whatever/list/znamenitosti"
    get_request(url)