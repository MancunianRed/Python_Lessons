#  Пишем генератор ключевых слов для брутфорса: Задание 1 - 50 баллов
import string
import itertools


def file_writer(list_of_combinations):
    with open("my_dict.txt", "w", encoding="utf-8") as writer:
        for var in list_of_combinations:
            writer.write(''.join(var) + "\n")
    print("Done!")


def data_input():
    try:
        symbols = int(input("Количество символов в слове: "))
    except ValueError:
        print("Ошибка! Введите целое число больше нуля!")
        data_input()
    else:
        combinations(symbols)


def combinations(symbols):
    if symbols <= 0:
        print("Ошибка! Введите целое число больше нуля!")
        data_input()
    else:
        pass_chars = string.ascii_letters + string.digits
        list_of_combinations = itertools.product(pass_chars, repeat=symbols)
        print(f"Количество комбинаций: {len(pass_chars)**symbols}")
        file_writer(list_of_combinations)


if __name__ == "__main__":
    print("Keyword generator\n")
    data_input()