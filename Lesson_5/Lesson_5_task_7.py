#  Циклы: Задание 7 - 120 баллов
targets = ["7 раз отмерь, 1 раз отрежь.", "Не имей 100 рублей, а имей 100 "
                                          "друзей.", "1 за всех и все за 1."]
total_sum = 0
for i in range(len(targets)):
    for j in targets[i].split(' '):
        j = j.strip('.')
        if j.isdigit():
            total_sum = total_sum + int(j)
print(total_sum)


