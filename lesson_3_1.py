#  Типы данных - list: Задание 1 - 20 баллов
import string

main_list = ['True', 'False', 'pop', 'remove', 'del']

print(main_list)

#  Типы данных - list: Задание 2 - 25 баллов
computer_language = ['JavaScript', 'Java', 'Python', 'C#', 'PHP', 'C++']
computer_language.append('Objective-C')
print("\n".join(computer_language))

#  Типы данных - list: Задание 3 - 30 баллов
word = 'the best and good'
print(word.split(' and '))

#  Типы данных - list: Задание 4 - 50 баллов
adress = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
adress.append(adress[0]+adress[1]+adress[6])
adress.extend(adress[-2]*2+adress[0])
del adress[:-4]
print('.'.join(adress))

#  Типы данных - list: Задание 5 - 70 баллов
simple = 'promo'
new_list = []
new_list.extend(simple + 'tion')
print(new_list)

#  Типы данных - list: Задание 6 - 80 баллов
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbol = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
new_list = [number[-1]*2, number[0]+symbol[-3], number[-3]+symbol[2], number[
    1]+number[5], symbol[0]+number[0], symbol[2]+number[-3]]
print(':'.join(new_list))

#  Типы данных - list: Задание 7 - 120 баллов
slice_string = ['pgekjsgqlafrimzixwuiavukxdqifadmbdqvszcqizimkifcajycqijwuwwa'
                'wmbbiiigevfrualbsgijbvskfskwczlbervxkmsgtxrfxswmxsibffvaqrab'
                'gwxwcqzcrjiedsizjauufrfdiguzjxhcwlgjiduemddufkewasjfgavsrujg'
                'bisagzswdaeebwerdcluoqvgajabbelaadswzdebwgxvdfaugqjazlwvzejd'
                'gleszsrlqxnsrkbkqcvgwekwsqezll']

print(slice_string[0][::50])


string = 'pgekjsgqlafrimzixwuiavukxdqifadmbdqvszcqizimkifcajycqijwuwwawmbbiiige' \
         'vfrualbsgijbvskfskwczlbervxkmsgtxrfxswmxsibffvaqrabgwxwcqzcrjiedsizja' \
         'uufrfdiguzjxhcwlgjiduemddufkewasjfgavsrujgbisagzswdaeebwerdcluoqvgaja' \
         'bbelaadswzdebwgxvdfaugqjazlwvzejdgleszsrlqxnsrkbkqcvgwekwsqezll'

letter_index = string.index('p')
letter_index1 = string.index('y')

print(letter_index, string[letter_index] + string[string.index('y')])

address = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
zero = address[address.index('0')]
print(address[address.index('3'):address.index('7')])
del address[address.index('3'):address.index('7')]
del address[address.index('8'):]
print(zero)

print(''.join(address), zero, zero, address[address.index('1')], sep='.')
