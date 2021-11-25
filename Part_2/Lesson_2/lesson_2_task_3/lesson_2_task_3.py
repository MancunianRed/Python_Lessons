#  Модуль OS: Задание 3 - 150 баллов
import os
import argparse
import stat


class SystemManagement:
    def __init__(self, arguments):
        self.args = arguments
        if self.args.system is None and self.args.chmod is None \
                and self.args.tree is None:
            parser.print_help()
        elif self.args.system == 'system':
            self.system()
        elif self.args.chmod == 'chmod':
            self.chmod()
        elif self.args.tree == 'tree':
            self.tree()

    def system(self):
        while (command := input('Shell command: ')) != 'exit':
            if os.system(command) == 0:
                pass
            else:
                print('Wrong command, exit!')
                break
        if command == 'exit':
            print('The work was completed!')

    def chmod(self):
        while (command := input('Enter the path: ')) != 'exit':
            if os.path.exists(command):
                print(oct(stat.S_IMODE(os.lstat(command).st_mode))[2:])
            else:
                print('The file or directory does not exist!')
        if command == 'exit':
            print('The work was completed!')

    def tree(self):
        while (command := input('Enter the path: ')) != 'exit':
            if os.path.exists(command):
                os.system('tree ' + command)
                os.system('tree ' + command + ' -o '
                          + f'wood_{command.split("/")[-1]}.txt')
            else:
                print('The file or directory does not exist!')
        if command == 'exit':
            print('The work was completed!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='System management program',
                                     usage='Script option:')
    parser.add_argument('-s', '--system', help='System command')
    parser.add_argument('-c', '--chmod', help='Checking access rights')
    parser.add_argument('-t', '--tree', help='Directory tree')
    args = parser.parse_args()

    SystemManagement(args)



