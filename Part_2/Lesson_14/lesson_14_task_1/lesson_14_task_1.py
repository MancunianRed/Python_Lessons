#  Криптография: Задание 1 - 50 баллов


def input_messages():
    value = input("Select action: ")
    message = input("Enter a message: ").upper()
    if value == "1":
        print(f"Encrypted message: {encrypt_decrypt(message)}")
    elif value == "2":
        print(f"Decrypted message: {encrypt_decrypt(message)}")


def encrypt_decrypt(message):
    alphabet = "".join([chr(x) for x in range(1040, 1072)])
    return message.translate(str.maketrans(alphabet, alphabet[::-1]))


if __name__ == "__main__":
    input_messages()