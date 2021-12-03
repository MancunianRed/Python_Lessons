#  Регулярные выражения: Задание 2 - 40 баллов
import re

with open('proxy.txt', encoding='utf-8') as reader:
    for ip in reader:
        if (res := re.match(r'(\d{1,3}\.){3}\d{1,3}', ip)) is not None:
            print(res.group())
