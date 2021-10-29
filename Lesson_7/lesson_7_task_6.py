#  Модули и пакеты: Задание 6 - 150 баллов
import random
import time


def roads_print(results):
    for i in range(results):
        print('#', end='')
        time.sleep(0.5)
    print()


def get_the_winner(**kwargs):
    print(' Старт! '.center(30, '-'))
    for num, i in enumerate(kwargs.keys(), 1):
        print(str(num) + ')')
        roads_print(kwargs.get(i))


def result(**kwargs):
    for number, length in kwargs.items():
        if length == max(kwargs.values()):
            print('Дорожка', number, 'из', length, 'сим. победила!')


if __name__ == "__main__":
    table_results = {x: random.randint(10, 30) for x in ('one', 'two', 'three')}
    get_the_winner(**table_results)
    result(**table_results)

