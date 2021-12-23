#  Работа с сетью: Задание 3 - 100 баллов
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(("localhost", 2323))
    s.sendto("".encode(), ("", 2323))
    print("Соединение установлено.")
    while True:
        message = input("Клиент UDP: ")
        data = s.sendto(message.encode(), ("", 2323))
        if message == "exit":
            break
        mes, adr = s.recvfrom(1024)
        print("Сервер UDP: ", mes.decode())
except Exception as e:
    print("Error: ", e)
finally:
    sys.exit()

