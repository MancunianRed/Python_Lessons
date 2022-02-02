#  Пишем фреймворк: Задание 1 - 200 баллов
import requests
import fake_useragent


def get_page_data(html):
    res = html.text
    print(res)


def request_robots_data():
    url = input("Enter host [https://site.com]: ")
    ua = fake_useragent.UserAgent()
    head = {"User-Agent": ua.random}
    if url[-1] == "/":
        page = requests.get(url + "robots.txt", headers=head)
    else:
        page = requests.get(url + "/robots.txt", headers=head)
    if page.status_code != 404:
        get_page_data(page)
    else:
        print("FIle 'robots.txt' not found")


