#  test
import requests
from bs4 import BeautifulSoup
import re

def get_html(url):
    r = requests.get(url)

    return r.text

def get_all_links(html):
    soup = BeautifulSoup(html, "lxml")
    divs = soup.find("div", class_="exchanges-page__content").find_all("div",
                                                                      class_="CardWrapper")
    links = {}
    for div in divs:
        a = div.find("div", class_="Typography cardHeadlineL align").text
        b = div.find("span", class_="text-address").text

        links[b] = a
    return links


def main():
    url = "https://minfin.com.ua/currency/auction/exchanger/usd/sell/odessa/"
    all_links = get_all_links(get_html(url))
    print(all_links)
    min = float()
    minimum = ""
    for key in all_links.keys():
        s = re.match(r"\d+,\d+", all_links[key])
        d = float(re.sub(",", ".", s.group()))
        if min > d:
            min = d
            minimum = key


    print(min)
    print(minimum)


if __name__ == "__main__":
    main()
