#  Многопоточность: Задание 4 - 100 баллов
import multiprocessing
from multiprocessing import Queue
from multiprocessing import Process, Lock


def action(q1, q, i, amount):
    q1.put(i)
    print(f"Курсант {i+1} начал снаряжать магазин")
    for bullets in range(amount):
        print(bullets+1, end=" ")
        q.get()
    print()
    print(f"Курсант {i+1} снарядил магазин\n")


if __name__ == "__main__":
    q1 = Queue()
    q = Queue()
    for n in range(150):
        q.put(n)
    my_process = []
    print("очередь в начале", q.qsize())
    for i in range(5):
        if q.qsize() >= 30:
            p = Process(target=action, args=(q1, q, i, 30))
            my_process.append(p)
            p.start()
            q1.get()
        else:
            p = Process(target=action, args=(q1, q, i, q.qsize()))
            my_process.append(p)
            p.start()
            q1.get()

    for l in my_process:
        l.join()
    print("очередь в конце", q.qsize())