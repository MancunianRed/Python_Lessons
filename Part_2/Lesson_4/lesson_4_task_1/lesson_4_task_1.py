#  Регулярные выражения: Задание 1 - 20 баллов

import re

text = 'Московское время 10:36:06'

res = re.findall(r'[\d:]', text)
print(''.join(res))