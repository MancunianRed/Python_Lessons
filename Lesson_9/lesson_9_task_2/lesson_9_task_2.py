#  Работа с файлами: Задание 2 - 25 баллов

try:
    with open('city.txt', encoding='utf-8') as file:
        print(len(file.readlines()))
except FileNotFoundError:
    print('File error')

