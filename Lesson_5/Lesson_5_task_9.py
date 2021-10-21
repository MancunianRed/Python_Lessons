#  Циклы: Задание 9 - 150 баллов
target_ints = [1, 3, 3, 4, 7, 9]
remove_ints = []
count = 0
for i in target_ints:
    for j in target_ints:
        if i == j:
            count = count + 1
    if count < 2:
        remove_ints.append(i)
    count = 0
for i in remove_ints:
    if i in target_ints:
        target_ints.remove(i)
print(target_ints)