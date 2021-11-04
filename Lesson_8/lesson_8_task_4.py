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
        if (number := input_check()) is None:
            if i == 2:
                print('Удача не на твоей стороне, попробуй ещё!')
            else:
                print('Ошибка! Введите число от 1 до 10')
            continue
        elif number > 10:
            if i == 2:
                print('Удача не на твоей стороне, попробуй ещё!')
            else:
                print('Ошибка! Введите число от 1 до 10')
                print('Ваше число больше')
            continue
        elif number < 1:
            if i == 2:
                print('Удача не на твоей стороне, попробуй ещё!')
            else:
                print('Ошибка! Введите число от 1 до 10')
                print('Ваше число меньше')
            continue
        elif number > random_number:
            if i == 2:
                print('Удача не на твоей стороне, попробуй ещё!')
            else:
                print('Ваше число больше')
            continue
        elif number < random_number:
            if i == 2:
                print('Удача не на твоей стороне, попробуй ещё!')
            else:
                print('Ваше число меньше')
            continue
        elif number == random_number:
            print('Ты победил!')
            break


if __name__ == '__main__':
    game()
