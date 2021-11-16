#  Классы и ООП часть 2: Задание 5 - 100 баллов
import datetime


class Hello:
    print("Hello")


def my_decorator(function_to_decorate):
    def wrap():
        function_to_decorate()
        current_date = datetime.datetime.now()
        current_date_string = current_date.strftime('%d-%m-%y %H:%M:%S')
        print(current_date_string)
    return wrap


if __name__ == '__main':
    new_function = my_decorator(Hello)
    new_function()

