import mysql.connector as db


class DBHelper:

    def __init__(self):
        self.connection = db.connect(user='root', password='jatin12345',
                                     host='127.0.0.1',
                                     database='gw2022pd1')
        print("1.DB CONNECTED ")
        self.cursor = self.connection.cursor()
        print("2.CURSOR CREATED ")

    def write(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()
        print("SQL QUERY EXECUTED ")

    def read(self, sql):
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows
