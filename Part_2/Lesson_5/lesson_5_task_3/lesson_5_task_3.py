#  Многопоточность: Задание 3 - 150 баллов
import colorama
from colorama import Fore
import threading
import time
colorama.init(autoreset=True)


def results():
    print(f'\nКоличество активных авто {threading.active_count() - 1}')
    print(f'Автомобиль {Fore.GREEN} {threading.current_thread().getName()}'
          f'{Fore.RESET} завершил гонку')
    print(f'{Fore.LIGHTMAGENTA_EX}Доехал до финиша за {time.time() - start}'
          f'{Fore.RESET}')


def race(**vehicles):
    print(f'Автомобиль {threading.current_thread().getName()} стартовал!')
    time.sleep(vehicles.get(threading.current_thread().getName()))
    results()


if __name__ == "__main__":
    vehicles = {"MAZDA": 15, "HONDA": 18, "TOYOTA": 19}
    racing_list = []
    start = time.time()
    for name in vehicles.keys():
        car = threading.Thread(target=race, name=name, kwargs=vehicles)
        racing_list.append(car)
        car.start()
    for car in racing_list:
        car.join()


