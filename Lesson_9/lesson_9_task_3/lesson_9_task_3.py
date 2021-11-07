#  Работа с файлами: Задание 3 - 50 баллов

try:
    with open('city.txt', encoding='utf-8') as file:
        with open('city_2.txt', 'a', encoding='utf-8') as file1:
            for i in file.readlines():
                if 'о' not in i:
                    file1.write(str(i.strip()) + '\n')
except:
    print('File error')

