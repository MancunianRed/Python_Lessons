#  Условные операторы: Задание 1 - 20 баллов
num_1, num_2, num_3 = int(input('Введите число: ')), \
                      int(input('Введите число: ')), \
                      int(input('Введите число: '))
if num_1 > 100 and num_2 > 100 and num_3 > 100:
    print('"Все числа больше 100')
else:
    print('"Не все числа больше 100')


#  Условные операторы: Задание 2 - 25 баллов
num = int(input('Введите число: '))
if 1 <= num <= 100:
    if 1 <= num <= 6:
        print('Детство это прекрасно )')
    elif 7 <= num <= 17:
        print('Учиться, учиться, учиться...')
    elif 18 <= num <= 64:
        print('Теперь ты можешь делать всё что угодно!')
    elif 65 <= num <= 100:
        print('Заслуженный отдых')
else:
    print('Введите число от 1 до 100')


#  Условные операторы: Задание 3 - 25 баллов
if set(word_1 := input('Введите первое слово: ')) == set(word_2 := input(
        'Введите второе слово: ')):
    print('Слова', word_1, 'и', word_2, 'состоят из одних и тех же букв.')
else:
    print('Введенные слова содержат разный набор букв')


#  Условные операторы: Задание 4 - 70 баллов
if (len_1 := int(len(input('Введите строку: ')))) <= 100:
    if (len_1 == 1) or (int(str(len_1)[-1]) == 1):
        print('В строке', len_1, 'символ')
    elif (2 <= len_1 <= 4) or (2 <= int(str(len_1)[-1]) <= 4):
        print('В строке', len_1, 'символa')
    else:
        print('В строке', len_1, 'символов')
else:
    print('Количество символов не должно быть больше 100!')


#  Условные операторы: Задание 5 - 90 баллов
hours = int(input('Введите часы: '))
minutes = int(input('Введите минуты: '))
seconds = int(input('Введите секунды: '))

if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
    if hours <= 9:
        print('0' + str(hours) + ':', end='')
    else:
        print(str(hours) + ':', end='')
    if minutes <= 9:
        print('0' + str(minutes) + ':', end='')
    else:
        print(str(minutes) + ':', end='')
    if seconds <= 9:
        print('0' + str(seconds))
    else:
        print(str(seconds))
else:
    print('Введите числа для часов от 0 до 23, и для минут и секунд от 0 до 59')


#  Условные операторы: Задание 6 - 100 баллов
month_tuple = 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', \
              'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
if 1 <= (data := int(input('Введите число от 1 до 12: '))) <= 12:
    if 1 <= data <= 2 or data == 12:
        print('Зима,', month_tuple[data-1])
    elif 3 <= data <= 5:
        print('Весна,', month_tuple[data - 1])
    elif 3 <= data <= 5:
        print('Лето,', month_tuple[data - 1])
    elif 6 <= data <= 8:
        print('Лето,', month_tuple[data - 1])
    else:
        print('Осень,', month_tuple[data - 1])
else:
    print('Введите число от 1 до 12')


#  Условные операторы: Задание 7 - 200 баллов
time = input('Введите время: ')
if (hours := time[:2]) == '00':
    hours_1 = 0
else:
    hours_1 = int(hours.lstrip('0'))
if (minutes := time[3:]) == '00':
    minutes_1 = 0
else:
    minutes_1 = int(minutes.lstrip('0'))
if hours_1 < 6 or (hours_1 == 18 and minutes_1 > 0) or hours_1 > 18:
    print('Солнце за горизантом!')
else:
    if minutes_1 == 0:
        print('Угол солнца ', (hours_1 - 6) * 15, 'градусов')
    else:
        print('Угол солнца ', (hours_1 - 6) * 15 + minutes_1 * 0.25, 'градусов')

