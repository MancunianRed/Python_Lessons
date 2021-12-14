#  test
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


if __name__=="__main__":
    vehicles = {"MAZDA": 15, "HONDA": 18, "TOYOTA": 19}
    racing_list = {"MAZDA": 15, "HONDA": 18, "TOYOTA": 19}
    start = time.time()
    for
    mazda = threading.Thread(target=race, name="MAZDA", kwargs=vehicles)
    honda = threading.Thread(target=race, name="HONDA", kwargs=vehicles)
    toyota = threading.Thread(target=race, name="TOYOTA", kwargs=vehicles)
    mazda.start()
    honda.start()
    toyota.start()
    mazda.join()
    honda.join()
    toyota.join()


