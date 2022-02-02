#  Пишем фреймворк: Задание 1 - 200 баллов
from dns import reversename, resolver


def dns_reverse():
    ip = input("Enter ip: ")
    try:
        rev_name = reversename.from_address(ip)
        reversed_dns = resolver.resolve(str(rev_name), "PTR")[0]
    except Exception as e:
        print("Error ==> ", e)
    else:
        print(reversed_dns)
