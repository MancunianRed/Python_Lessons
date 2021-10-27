#  Модули и пакеты: Задание 2 - 35 баллов
import time

print('Время пошло')
time_start = time.time()
string = input('Введите текст: ')
time_stop = time.time()
time_dif = round(time_stop - time_start, 3)
str_amount = len(string)
print('Прошло', time_dif, 'сек')
print('Ваша скорость набора', round(60*str_amount/time_dif), 'знаков в минуту')
