#  Работа с сетью: Задание 1 - 50 баллов
import socket

server_s = socket.socket()
print("Жду подключения...")
server_s.bind(("0.0.0.0", 4444))
server_s.listen(1)
conn, addr = server_s.accept()
print("Соединение установлено: ", addr)
client_mes = conn.recv(1024).decode()
print("Клиент: " + client_mes)
print("Соединение закрыто")
conn.close()
