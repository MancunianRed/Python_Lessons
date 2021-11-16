#  Классы и ООП часть 2: Задание 2 - 35 баллов
class AccountBalance:
    def __init__(self, name, summa, prepayment='аванс'):
        self.name = name
        self.summa = summa
        self.prepayment = prepayment


class AccountBalanceWithSalary(AccountBalance):
    def __init__(self, name, summa, summa2, salary='зарплата'):
        self.salary = salary
        self.summa2 = summa2
        super().__init__(name, summa, prepayment='аванс')


if __name__ == '__main__':
    employee_1 = AccountBalance('Vasya', 6)
    employee_2 = AccountBalanceWithSalary('Petya', 10, 20)
    print(f'{employee_1.name} - {employee_1.prepayment} {employee_1.summa} '
          f'рублей.')
    print(f'{employee_2.name} - {employee_2.prepayment} {employee_2.summa} '
          f'рублей, {employee_2.salary} {employee_2.summa2} рублей.')