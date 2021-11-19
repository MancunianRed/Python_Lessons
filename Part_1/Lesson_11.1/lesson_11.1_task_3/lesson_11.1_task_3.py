#  Классы и ООП часть 2: Задание 3 - 50 баллов


class Ellipse:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sqr(self):
        try:
            s = 3.14 * self.a * self.b
        except TypeError:
            print('Введите корректные данные!')
        else:
            print(f'{s:.2f}')


class Conus(Ellipse):
    def __init__(self, a, b):
        super().__init__(a, b)

    def sqr(self):
        try:
            v = (self.b / 3) * 3.14 * self.a**2
        except TypeError:
            print('Введите корректные данные!')
        else:
            print(f'{v:.2f}')


if __name__ == '__main__':
    Ellipse(3, 4).sqr()
    Conus(3, 4).sqr()
