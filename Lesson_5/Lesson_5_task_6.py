#  Циклы: Задание 6 - 100 баллов
n = 18
while n >= 4:
    print(('&'*n).center(18))
    if n == 4:
        break
    n = n - 2
while n <= 18:
    print(('&'*n).center(18))
    n = n + 2