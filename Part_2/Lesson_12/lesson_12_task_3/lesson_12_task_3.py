#  Пишем брутфорсер: Задание 3 - 50 баллов
import mysql.connector as sql
import hashlib

mydb = sql.connect(host="localhost", user="", passwd="")
mycursor =mydb.cursor()
mycursor.execute("use example")


def input_data():
    login = input("Enter login: ")
    if check_login(login):
        password = input("Enter password: ")
        if check_passwd(password):
            print("Access is open!")
        else:
            print("Access is denied!")
    else:
        print("Access is denied!")


def check_login(login):
    mycursor.execute(f"select * from users where login like '{login}'")
    if len(mycursor.fetchall()) > 0:
        return True


def check_passwd(password):
    passw_hash = hashlib.sha1(password.encode()).hexdigest()
    mycursor.execute(f"select * from users where passwd like '{passw_hash}'")
    if mycursor.fetchone() is not None:
        return True


if __name__ == "__main__":
    input_data()
    mydb.close()

