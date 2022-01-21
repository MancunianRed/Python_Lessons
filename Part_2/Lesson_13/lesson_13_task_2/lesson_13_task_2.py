#  Пишем парсер: Задание 2 - 100 баллов
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests


def get_request(url):
    ua = UserAgent()
    try:
        res = requests.get(url, params=ua.random).text
    except Exception as e:
        print("Error", e)
    else:
        soup = BeautifulSoup(res, "lxml")
        member_search(soup)


def member_search(soup):
    members = soup.find("ol", class_="block-body").\
        find_all("li", class_="block-row--separated")
    for member in members:
        name = member.find("span", class_="username--staff").text
        print(name.strip())


if __name__ == "__main__":
    url = "https://codeby.net/members/?key=staff_members"
    get_request(url)