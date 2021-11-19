#  Классы и ООП: Задание 5 - 100 баллов


class Trapeze:

    def __init__(self, d1, d2, h):
        self.d1 = d1
        self.d2 = d2
        self.h = h

    def trapeze_square(self):
        if self.h >= self.d1 or self.h >= self.d2 or self.h == 0 or \
                self.d1 == 0 or self.d2 == 0:
            print('\nВведите корректные параметры трапеции.')
        else:
            s = (((self.d2**2 - self.h**2)**0.5 + (self.d1**2 -
                                                   self.h**2)**0.5) / 2)*self.h
            print(f'\nПлощадь трапеции {s:.2f} кв.м')


if __name__ == '__main__':
    d1 = int(input('Введите диагональ трапеции 1: '))
    d2 = int(input('Введите диагональ трапеции 2: '))
    h = int(input('Введите высоту трапеции: '))
    trapeze = Trapeze(d1, d2, h)
    trapeze.trapeze_square()

