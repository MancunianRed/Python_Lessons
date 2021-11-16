#  Классы и ООП часть 2: Задание 4 - 100 баллов


class TextFormat:
    def __init__(self, word):
        self.word = word
        print(self.word)


def my_decorator(function_to_decorate):
    def wrap():
        string_1 = '+' + '-+' * len(function_to_decorate.word)
        string_2 = '|' + '|'.join(function_to_decorate.word) + '|'
        print(f'{string_1}\n{string_2}\n{string_1}')
    return wrap


if __name__ == '__main':
    new_function = my_decorator(TextFormat('Hello'))
    new_function()

