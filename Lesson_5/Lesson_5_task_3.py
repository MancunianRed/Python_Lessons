#  Циклы: Задание 3 - 40 баллов
jewel = ['золото', 'алмазы', 'серебро', 'сапфиры', 'бронза', 'рубины',
         'платина', 'изумруды', 'палладий', 'аметисты']
for index, value in enumerate(jewel[::2], start=1):
    print(index, value)
print()
for index, value in enumerate(jewel[1::2], start=1):
    print(index, value)





