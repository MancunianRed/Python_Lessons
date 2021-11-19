#  Модули и пакеты: Задание 5.1 - 100 баллов


def new_format(string):
    string_1 = '+-' * len(string) + '+'
    string_2 = '|' + '|'.join(string) + '|'
    agrs = (string_1, string_2)
    return agrs
