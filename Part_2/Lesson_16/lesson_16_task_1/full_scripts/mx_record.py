#  Пишем фреймворк: Задание 1 - 200 баллов
import dns.resolver


def mx_record():
    address = input("Enter host: ")
    try:
        my_resolver = dns.resolver.Resolver(configure=False)
        my_resolver.nameservers = ["8.8.8.8", "1.1.1.1"]
        answers = my_resolver.resolve(address, "MX")
    except Exception as e:
        print("Error ==> ", e)
    else:
        for rdata in answers:
            print("MX record:", rdata.exchange)


