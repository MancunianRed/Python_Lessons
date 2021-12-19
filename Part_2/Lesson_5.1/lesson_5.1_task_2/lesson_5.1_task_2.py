#  Многопоточность: Задание 2 - 30 баллов
from queue import LifoQueue
from queue import Queue
import time

q_lifo = LifoQueue()
q_fifo = Queue()

for coin in range(1, 11):
    q_fifo.put(coin)
    q_lifo.put(coin)

print("Собираем стопку монет...")
while not q_fifo.empty():
    print(q_fifo.get(), end=" ")
    time.sleep(1)

print("\nРазбираем стопку монет...")
while not q_lifo.empty():
    print(q_lifo.get(), end=" ")
    time.sleep(1)
