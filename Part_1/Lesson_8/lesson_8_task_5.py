#  Исключения: Задание 5 - 90 баллов
import string
import sys


def input_check():
    try:
        password = input('Введите пароль: ')
    except (ValueError, EOFError):
        return
    else:
        if password is None:
            print('Пароль не соответствует требованиям!')
            sys.exit()
        else:
            return password


def first_symbol_check(target_word):
    if not(target_word[0].isupper()):
        return False
    else:
        return True


def last_symbol_check(target_word):
    if target_word[-1] not in (string.ascii_letters + string.digits):
        return False
    else:
        return True


def len_pass_check(target_word):
    if len(target_word) not in range(8, 20):
        return False
    return True


def all_symbol_check(target_word):
    all_letters_string = string.ascii_letters + string.digits + '_'
    return all((letter in all_letters_string for letter in target_word))


def underscore_symbol_check(target_word):
    if len([s for s in target_word if s == '_']) == 0:
        return False
    return True


if __name__ == '__main__':
    password = input_check()
    def_list = [first_symbol_check(password), last_symbol_check(password),
                len_pass_check(password), all_symbol_check(password),
                underscore_symbol_check(password)]
    if all(def_list):
        print('Пароль принят!')
    else:
        print('Пароль не соответствует требованиям!')
