import mysql.connector
from dataclasses import dataclass

@dataclass
class Lang:
    name: str
    first_appeared: int

class LangDB:
    def __init__(self, user, password, database):
        self.con = mysql.connector.connect(
            user=user,
            password=password,
            database=database
        )
        self.cur = self.con.cursor()
        self.cur.execute("DROP TABLE IF EXISTS lang")
        self.cur.execute("CREATE TABLE lang(name VARCHAR(50), first_appeared INT)")

    def insert_data(self, data):
        formatted_data = [(lang.name, lang.first_appeared) for lang in data]
        self.cur.executemany("INSERT INTO lang(name, first_appeared) VALUES(%s, %s)", formatted_data)
        self.con.commit()

    def select_all(self):
        self.cur.execute("SELECT * FROM lang")
        result = [Lang(*row) for row in self.cur.fetchall()]
        return result

    def update_data(self, res: Lang):
        self.cur.execute(
            "UPDATE lang SET name = %s, first_appeared = %s WHERE name = 'C'",
            (res.name, res.first_appeared)
        )
        self.con.commit()

    def __del__(self):
        self.con.close()

if __name__ == '__main__':
    db = LangDB('root', '0000', 'my_emp')
    data = [
        Lang("C", 1972),
        Lang(name="Fortran", first_appeared=1957),
        Lang(name="Python", first_appeared=1991),
        Lang(name="Go", first_appeared=2009),
    ]

    db.insert_data(data)
    all_rows = db.select_all()
    for row in all_rows:
        print(row)

    update_val = Lang('Java', 2008)
    db.update_data(update_val)
    print('-------------')
    all_rows = db.select_all()
    for row in all_rows:
        print(row)
