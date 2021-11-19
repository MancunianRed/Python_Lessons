#  Работа с файлами: Задание 3 - 50 баллов

with open('city.txt', encoding='utf-8') as reader, \
        open('city_2.txt', 'a', encoding='utf-8') as writer:
    for i in reader.readlines():
        if 'о' not in i:
            writer.write(str(i.strip()) + '\n')



