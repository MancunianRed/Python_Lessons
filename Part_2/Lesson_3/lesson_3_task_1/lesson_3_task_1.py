#  Работа с базой данных MySQL: Задание 1 - 40 баллов
import mysql.connector as sql

mydb = sql.connect(
    database='mysql',
    host="localhost",
    user="root",
    passwd="")

mycursor = mydb.cursor()
mycursor.execute('CREATE DATABASE first')
mydb.close()

mydb = sql.connect(
    database='first',
    host="localhost",
    user="root",
    passwd="")

mycursor = mydb.cursor()
mycursor.execute('CREATE TABLE product (id INT AUTO_INCREMENT PRIMARY KEY, '
                 'name VARCHAR(100), price VARCHAR(100))')
ins_tab = 'INSERT INTO product (name, price) VALUES (%s, %s)'
val = [('батон нарезной', '21 руб'), ('масло подсолнечное', '60 руб'),
       ('крупа гречневая', '80 руб'), ('молоко', '54 руб'),
       ('яйцо куриное', '55 руб'), ('кетчуп', '75 руб'),
       ('сок томатный', '92 руб'), ('макароны', '30 руб'),
       ('бзеленый горошек', '45 руб'), ('селедка', '150 руб')]
mycursor.executemany(ins_tab, val)
mydb.commit()
print('The database \'first\' was created!')
mydb.close()
