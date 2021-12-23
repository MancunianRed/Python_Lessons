#  Многопоточность: Задание 2 - 30 баллов
from queue import LifoQueue
import time

q_lifo = LifoQueue()

print("Собираем стопку монет...")
for coin in range(1, 11):
    print(coin, end=" ")
    q_lifo.put(coin)
    time.sleep(1)

print("\nРазбираем стопку монет...")
while not q_lifo.empty():
    print(q_lifo.get(), end=" ")
    time.sleep(1)
