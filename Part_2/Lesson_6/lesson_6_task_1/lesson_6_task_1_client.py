#  Работа с сетью: Задание 1 - 50 баллов
import socket

client_s = socket.socket()
client_s.connect(("127.0.0.1", 4444))
print("Соединение установлено!")
mes = "Мудрым пользуйся девизом - будь готов к любым сюрпризам"
client_s.send(mes.encode())
client_s.close()

