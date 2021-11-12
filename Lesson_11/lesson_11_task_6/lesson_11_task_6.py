#  Классы и ООП: Задание 6 - 120 баллов
from random import randint


class Humans:

    def __init__(self, name):
        self.name = name
        self.list_1 = list()
        self.attempts = {self.name: self.list_1}

    def target(self):
        print(f'Стреляет {self.name}:')
        for i in range(3):
            attempt_range = randint(1, 10)
            if attempt_range < 5:
                self.list_1.append(0)
                print(f'Попытка {i + 1}: {self.list_1[i]:02d} оч. Мазила!')
            elif 5 <= attempt_range < 8:
                self.list_1.append(attempt_range)
                print(f'Попытка {i + 1}: {self.list_1[i]:02d} оч. Так себе!')
            elif 8 <= attempt_range <= 9:
                self.list_1.append(attempt_range)
                print(f'Попытка {i + 1}: {self.list_1[i]:02d} оч. Неплохо')
            else:
                self.list_1.append(attempt_range)
                print(f'Попытка {i + 1}: {self.list_1[i]:02d} оч. Меткий '
                      f'выстрел')


def champion():
    print('-'*39)
    dict_1 = {artur.name: sum(artur.attempts.get(artur.name)),
              semen.name: sum(semen.attempts.get(semen.name)),
              daniil.name: sum(daniil.attempts.get(daniil.name))}
    sorted_keys = sorted(dict_1, key=dict_1.get, reverse=True)
    for i in range(3):
        print(f'{i+1} место в стрельбе из лука: {sorted_keys[i]} - '
              f'{dict_1.get(sorted_keys[i]):02d} оч.')


if __name__ == '__main__':
    artur = Humans('Артур')
    semen = Humans('Семен')
    daniil = Humans('Даниил')
    artur.target()
    semen.target()
    daniil.target()
    champion()

