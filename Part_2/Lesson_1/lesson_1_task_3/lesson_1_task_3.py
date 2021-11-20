#  Аргументы: Задание 3 - 50 баллов
import argparse


class FileReader:
    def __init__(self, name):
        self.name = name
        self.value_list = list()

    def file_reader(self):
        with open("phonebook_al.txt", encoding="utf-8") as reader:
            for value in reader:
                if self.name in value:
                    self.value_list.append(' '.join(value.rsplit()))
            print(f'Найдено {len(self.value_list)} записей.')
            return self.value_list

    def value_print(self):
        for i in self.file_reader():
            if '@' in i:
                print(' '.join(i.title().split()[:-1]))
            else:
                print(''.join(i.title()))


parser = argparse.ArgumentParser(description='parsing files')
parser.add_argument('name', type=str, help='a key for searching')
args = parser.parse_args()


def names():
    FileReader(args.name).value_print()


if __name__ == '__main__':
    names()
