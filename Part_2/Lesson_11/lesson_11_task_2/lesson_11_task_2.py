#  Пишем сканер: Задание 2 - 80 баллов
import socket
from functools import partial
from multiprocessing import Pool, Lock
from netaddr import IPRange


def input_data():
    try:
        ip_start, ip_end = input("Enter IP-IP: ").split("-")
    except (TypeError, ValueError) as e:
        print("Error", e)
    else:
        return IPRange(ip_start, ip_end)


def scanner(port_num, host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((host, port_num))
        lock.acquire()
        print(f"IP address {host} Port: {port_num} is open")
        lock.release()
    except socket.error:
        pass
    finally:
        s.close()


def init(l):
    global lock
    lock = l


if __name__ == "__main__":
    port_list = [43, 80, 109, 110, 115, 118, 119, 143, 194, 220, 443, 540,
                 585, 591, 1112, 1433, 1443, 3128, 3197, 3306, 3899, 4224,
                 4444, 5000, 5432, 6379, 8000, 8080, 10000]
    l = Lock()
    try:
        ip_range = input_data()
        for ip in ip_range:
            with Pool(20, initializer=init, initargs=(l, )) as pool:
                results = pool.map(partial(scanner, host=str(ip)), port_list)
    except Exception as e:
        print("Error", e)
