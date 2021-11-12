#  Классы и ООП: Задание 2 - 25 баллов


class Bullets:

    def __init__(self, bullets_total):
        self.bullets_total = bullets_total

    def time_to_empty(self):
        if self.bullets_total < 250 or self.bullets_total > 10000:
            print('Введите число от 250 до 10000.')
        else:
            if self.bullets_total % 250 == 0:
                recharge = (int(self.bullets_total / 250) * 20) - 20
            else:
                recharge = int(self.bullets_total / 250) * 20

            print('Патроны закончатся через', self.bullets_total / 20 +
                  recharge, 'сек.')


if __name__ == '__main__':
    new_count = Bullets(333)
    new_count.time_to_empty()
