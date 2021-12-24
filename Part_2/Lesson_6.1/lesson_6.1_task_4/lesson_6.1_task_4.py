#  Работа с сетью: Задание 4 - 60 баллов
import requests

url = "https://belarusbank.by/api/kursExchange"
res = requests.get(url)
res_json = res.json()[0]
keys = list(res_json.keys())
print(f"Курсы валют в Минске на сегодня:")
for i in keys[0:5]:
    print(f"{i + ':':<8}{res_json.get(i)[0:4]:>7} руб.")

