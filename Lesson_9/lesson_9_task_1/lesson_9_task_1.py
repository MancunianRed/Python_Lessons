#  Работа с файлами: Задание 1 - 25 баллов

try:
    with open('numbers.txt', 'a') as file:
        for i in range(10000):
            file.write(str(i+1) + '\n')
except:
    print('File error')

