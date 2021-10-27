#  Модули и пакеты: Задание 5.1 - 100 баллов


def new_format(string):
    string_list = list(string)
    list1 = []
    list2 = []
    for i in string_list:
        if string_list.index(i) == 0:
            list2.append('|')
            list1.append('+')
            list2.append(i)
            list1.append('-')
            list2.append('|')
            list1.append('+')
        else:
            list2.append(i)
            list1.append('-')
            list2.append('|')
            list1.append('+')
    print(''.join(list1))
    print(''.join(list2))
    print(''.join(list1))
