#  Пишем генератор ключевых слов для брутфорса: Задание 2 - 100 баллов
import string
import itertools


def file_writer(list_of_combinations):
    with open("gen_dict.txt", "w", encoding="utf-8") as writer:
        for var in list_of_combinations:
            writer.write(''.join(var) + "\n")
    print("Done!")


def data_input():
    try:
        args = set(input("Выберите аргументы: \n").lower())
        symbols = int(input("Количество символов в слове? \n"))
    except ValueError:
        print("Ошибка! Введите целое число больше нуля!")
        data_input()
    else:
        combinations(symbols, args)


def combinations(symbols, args):
    if symbols <= 0:
        print("Ошибка! Введите целое число больше нуля!")
        data_input()
    else:
        pass_chars_dict = {"b": string.ascii_uppercase,
                           "l": string.ascii_lowercase,
                           "s": string.punctuation,
                           "n": string.digits}
        pass_chars = ''
        for var in args:
            pass_chars = pass_chars + pass_chars_dict.get(var)
        list_of_combinations = itertools.product(pass_chars, repeat=symbols)
        print(f"Количество комбинаций: {len(pass_chars)**symbols}")
        file_writer(list_of_combinations)


if __name__ == "__main__":
    print("Keyword generator\n\nB - большие буквы\nL - маленькие буквы\nS - "
          "спецсимволы\nN - числа\n")
    data_input()