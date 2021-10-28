#  Модули и пакеты: Задание 5.1 - 100 баллов


def new_format(string):
    string_1 = '+-' * len(string) + '+'
    string_2 = '|' + '|'.join(string) + '|'
    print(string_1)
    print(string_2)
    print(string_1)
