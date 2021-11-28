#  Работа с базой данных MySQL: Задание 3 - 150 баллов
import mysql.connector as sql


class BaseFirst:
    def __init__(self, mycursor):
        self.mycursor = mycursor
        self.delete()
        self.update()
        self.insert()
        self.create()
        self.print()

    def delete(self):
        self.mycursor.execute('DELETE FROM product WHERE id=2')
        db.commit()

    def update(self):
        self.mycursor.execute('UPDATE product SET price="63 руб" '
                              'WHERE name="молоко"')
        self.mycursor.execute('UPDATE product SET price="34 руб" '
                              'WHERE name="макароны"')
        db.commit()

    def insert(self):
        self.mycursor.execute('INSERT INTO product (name, price) '
                              'VALUES ("мука ржаная", "54 руб")')
        db.commit()

    def create(self):
        self.mycursor.execute('ALTER TABLE product ADD COLUMN note '
                              'VARCHAR(100) NULL AFTER price')
        db.commit()

    def print(self):
        self.mycursor.execute('SELECT * FROM product')
        for data in self.mycursor:
            print(''.join(str(data).strip('()')))


if __name__ == '__main__':
    db = sql.connect(host='localhost', database='first', user='root', passwd='')
    mycursor = db.cursor()
    BaseFirst(mycursor)
    db.close()
