#  Аргументы: Задание 5 - 80 баллов
import itertools
import random
import string
import time
import click


class FileWriter:
    def __init__(self, length_comb):
        self.length_comb = int(length_comb)

    def file_writer(self):
        with open(f'num_dict{self.length_comb}.txt', 'w', encoding='utf-8') \
                as writer:
            list_1 = [int(x) for x in string.digits]
            random.shuffle(list_1)
            pincode_vars = itertools.product(list_1, repeat=self.length_comb)
            print(f'Start process...\nКоличество комбинаций: '
                  f'{10**self.length_comb}')
            start_time = time.time()
            for var in pincode_vars:
                writer.write(''.join(str(x) for x in var) + '\n')
            print(f'Completed in: {time.time() - start_time: .2f} sec.')


@click.command()
@click.argument('length_comb')
def parse(length_comb):
    FileWriter(length_comb).file_writer()


if __name__ == '__main__':
    parse()




