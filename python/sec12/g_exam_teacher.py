import mysql.connector
from mysql.connector import MySQLConnection

class LangDB:
    def __init__(self, user, password, database):
        self.con = MySQLConnection(user=user, password=password, database=database)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS lang(name VARCHAR(50), first_appeared INT)")

    def insert_data(self, data):
        formatted_data = [(d['name'], d['year']) for d in data]
        print(formatted_data, "======>") # [('C',1972),('Fortran',1957), ('Python', 1991), ('Go', 2009)] ===>
        self.cur.executemany("INSERT INTO lang(name, first_appeared) VALUES(%s, %s)", formatted_data)
        self.con.commit()

    def select_all(self):
        self.cur.execute("SELECT * FROM lang")
        return self.cur.fetchall()

    def update_data(self, name, year):
        self.cur.execute("UPDATE lang SET name = %s, first_appeared = %s WHERE name = 'C'", (name, year))
        self.con.commit()

    def __del__(self):
        self.con.close()

if __name__ == '__main__':
    db = LangDB('root', '0000', 'my_emp')

    data = [
        {"name": "C", "year": 1972},
        {"name": "Fortran", "year": 1957},
        {"name": "Python", "year": 1991},
        {"name": "Go", "year": 2009},
    ]

    db.insert_data(data)
    all_rows = db.select_all()
    for row in all_rows:
        print(row)

    db.update_data('Java', 2008)
    print('-------------')
    all_rows = db.select_all()
    for row in all_rows:
        print(row)

    del  db
