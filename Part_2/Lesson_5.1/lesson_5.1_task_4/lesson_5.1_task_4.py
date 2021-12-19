#  Многопоточность: Задание 4 - 100 баллов
from multiprocessing import Queue
from multiprocessing import Process


def action(num, q):
    q.put(num)
    print(f"Курсант {num+1} начал снаряжать магазин")
    for bullet in range(1, 31):
        print(bullet, end=" ")
    print()
    print(f"Курсант {num+1} снарядил магазин\n")


if __name__ == "__main__":
    q = Queue()
    my_process = []
    for i in range(5):
        new_thread = Process(target=action, name=str(i+1),  args=(i, q))
        new_thread.start()
        q.get()
    for l in my_process:
        l.join()