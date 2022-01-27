#  Криптография: Задание 1 - 50 баллов
import string

def input_messages():
    value = input("Select action: ")
    message = input("Enter a message: ").upper()
    if value == "1":
        encode(message)
    else:
        decode(message)


def encode(message):
    encode_word = ""
    alphabet = [chr(x) for x in range(1040, 1072)]
    alpha = list(alphabet)
    alpha.reverse()
    for symbol in message:
        for index, value in enumerate(alphabet):
            if symbol == value:
                encode_word += alpha[index]
    print(f"Encrypted message: {encode_word}")


def decode(message):
    decode_word = ""
    alphabet = [chr(x) for x in range(1040, 1072)]
    alpha = list(alphabet)
    alpha.reverse()
    for symbol in message:
        for index, value in enumerate(alpha):
            if symbol == value:
                decode_word += alphabet[index]
    print(f"Decrypted message: {decode_word}")


if __name__ == "__main__":
    input_messages()