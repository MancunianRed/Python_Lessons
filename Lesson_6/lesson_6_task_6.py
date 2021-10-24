#  Функции: Задание 6 - 150 баллов


def count_symbols_and_spaces(a):
    if len(a) % 10 == 1 and len(a) != 11:
        last_symbol = ''
    elif len(a) % 10 in (2, 3, 4) and len(a) not in (12, 13, 14):
        last_symbol = 'а'
    else:
        last_symbol = 'ов'
    print('В предложении', len(a), 'символ' + last_symbol)


def count_words(a):
    string_list = a.split()
    if len(string_list) % 10 == 1 and len(string_list) != 11:
        last_symbol = 'о'
    elif len(string_list) % 10 in (2, 3, 4) and len(string_list) not in \
            (12, 13, 14):
        last_symbol = 'а'
    else:
        last_symbol = ''
    print('В предложении', len(string_list), 'слов' + last_symbol)


def count_symbols(a):
    arg = set(a)
    print('Сколько раз встречается каждый знак: ', end='\n')
    for i in sorted(arg):
        print(i, '-', a.count(i))


if __name__ == '__main__':
    string = input('Введите предложение: ')
    count_symbols_and_spaces(string)
    count_words(string)
    count_symbols(string)


