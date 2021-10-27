#  Модули и пакеты: Задание 3 - 40 баллов

text = input('Введите текст: ')
str1 = "qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?"
str2 = "йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ."
translation = str.maketrans(str1, str2)
ru_text = text.translate(translation)
print(ru_text)



