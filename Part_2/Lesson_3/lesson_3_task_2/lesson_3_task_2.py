#  Работа с базой данных MySQL: Задание 2 - 100 баллов
import mysql
import mysql.connector as sql

mydb = sql.connect(
    host='localhost',
    user='root',
    passwd=''
)

mycursor = mydb.cursor()
while (command := input('Enter SQL > ')) != 'exit':
    try:
        mycursor.execute(command)
    except mysql.connector.Error as err:
        print(err)
        break
    else:
        for db in mycursor:
            for index, value in enumerate(db):
                if index != len(db) - 1:
                    print(f'{value},', end=' ')
                else:
                    print(value)
print('Work with the database is complete')
mydb.close()
