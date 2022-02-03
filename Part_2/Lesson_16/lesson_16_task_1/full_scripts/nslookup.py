#  Пишем фреймворк: Задание 1 - 200 баллов
from nslookup import Nslookup
import Part_2.Lesson_16.lesson_16_task_1.full_scripts.input_text_check as in_text
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def ns_lookup():
    domain = in_text.input_text("Enter host: ")
    try:
        dns_query = Nslookup(dns_servers=["1.1.1.1"])
        ips_record = dns_query.dns_lookup(domain)
        soa_record = dns_query.soa_lookup(domain)
    except Exception as e:
        print(f"{Fore.RED}==> Error: {e}{Fore.RESET}")
    else:
        for i in ips_record.response_full:
            print(i)
        for i in soa_record.response_full:
            print("\n".join(i.split(". ")))



