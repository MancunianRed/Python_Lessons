#  Регулярные выражения: Задание 3 - 50 баллов
import re

with open('job.txt', encoding='utf-8') as reader:
    for job in reader:
        if (res := re.search(r'[К-С].{5}к', job)) is not None:
            print(res.group())