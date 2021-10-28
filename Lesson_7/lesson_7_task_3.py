#  Модули и пакеты: Задание 3 - 40 баллов

# text = input('Введите текст: ')
# str1 = "qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?"
# str2 = "йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ."
# translation = str.maketrans(str1, str2)
# ru_text = text.translate(translation)
# print(ru_text)

sentence = input('Введите текст: ')
print()
eng_ru_dict = {'q': 'й', 'w': 'ц', 'e': 'у', 'r':'к', 't':'е', 'y':'н', 'u':'г',
               'i': 'ш', 'o': 'щ', 'p': 'з', '[':'х', ']':'ъ', 'a':'ф', 's':'ы',
               'd': 'в', 'f': 'а', 'g': 'п', 'h':'р', 'j':'о', 'k':'л', 'l':'д',
               ';': 'ж', '\'': 'э', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м',
               'b': 'и', 'n': 'т', 'm': 'ь', ',':'б', '.':'ю', '/':'.', '{':'Х',
               '}': 'Ъ', ':': 'Ж', '"': 'Э', '<':'Б', '>':'Ю', '?':',', 'Q':'Й',
               'W': 'Ц', 'E': 'У', 'R': 'К', 'T':'Е', 'Y':'Н', 'U':'Г', 'I':'Ш',
               'O': 'Щ', 'P': 'З', 'A': 'Ф', 'S':'Ы', 'D':'В', 'F':'А', 'G':'П',
               'H': 'Р', 'J': 'О', 'K': 'Л', 'L':'Д', 'Z':'Я', 'X':'Ч', 'C':'С',
               'V': 'М', 'B': 'И', 'N': 'Т', 'M': 'Ь'}


def translate_en_ru(text):
    res = ''
    for i in text:
        if i in eng_ru_dict:
            res += eng_ru_dict[i]
        else:
            res += i
    return res


print(translate_en_ru(sentence))
