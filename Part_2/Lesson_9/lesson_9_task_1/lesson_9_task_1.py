#  Пишем конвертеры для полезных нагрузок: Задание 1 - 50 баллов
import base64
import urllib.parse


with open("task.txt", "r", encoding="unicode_escape") as reader:
    text = reader.readline()
text = urllib.parse.unquote(text)
print(base64.b64decode(bytes(text, "utf-8")).decode("utf-8"))



