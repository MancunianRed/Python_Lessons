#  Циклы: Задание 5 - 80 баллов
number = '321065452012615015041652469504158791051017052612101190152612016520' \
         '941501206206'
count = 0
for i in range(0, len(number), 2):
    count = count + int(number[i] + number[i+1])
print(count)