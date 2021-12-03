#  Регулярные выражения: Задание 4 - 100 баллов
import re


class PasswdCheck:
    def __init__(self):
        self.pass_check()

    def pass_check(self):
        try:
            password = input('Введите пароль: ')
        except (ValueError, EOFError):
            print('Пароль не соответствует требованиям!')
        else:
            if (re.match(r'(?=.*_)(?=.*[A-Z])(?=.*[a-z])(?=.*\d)^[A-Z].{6,'
                         '18}[a-z0-9]$', password)) is not None:
                print('Пароль принят!')
            else:
                print('Пароль не соответствует требованиям!')


if __name__ == '__main__':
    PasswdCheck()


