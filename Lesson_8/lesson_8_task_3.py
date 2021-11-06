#  Исключения: Задание 3 - 40 баллов
import time


def input_check():
    try:
        number = int(input('Введите число от 10 до 30: '))
    except (ValueError, EOFError):
        return
    else:
        if 30 >= number >= 10:
            return number


def timer_count(b):
    if (a := b) is None or 10 > a > 30:
        print('Ошибка! Введите число от 10 до 30')
    else:
        count = a
        for i in range(a + 1):
            print('\r' + str(count) + " ", flush=True, end='')
            count = count - 1
            time.sleep(1)


if __name__ == '__main__':
    timer_count(input_check())
