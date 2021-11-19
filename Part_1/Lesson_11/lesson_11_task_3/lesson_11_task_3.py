#  Классы и ООП: Задание 3 - 30 баллов


class Person:
    def __init__(self, cash, name, position):
        self.__cash = cash
        self.name = name
        self.position = position

    def money(self):
        return self.__cash


people = Person('20000', 'Вася', 'Дворник')
man = Person('150000', 'Жора', 'Гендиректор')
print(f'{people.position} {people.name} получил зарплату '
      f'{people.money()} рублей')
print(f'{man.position} {man.name} получил зарплату {man.money()} рублей')