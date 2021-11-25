#  Модуль OS: Задание 2 - 30 баллов
import argparse


def calculator():
    codes = {0: '---', 1: '--x', 2: '-w-', 3: '-wx', 4: 'r--', 5: 'r-x',
             6: 'rw-', 7: 'rwx'}
    permit = []
    for i in list(agrs.a):
        permit.append(codes.get(int(i)))
    print(f'Калькулятор прав доступа:\n{agrs.a} this {"".join(permit)}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Permission calculator',
                                     usage='Python script')
    parser.add_argument('a', type=str, help='permission number')
    agrs = parser.parse_args()
    calculator()

# --------------version with click--------------------
# import click
#
# @click.command()
# @click.argument('a')
# def calculator(a):
#     codes = {0: '---', 1: '--x', 2: '-w-', 3: '-wx', 4: 'r--', 5: 'r-x',
#              6: 'rw-', 7: 'rwx'}
#     permit = []
#     for i in list(a):
#         permit.append(codes.get(int(i)))
#     click.echo(f'Калькулятор прав доступа:\n{a} this {"".join(permit)}')
#
#
# if __name__ == '__main__':
#     calculator()

