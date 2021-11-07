#  Работа с файлами: Задание 2 - 25 баллов

# try:
#     with open('city.txt', encoding='utf-8') as file:
#         print(len([i for i in file.readlines()]))
# except FileNotFoundError:
#     print('File not found')

try:
    with open('../lesson_9_task_3/city.txt', encoding='utf-8') as file:
        count = 0
        for i in file.readlines():
            count += 1
        print('Количество строк в файле: ', count)
except:
    print('File error')

