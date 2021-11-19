#  Исключения: Задание 1 - 25 баллов
import random


try:
    number = int(input('Введите число от 1 до 10: '))
except ValueError:
    print('Ошибка ввода! Введите число от 1 до 10.')
except EOFError:
    print('Отмена операции')
else:
    if number < 1 or number > 10:
        print(' Введите число от 1 до 10')
    else:
        sum_1 = number
        if (rand := random.randint(10, 100)) == number:
            print(number + rand)
        else:
            for i in range(rand - number):
                sum_1 = sum_1 + (number + (i + 1))
            print(sum_1)
