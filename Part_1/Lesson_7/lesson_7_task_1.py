#  Модули и пакеты: Задание 1 - 25 баллов
import string
import random

lit_s = list(string.ascii_letters)
dig = list(string.digits)
lit_s.extend(dig)
print(random.sample(lit_s, 10))


