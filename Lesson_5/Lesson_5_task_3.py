#  Циклы: Задание 3 - 40 баллов
jewel = ['золото', 'алмазы', 'серебро', 'сапфиры', 'бронза', 'рубины',
         'платина', 'изумруды', 'палладий', 'аметисты']
metal = []
stone = []
for i in range(1, len(jewel), 2):
    stone.append(jewel[i])
    metal.append(jewel[i-1])
for index, value in enumerate(metal):
    index += 1
    print(index, value)
print()
for index, value in enumerate(stone):
    index += 1
    print(index, value)