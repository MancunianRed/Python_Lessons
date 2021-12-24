#  Работа с сетью: Задание 1 - 20 баллов
import requests

res = requests.get("https://example.com/")
for i in res.headers.items():
    print(":".join(i))
