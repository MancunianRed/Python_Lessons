#  Аргументы: Задание 4 - 100 баллов
import argparse
import itertools
import random
import string
import time


class FileWriter:
    def __init__(self, len_c):
        self.len_c = int(len_c)

    def file_writer(self):
        with open(f'num_dict{self.len_c}.txt', 'w', encoding='utf-8') as writer:
            list_1 = [int(x) for x in string.digits]
            random.shuffle(list_1)
            pincode_vars = itertools.product(list_1, repeat=self.len_c)
            print(f'Start process...\nКоличество комбинаций: {10**self.len_c}')
            start_time = time.time()
            for var in pincode_vars:
                writer.write(''.join(str(x) for x in var) + '\n')
            print(f'Completed in: {time.time() - start_time: .2f} sec.')


class ArgParse:
    def __init__(self):
        parser = argparse.ArgumentParser(description='parsing files')
        parser.add_argument('len', type=str, help='length of combination')
        self.args = parser.parse_args()

    def list_combinations(self):
        FileWriter(self.args.len).file_writer()


if __name__ == '__main__':
    ArgParse().list_combinations()
