#  Исключения: Задание 2 - 35 баллов
from Lesson_8.animals import *
import random

animals_dict = {1: (deer, 'deer'), 2: (cat, 'cat'), 3: (cow, 'cow'),
                    4: (frog, 'frog'), 5: (bat, 'bat'),
                    6: (butterfly, 'butterfly')}


def check_legal_value():
    try:
        number = int(input('Введите номер рисунка: '))
    except(ValueError, EOFError):
        return
    else:
        if 7 >= number >= 1:
            return number
        else:
            return


def choice_help():
    print('Help:', '\n')
    for i in animals_dict:
        print('   ', str(i) + ')', animals_dict.get(i)[1])
    print('    7) random\n')


def print_animals(a):
    if a is not None and 7 > a >= 1:
        print(animals_dict.get(a)[0])
    elif a == 7:
        print(animals_dict.get(random.randint(1, 7))[0])
    else:
        print('Введите число от 1 до 7.')


if __name__ == '__main__':
    choice_help()
    print_animals(check_legal_value())




