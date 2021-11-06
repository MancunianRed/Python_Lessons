#  Исключения: Задание 4 - 80 баллов
import random


def input_check():
    try:
        number = int(input('Введите число от 1 до 10: '))
    except (ValueError, EOFError):
        return
    else:
        return number


def game():
    random_number = random.randint(1, 10)
    for i in range(3):
        if (number := input_check()) == random_number:
            print('Ты победил!')
            break
        elif i == 2:
            print('Удача не на твоей стороне, попробуй ещё!')
            break
        else:
            if number > 10 or number < 1:
                print('Ошибка! Введите число от 1 до 10')
            if number > random_number:
                print('Ваше число больше')
            elif number < random_number:
                print('Ваше число меньше')


if __name__ == '__main__':
    game()
