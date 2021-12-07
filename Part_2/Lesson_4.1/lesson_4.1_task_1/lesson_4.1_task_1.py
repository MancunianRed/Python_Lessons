#  Регулярные выражения: Задание 1 - 30 баллов
import re

text = 'Сначала был адрес http://yandex.ru, потом стал https://yandex.ru.' \
       ' \ Гугл https://google.com имеет шире охват чем https://yandex.ru.'

res = re.findall(r'(https?://[\w]+\.[a-z]+)', text)
for url in sorted(set(res)):
    print(''.join(url))
