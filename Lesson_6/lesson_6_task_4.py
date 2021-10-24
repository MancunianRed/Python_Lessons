#  Функции: Задание 4 - 50 баллов
def words_list(a):
    words = []
    while len(a) > 0:
        words.append(a)
        a = input('Введите любое слово: ')
    print(words)


words_list(input('Введите любое слово: '))
