#  Функции: Задание 3 - 30 баллов
word = input('Введите слово: ')

compare = lambda x: 'Это слово больше чем predator' if len(x) > \
                    len('predator') else 'Это слово меньше чем predator'

print(compare(word))
