#  Модули и пакеты: Задание 6 - 150 баллов
import random
import time


def roads_print(results):
    for i in range(results):
        print('#', end='')
        time.sleep(0.5)
    print()


table_results = {x: random.randint(10, 30) for x in ('one', 'two', 'three')}

print(' Старт! '.center(30, '-'))
count = 1
for i in table_results.keys():
    print(str(count) + ')')
    roads_print(table_results.get(i))
    count += 1
for number, length in table_results.items():
    if length == max(table_results.values()):
        print('Дорожка', number, 'из', length, 'сим. победила!')
