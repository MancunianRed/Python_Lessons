#  Функции: Задание 1 - 25 баллов
new_str = input('Введите предложение: ')


def without_space(a):
    """
Программа считает количество символов без учёта пробелов
    """
    if len(a.replace(' ', '')) % 10 == 1 and len(a.replace(' ', '')) != 11:
        end_sum = ''
    elif len(a.replace(' ', '')) % 10 in (2, 3, 4) and len(a.replace
                                        (' ', '')) not in (12, 13, 14):
        end_sum = 'а'
    else:
        end_sum = 'ов'
    print('В предложении ', len(a.replace(' ', '')), ' символ' + end_sum)
    print(without_space.__doc__)


without_space(new_str)

