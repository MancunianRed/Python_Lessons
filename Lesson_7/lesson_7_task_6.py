#  Модули и пакеты: Задание 6 - 150 баллов
import random
import time
count = 0
roads = {}
for i in range(3):
    print(str(i+1) + ')')
    for j in range(random.randint(10, 30)):
        print('#', end='')
        time.sleep(0.5)
        count += 1
    if i+1 == 1:
        roads['one'] = count
    elif i+1 == 2:
        roads['two'] = count
    else:
        roads['three'] = count
    count = 0
    print()
if roads.get('one') >= roads.get('two') and roads.get('one') >= roads.get(
        'three'):
    print('Дорожка one из', roads.get('one'), 'сим. победила!')
elif roads.get('two') >= roads.get('one') and roads.get('two') >= roads.get(
        'three'):
    print('Дорожка two из', roads.get('two'), 'сим. победила!')
else:
    print('Дорожка three из', roads.get('three'), 'сим. победила!')
