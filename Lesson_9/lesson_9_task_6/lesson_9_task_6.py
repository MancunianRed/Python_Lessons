#  Работа с файлами: Задание 6 - 150 баллов

try:
    with open('surnames.txt', encoding='utf-8') as file, \
            open('woman.txt', 'a', encoding='utf-8') as file_woman, \
            open('man.txt', 'a', encoding='utf-8') as file_man:
        for surnames in file:
            if surnames.strip().endswith(('ВА', 'НА', 'АЯ')):
                file_woman.write(surnames.strip().title() + '\n')
            else:
                file_man.write(surnames.strip().title() + '\n')
except:
    print('Ошибка при работе с файлом')
else:
    print('Done')
