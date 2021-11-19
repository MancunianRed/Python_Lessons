#  Циклы: Задание 3 - 40 баллов
jewel = ['золото', 'алмазы', 'серебро', 'сапфиры', 'бронза', 'рубины',
         'платина', 'изумруды', 'палладий', 'аметисты']
for i in range(2):
    for index, value in enumerate(jewel[i::2], 1):
        print(index, value)
    print()



