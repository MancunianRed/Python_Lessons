#  Циклы: Задание 9 - 150 баллов
target_ints = [1, 3, 3, 4, 7, 9]
updated_ints = []
for i in target_ints:
    if target_ints.count(i) < 2:
        updated_ints.append(i)
for i in updated_ints:
    if i in target_ints:
        target_ints.remove(i)
print(target_ints)