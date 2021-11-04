#  Исключения: Задание 5 - 90 баллов
import string


def input_check():
    try:
        password = input('Введите пароль: ')
    except (ValueError, EOFError):
        return
    else:
        return password


def password_check(a):
    letdig = string.ascii_letters + string.digits
    if a is not None and a[0].isupper() and a[-1] in letdig and \
            (8 <= len(a) <= 20) and len([s for s in a if s == '_']) > 0:
        for index, value in enumerate(a, 1):
            if value in letdig or value == '_':
                if index == len(a):
                    print('Пароль принят!')
                continue
            else:
                print('Пароль не соответствует требованиям!')
                break
    else:
        print('Пароль не соответствует требованиям!')


if __name__ == '__main__':
    password_check(input_check())