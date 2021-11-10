#  Форматирование: Задание 2 - 35 баллов


def input_exchange_rate():
    exchange = float(input('Введите курс доллара США к канадскому доллару: '))
    return exchange


def input_currency_amount():
    amount = float(input('Введите количество долларов: '))
    return amount


if __name__=='__main__':
    print('По курсу %.2f за доллар США выполучите %.2f канадских доллара' %
          (exrt := input_exchange_rate(), amnt := exrt*input_currency_amount()))
    print('По курсу {:.2f} за доллар США выполучите {:.2f} канадских '
          'доллара'.format(exrt, amnt))
    print(f'По курсу {exrt:.2f} за доллар США выполучите {amnt:.2f} канадских '
          'доллара')