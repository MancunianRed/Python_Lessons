#  Работа с базой данных MySQL: Задание 2 - 100 баллов
import mysql
import mysql.connector as sql


class SqlCommands:
    def __init__(self, mycursor):
        self.mycursor = mycursor
        self.check_input()
        mydb.close()

    def check_input(self):
        while (command := input('Enter SQL > ')) != 'exit':
            try:
                self.mycursor.execute(command)
            except mysql.connector.Error as err:
                print(err)
                break
            else:
                self.print_output()
        if command == 'exit':
            print('Work with the database is complete')

    def print_output(self):
        for db in self.mycursor:
            for index, value in enumerate(db):
                if index != len(db) - 1:
                    print(f'{value},', end=' ')
                else:
                    print(value)


if __name__ == '__main__':
    mydb = sql.connect(host='localhost', user='root', passwd='')
    mycursor = mydb.cursor()
    SqlCommands(mycursor)
