#  Пишем брутфорсер: Задание 2 - 50 баллов

import mysql.connector as sql
import hashlib
mydb = sql.connect(host="localhost", user="", passwd="")


def mysql_data(data):
    login = data[0]
    passwd = data[1]
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    databases = mycursor.fetchall()
    flag = True
    for db in databases:
        if db[0] == "example":
            flag = False
            break
    if flag:
        mycursor.execute("create database example")
    mycursor.execute("use example")
    mycursor.execute("show tables")
    tables = mycursor.fetchall()
    flag = True
    for table in tables:
        if table[0] == "users":
            flag = False
            break
    if flag:
        mycursor.execute("CREATE TABLE users ( id INT NOT NULL AUTO_INCREMENT, "
                                              "login VARCHAR(100) NOT NULL,"
                                              "passwd VARCHAR(100) NOT NULL,"
                                              "PRIMARY KEY(id))")
    command = "INSERT INTO users (login, passwd) VALUES (%s, %s)"
    values = (login, passwd)
    mycursor.execute(command, values)
    mydb.commit()
    print("Thr database \'example\' is updated!")


def input_and_hash():
    login = input("Enter login: ")
    passw = input("Enter password: ")
    passw_hash = hashlib.sha1(passw.encode().strip()).hexdigest()
    return login, passw_hash


if __name__ == "__main__":
    mysql_data(input_and_hash())