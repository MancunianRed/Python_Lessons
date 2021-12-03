#  Регулярные выражения: Задание 2 - 40 баллов
import re

with open('proxy.txt', encoding='utf-8') as reader:
    for ip in reader:
        if (res := re.match(r'(\d+\.?)+', ip)) != 0:
            print(res.group())
