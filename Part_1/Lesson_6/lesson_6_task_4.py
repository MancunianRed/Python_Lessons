#  Функции: Задание 4 - 50 баллов
def words_list():
    words = []
    while len((word := input('Введите любое слово: '))) > 0:
        words.append(word)
    print(words)


words_list()
