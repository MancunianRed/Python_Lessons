#  Функции: Задание 2 - 25 баллов
bullets_total = int(input('Введите количество патронов: '))


def time_to_empty(bullets):
    if bullets < 250 or bullets > 10000:
        print('Введите число от 250 до 10000.')
    else:
        if bullets % 250 == 0:
            recharge = (int(bullets / 250) * 20) - 20
        else:
            recharge = int(bullets / 250) * 20

        print('Патроны закончатся через', bullets / 20 + recharge, 'сек.')


time_to_empty(bullets_total)
