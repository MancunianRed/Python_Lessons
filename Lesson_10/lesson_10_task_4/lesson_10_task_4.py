#  Форматирование: Задание 4 - 50 баллов


def years_to_million(amount_1):
    amount = amount_1
    years = 1
    while amount < 1000000:
        amount = amount*2
        years += 1
    print(f'Понадобится {years} лет чтобы стать миллионером при доходе'
          f' {amount_1}$ за первый год')


def money_in_first_year(total_years):
    money = 1000000
    for i in range(total_years-1):
        money = money / 2
    print(f'Понадобится заработать в первый год {money:.2f}$ чтобы стать '
          f'миллионером за {total_years} лет')


if __name__ == '__main__':
    years_to_million(15625)
    money_in_first_year(10)