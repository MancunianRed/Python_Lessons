#  Работа с сетью: Задание 2 - 80 баллов
from ftplib import FTP
import re
import socket


def ip_address_writer(hosts, filename):
    with open(filename, "w", encoding="utf-8") as writer:
        for host_name in hosts:
            writer.write(socket.gethostbyname(host_name) + "\n")


def ftp_storage(filename):
    ftp = FTP("localhost")
    ftp.login("ftpuser", "123")
    ftp.cwd("files")
    with open(filename, "rb") as fp:
        ftp.storlines("STOR ip_address.txt", fp)
    ftp.close()


if __name__ == "__main__":
    host = ["https://www.hackthebox.eu/", "https://hack.me/",
         "http://www.gameofhacks.com/", "http://www.itsecgames.com/"]
    upd_host = re.findall(r"(\w+\.[a-z]+)(?=/)", ' '.join(host))
    filename = "/home/kali/Desktop/ip_address.txt"
    ip_address_writer(upd_host, filename)
    ftp_storage(filename)
