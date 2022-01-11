#  Пишем конвертеры для полезных нагрузок: Задание 2 - 50 баллов
import base64
import urllib.parse
import codecs


def encode():
    try:
        text = input("Enter text: ")
        print(f"{'BASE64': <9} ==> "
              f"{str(base64.b64encode(text.encode('utf-8')), 'UTF-8')}")
        print(f"{'BASE32': <9} ==> "
              f"{str(base64.b32encode(text.encode('utf-8')), 'UTF-8')}")
        print(f"{'BASE16': <9} ==> "
              f"{str(base64.b16encode(text.encode('utf-8')), 'UTF-8')}")
        print(f"URLENCODE ==> {urllib.parse.quote(text)}")
        print(f"{'HEX': <9} ==> " + '\\' + '\\'.join(hex(ord(c))[1:] for c in text))
        print(f"{'ROT13': <9} ==> {codecs.encode(text, 'rot_13')}")
    except Exception as e:
        print("Error", e)


def decode():
    print("Select the desired format: BASE64, BASE32, BASE16, URLENCODE, HEX, "
          "ROT13")
    try:
        decode_format = input("Enter format: ")
        text = input("Enter text: ")
        if decode_format == "BASE64":
            print(f"BASE64 ==> "
                  f"{(base64.b64decode(bytes(text, 'UTF-8'))).decode('utf-8')}")
        elif decode_format == "BASE32":
            print(f"BASE32 ==> "
                  f"{(base64.b32decode(bytes(text, 'UTF-8'))).decode('utf-8')}")
        elif decode_format == "BASE16":
            print(f"BASE16 ==> "
                  f"{(base64.b16decode(bytes(text, 'UTF-8'))).decode('utf-8')}")
        elif decode_format == "URLENCODE":
            print(f"URLENCODE ==> {urllib.parse.unquote(text)}")
        elif decode_format == "HEX":
            print(f"HEX ==> "
                  f"{codecs.decode(bytes(text, 'utf-8'), 'unicode_escape')}")
        elif decode_format == "ROT13":
            print(f"ROT13 ==> {codecs.decode(text, 'rot_13')}")
    except Exception as e:
        print("Error", e)


if __name__ == "__main__":
    print("1 - encode\n2 - decode")
    try:
        action = int(input("Selected action: "))
    except Exception as e:
        print("Error", e)
    else:
        if action == 1:
            encode()
        else:
            decode()
