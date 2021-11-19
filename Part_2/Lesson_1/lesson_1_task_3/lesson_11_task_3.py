#  Аргументы: Задание 3 - 50 баллов
import argparse


class FileReader:
    value_list = list()

    def __init__(self, name):
        self.name = name
        self.count = 0

    def file_reader(self):
        with open("phonebook_al.txt", encoding="utf-8") as reader:
            for value in reader:
                if value.find(self.name) != -1:
                    FileReader.value_list.append(value)
                    self.count += 1
            print(f'Найдено {self.count} записей.')

    def value_print(self):
        for i in FileReader.value_list:
            list_1 = i.split()
            list_2 = list_1
            for j in range(len(list_1)):
                if list_1[j].find('@') != -1:
                    list_2.pop(j)
            print(' '.join(list_2).title())


class ArgsParse:
    def __init__(self):
        parser = argparse.ArgumentParser(description='parsing files')
        parser.add_argument('name', type=str, help='a key for '
                                                   'searching')
        self.args = parser.parse_args()

    def names(self):
        FileReader(self.args.name).file_reader()
        FileReader(self.args.name).value_print()


if __name__ == '__main__':
    ArgsParse().names()
