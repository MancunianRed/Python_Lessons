#  Форматирование: Задание 3 - 50 баллов


def file_read():
    with open('symbol.txt', encoding='utf-8') as reader:
        content = reader.read()
    return content


def file_format(content):
    count = 0
    for _ in range(int(len(content) / 8)):
        # print('{0:,>9}'.format(content[count]) + content[count+1:count+7] +
        #       '{0:.<9}'.format(content[count+7]))
        print(f'{content[count]:,>9}' + content[count+1:count+7] +
              f'{content[count+7]:,<9}')
        count = count + 8


if __name__=='__main__':
    file_format(file_read())