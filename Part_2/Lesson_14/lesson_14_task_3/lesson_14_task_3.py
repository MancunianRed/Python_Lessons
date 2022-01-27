#  Криптография: Задание 3 - 100 баллов
import string


def input_messages():
    message = list(input("Enter a message: "))
    crypt(message)


def crypt(message):
    alphabet = string.ascii_letters + " "
    keys = {x: chr(y) for x, y in zip(alphabet, range(20000, 20000+len(alphabet)))}
    for symbol in range(len(message)):
        for key in keys:
            if message[symbol] == key:
                message[symbol] = keys[key]
            elif message[symbol] == keys[key]:
                message[symbol] = key
            else:
                pass
    print(f"Encrypted/decrypted message: {''.join(message)}")


if __name__ == "__main__":
    input_messages()



