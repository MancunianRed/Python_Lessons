#  Функции: Задание 5 - 80 баллов
arguments = input('Введите аргументы: ')
arguments_list = arguments.split()


def square_math(*args):
    if len(args) == 1:
        print('Площадь круга: ', round(3.14 * int(args[0]) ** 2 / 4, 2),
              ' кв. метров')
    elif len(args) == 2:
        print('Площадь прямоугольника: ', int(args[0]) * int(args[1]),
              ' кв. метров')
    else:
        side = (int(args[0]) + int(args[1]) + int(args[2])) / 3
        print('Площадь треугольника: ', round((3 ** 0.5 * side ** 2) / 4, 2),
              ' кв. метров')


square_math(*arguments_list)
