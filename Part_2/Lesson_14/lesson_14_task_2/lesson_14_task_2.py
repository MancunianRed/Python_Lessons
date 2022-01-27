#  Криптография: Задание 2 - 150 баллов
import string

s = "=Lryqna Ljnbja="
symbols = []
decrypt = ""
for i in range(26):
    for symbol in s:
        if symbol in string.ascii_letters:
            if symbol.isupper():
                decrypt += chr((ord(symbol) - i - 65) % 26 + 65)
            else:
                decrypt += chr((ord(symbol) - i - 97) % 26 + 97)
        else:
            decrypt += symbol
    print(f"Key +{i}: {decrypt}")
    decrypt = ""
