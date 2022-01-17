#  Пишем сканер: Задание 1 - 70 баллов
import socket
from multiprocessing import Process


def input_data():
    try:
        url = input("Enter url: ")
    except Exception as e:
        print("Error", e)
    else:
        return url


def scanner(url, host, port_num):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((host, port_num))
        print(port_num, end="\r")
        print(f"{url} Port: {port_num} is open")

    except socket.error:
        pass
    finally:
        s.close()


if __name__ == "__main__":
    url = input_data()
    host = socket.gethostbyname(url)
    my_list = []
    try:
        for port in range(65536):
            mult = Process(target=scanner, args=(url, host, port))
            my_list.append(mult)
            mult.start()
        for my_thread in my_list:
            my_thread.join()
    except PermissionError as e:
        print("Error", e)

