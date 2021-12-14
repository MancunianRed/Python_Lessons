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


def race(time_to):
    if threading.current_thread().getName() == "MAZDA":
        print(f'Автомобиль {threading.current_thread().getName()} стартовал!')
        time.sleep(time_to)
    elif threading.current_thread().getName() == "HONDA":
        print(f'Автомобиль {threading.current_thread().getName()} стартовал!')
        time.sleep(time_to)
    else:
        print(f'Автомобиль {threading.current_thread().getName()} стартовал!')
        time.sleep(time_to)
    results()




vehicles = {"MAZDA": 15, "HONDA": 18, "TOYOTA": 19}
start = time.time()
mazda = threading.Thread(target=race, name="MAZDA", kwargs={"time_to": 15})
honda = threading.Thread(target=race, name="HONDA", kwargs={"time_to": 18})
toyota = threading.Thread(target=race, name="TOYOTA", kwargs={"time_to": 19})
mazda.start()
honda.start()
toyota.start()


