#  Пишем фреймворк: Задание 1 - 200 баллов
import requests
import socket
from dns import reversename, resolver


def reverse_dns(ip):
    try:
        rev_name = reversename.from_address(ip)
        reversed_dns = resolver.resolve(str(rev_name), "PTR")[0]
    except Exception as e:
        print("Error ==> ", e)
    else:
        return reversed_dns


def reverse_ip():
    api = "http://api.hackertarget.com/reverseiplookup/"
    var = input("Enter IP or Domain: ")
    ip = socket.gethostbyname(var)
    ip_dict = {"q": ip}
    pwn = requests.request("GET", api, params=ip_dict)
    print(f"Found domain hosted on the same web server as "
          f"{str(reverse_dns(ip)).rstrip('.')} ({ip})")
    print(pwn.text)

