#  Многопоточность: Задание 1 - 30 баллов
import os
import threading


def picture_open():
    os.chmod('/home/kali/PycharmProjects/lesson/nb.png', 0o777)
    os.system('xdg-open /home/kali/PycharmProjects/lesson/nb.png')


print('Привет Бро! Я занял первое место в конкурсе!')
thread = threading.Timer(5, picture_open)
thread.start()


