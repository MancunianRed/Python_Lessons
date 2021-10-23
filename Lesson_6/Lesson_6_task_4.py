#  Функции: Задание 4 - 50 баллов
word = input('Введите слово: ')

compare_with_predator = lambda x: 'Это слово больше чем predator' if len(x) > \
                    len('predator') else 'Это слово меньше чем predator'

print(compare_with_predator(word))
