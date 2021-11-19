#  Классы и ООП: Задание 1 - 25 баллов


class NewFormat:
    """
    Программа считает количество символов без учёта пробелов
        """
    new_str = input('Введите предложение: ')

    def without_space(self, a):
        if len(a.replace(' ', '')) % 10 == 1 and len(a.replace(' ',
                                                               '')) != \
                11:
            end_sum = ''
        elif len(a.replace(' ', '')) % 10 in (2, 3, 4) and \
                len(a.replace(' ', '')) not in (12, 13, 14):
            end_sum = 'а'
        else:
            end_sum = 'ов'
        print('В предложении ', len(a.replace(' ', '')), ' символ' + end_sum)


if __name__ == '__main__':
    space = NewFormat()
    space.without_space(NewFormat.new_str)
