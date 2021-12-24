#  Работа с сетью: Задание 3 - 50 баллов
import requests
from ftplib import FTP


def uri_download(uri, filename):
    res = requests.get(uri, stream=True)
    with open(filename, "wb") as writer:
        for i in res.iter_content(chunk_size=64000):
            writer.write(i)


def ftp_writer(filename):
    ftp = FTP("localhost")
    ftp.login("ftpuser", "123")
    with open(filename, "rb") as ftp_writer:
        ftp.storbinary("STOR winner.jpg", ftp_writer)


if __name__ == "__main__":
    uri = "https://i.ytimg.com/vi/VKErEwtJ-Nw/maxresdefault.jpg"
    filename = "winner.jpg"
    uri_download(uri, filename)
    ftp_writer(filename)
    print("Файл скачан и загружен на FTP-сервер")