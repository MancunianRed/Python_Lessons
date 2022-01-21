#  Пишем парсер: Задание 3 - 150 баллов
import requests
from bs4 import BeautifulSoup


def get_request(url):
    try:
        res = requests.get(url).text
    except Exception as e:
        print("Error", e)
    else:
        soup = BeautifulSoup(res, "lxml")
        return soup


def pager(soup):
    a = soup.find("div", class_="pager").find_all("a")[-1].text
    return a


def get_result(soup):
    tr_list = soup.find("table", id="theProxyList").find("tbody").find_all("tr")
    for tr in tr_list:
        td = tr.find_all("td")
        proxy_name = f"{td[1].text:<17}:{td[2].text}"
        print(proxy_name)


if __name__ == "__main__":
    url = "http://foxtools.ru"
    ext_url = "/Proxy"
    soup = get_request(url+ext_url)
    pages = int(pager(soup))
    if pages > 0:
        for page in range(pages):
            get_result(get_request(url + f"/Proxy?page={page+1})"))

