#  Пишем фреймворк: Задание 1 - 200 баллов
from nslookup import Nslookup


def ns_lookup():
    domain = input("Enter host: ")
    try:
        dns_query = Nslookup(dns_servers=["1.1.1.1"])
        ips_record = dns_query.dns_lookup(domain)
        soa_record = dns_query.soa_lookup(domain)
    except Exception as e:
        print("Error ==> ", e)
    else:
        for i in ips_record.response_full:
            print(i)
        for i in soa_record.response_full:
            print("\n".join(i.split(". ")))



