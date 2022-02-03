#  Пишем фреймворк: Задание 1 - 200 баллов
import Part_2.Lesson_16.lesson_16_task_1.full_scripts.host_ip as add
import Part_2.Lesson_16.lesson_16_task_1.full_scripts.site_location as location
import Part_2.Lesson_16.lesson_16_task_1.full_scripts.whois as whois
import Part_2.Lesson_16.lesson_16_task_1.full_scripts.nslookup as ns
import Part_2.Lesson_16.lesson_16_task_1.full_scripts.mx_record as mx
import Part_2.Lesson_16.lesson_16_task_1.full_scripts.reverse_dns as reverse
import Part_2.Lesson_16.lesson_16_task_1.full_scripts.robots_txt as robots
import Part_2.Lesson_16.lesson_16_task_1.full_scripts.sitemap_xml as sitemap
import Part_2.Lesson_16.lesson_16_task_1.full_scripts.reverse_ip as reverseip
import Part_2.Lesson_16.lesson_16_task_1.full_scripts.input_text_check as in_text
import colorama
from colorama import Fore
colorama.init(autoreset=True)

logo = Fore.RED + r"""
  ___  ____ ___ _   _ _____   ____   _____  __
 / _ \/ ___|_ _| \ | |_   _| | __ ) / _ \ \/ /
| | | \___ \| ||  \| | | |   |  _ \| | | \  / 
| |_| |___) | || |\  | | |   | |_) | |_| /  \ 
 \___/|____/___|_| \_| |_|   |____/ \___/_/\_\
""" + Fore.RESET


options_list = {
                0: ("0. Exit the program", exit),
                1: ("1. Host IP", add.get_ip),
                2: ("2. Site location", location.get_city),
                3: ("3. Whois", whois.who_is),
                4: ("4. Nslookup", ns.ns_lookup),
                5: ("5. DNS MX-Record", mx.mx_record),
                6: ("6. Reverse DNS", reverse.dns_reverse),
                7: ("7. robots.txt", robots.request_robots_data),
                8: ("8. sitemap.xml", sitemap.get_sitemap_data),
                9: ("9. Reverse IP Lookup", reverseip.reverse_ip)
                }


if __name__ == "__main__":
    print(logo)
    for value in options_list.values():
        print(Fore.MAGENTA + value[0] + Fore.RESET)
    try:
        while (
        num := int(in_text.input_text("\nEnter the option number: "))) != 0:
            print("-" * 35, options_list[num][0], "-" * 35, sep="\n")
            options_list[num][1]()
    except Exception as e:
        print(f"{Fore.RED} ==>> Error: {e}{Fore.RESET}")
    print("\nThe program is complete")