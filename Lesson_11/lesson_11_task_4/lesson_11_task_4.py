#  Классы и ООП: Задание 4 - 40 баллов


class ColorANSI:

    def __init__(self, color):
        if color == 1:
            self.color = '42'
        elif color == 2:
            self.color = '41'
        elif color == 3:
            self.color = '44'
        else:
            self.color = '45'

    def color_string(self, string):
        print(f'\033[{self.color}m{string}\033[0m')


if __name__ == '__main__':
    for index, value in enumerate(('Зеленый', 'Красный', 'Синий', 'Пурпурный'),
                                1):
        print(str(index) + ') ' + value)
    color_number = int(input('Выберите цвет: '))
    string = input('Введите строку: ')
    new_color = ColorANSI(color_number)
    new_color.color_string(string)


