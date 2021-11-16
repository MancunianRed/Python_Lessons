#  Классы и ООП часть 2: Задание 5 - 100 баллов


def my_decorator(function_to_decorate):
    import datetime

    def wrap(*args):
        function_to_decorate(*args)
        print(datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S'))
        # current_date = datetime.datetime.now()
        # current_date_string = current_date.strftime('%d-%m-%y %H:%M:%S')
        # print(current_date_string)
    return wrap


@my_decorator
class Hello:
    def __init__(self, a):
        self.a = a
        print(self.a)


if __name__ == '__main__':
    Hello('Hello')

