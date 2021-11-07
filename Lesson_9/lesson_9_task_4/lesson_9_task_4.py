#  Работа с файлами: Задание 4 - 50 баллов


def write_encode_string_to_file(file_name, string):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(string.decode('utf-8'))
    except:
        print('File error')


def read_decode_string_from_file(file_name):
    try:
        with open(file_name, encoding='utf-8') as file:
            contain = file.read()
            print(contain)
    except:
        print('File error')


if __name__ == '__main__':
    code_str = b'\xd0\x9f\xd1\x80\xd0\xb0\xd0\xb2\xd0\xb8\xd0\xbb\xd1\x8c\xd0\xbd' \
               b'\xd0\xbe\xd0\xb9 ' \
               b'\xd0\xb4\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb3\xd0\xbe\xd0\xb9 ' \
               b'\xd0\xb8\xd0\xb4\xd1\x91\xd1\x82\xd0\xb5 \xd1\x82\xd0\xbe\xd0\xb2' \
               b'\xd0\xb0\xd1\x80\xd0\xb8\xd1\x89\xd0\xb8!\n'
    write_encode_string_to_file('decode.txt', code_str)
    read_decode_string_from_file('decode.txt')
