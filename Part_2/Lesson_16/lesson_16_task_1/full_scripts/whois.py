#  Пишем фреймворк: Задание 1 - 200 баллов
import whois

def who_is():
    add = input("Enter domain: ")
    try:
        domain = whois.query(add)
    except Exception as e:
        print("Error ==> ", e)
    else:
        res = domain.__dict__
        for i in res:
            print(f"{i}: {res[i]}")
