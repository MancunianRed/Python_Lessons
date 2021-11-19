#  Классы и ООП часть 2: Задание 4 - 100 баллов


def my_decorator(function_to_decorate):
    def wrap(*args):
        string_1 = '+' + '-+' * len(*args)
        string_2 = '|' + '|'.join(*args) + '|'
        print(f'{string_1}\n{string_2}\n{string_1}')
        return function_to_decorate
    return wrap


@my_decorator
class TextFormat:
    def __init__(self, word):
        self.word = word
        print(self.word)


if __name__ == '__main__':
    TextFormat('Игорь Пройченко')