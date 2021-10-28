#  Модули и пакеты: Задание 2 - 35 баллов
import time


def time_dif():
    print('Время пошло')
    time_start = time.time()
    word = input('Введите текст: ')
    time_stop = time.time()
    time_differ = round(time_stop - time_start, 3)
    word_time = (word, time_differ)
    return word_time


def time_math(*args):
    str_amount = len(args[0])
    print('Прошло', args[1], 'сек')
    print('Ваша скорость набора', round(60*str_amount/args[1]),
          'знаков в минуту')


args_1 = time_dif()
time_math(*args_1)
