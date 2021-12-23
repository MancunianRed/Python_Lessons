#  Работа с сетью: Задание 3 - 100 баллов
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 2323))
print("Жду сообщение...")
try:
    mess, adrr = s.recvfrom(1024)
    print("соединение установлено: ", adrr)
    while True:
        mes, adr = s.recvfrom(1024)
        print("Клиент UDP: ", mes.decode())
        if mes.decode() == "exit":
            break
        s.sendto(input("Сервер UDP: ").encode(), ("", adr[1]))
    print("Соединение закрыто.")
except Exception as e:
    print("Error: ", e)
finally:
    s.close()
