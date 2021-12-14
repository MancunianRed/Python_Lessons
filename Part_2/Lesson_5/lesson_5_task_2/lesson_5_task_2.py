#  Многопоточность: Задание 2 - 50 баллов
import threading

x = 500000


def increment():
    global x
    for _ in range(500000):
        x = x + 1


def decrement():
    global x
    for _ in range(300000):
        x = x - 1


def one_thread():
    lock.acquire()
    if threading.current_thread().getName() == 'A':
        increment()
    else:
        decrement()
    lock.release()


def start_threads():
    global x
    x = 500000
    thread_1 = threading.Thread(target=one_thread, name='A')
    thread_2 = threading.Thread(target=one_thread, name='B')
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()


if __name__ == "__main__":
    lock = threading.Lock()
    for i in range(10):
        start_threads()
        print(f'Iteration {i + 1:2d}: x = {x}')
    print("Done!")

