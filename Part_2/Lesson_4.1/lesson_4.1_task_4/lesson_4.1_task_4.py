#  Регулярные выражения: Задание 3 - 130 баллов
import re

with open('surnames.txt', encoding='utf-8') as reader, \
    open('woman.txt', 'a', encoding='utf-8') as writer_woman, \
    open('man.txt', 'a', encoding='utf-8') as writer_man:
    for name in reader:
        if (res := re.match(r'.+АЯ|.+ВА|.+НА', name)) is not None:
            writer_woman.write(res.group().strip().title() + '\n')
        else:
            writer_man.write(name.strip().title() + '\n')