#  Форматирование: Задание 6 - 140 баллов
import calendar
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def calendar_file_writer():
    with open('calendar.txt', 'w') as writer:
        writer.write(calendar_format.formatyear(2020))


def calendar_color_format():
    with open('calendar.txt') as reader:
        for index, content in enumerate(reader, 1):
            if index == 1:
                print(Fore.GREEN + content.replace('\n', ''))
            elif index == 3 or index == 12 or index == 20 or index == 29:
                print(Fore.GREEN + content.replace('\n', ''))
            elif index == 4 or index == 13 or index == 21 or index == 30:
                print(content.replace('\n', '').
                      replace('Sa Su', f'{Fore.RED}Sa Su{Fore.RESET}'))
            else:
                print(content.replace('\n', ''))


if __name__ == '__main__':
    calendar_format = calendar.LocaleTextCalendar(locale='en_US')
    calendar_color_format()

