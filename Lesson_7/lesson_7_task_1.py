#  Модули и пакеты: Задание 1 - 25 баллов
import string
import random

lit_s = list(string.ascii_letters)
dig = list(string.digits)
lit_s.extend(dig)
list_10 = []
for i in range(10):
    list_10.append(lit_s[random.randint(0, len(lit_s) - 1)])
print(list_10)
