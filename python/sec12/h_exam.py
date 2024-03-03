import sqlite3
from dataclasses import dataclass

@dataclass
class Lang:  # 생성자, 소멸자, 연산자 재정의, __repr__
    name : str
    first_appeared: int

class LangDB:
    def __init__(self):     # ------ 1. 생성자 호출  
        self.con = sqlite3.connect(":memory:")  # 스키마 생성
        self.cur = self.con.execute("CREATE TABLE lang(name text, first_appeared integer)") # 테이블 생성

    def insert_data(self, data):    # ---- 2. 데이터 추가 data = data 변수가 아니라 클래스 객체이다.
        # if res = data 하면 넘어오는 데이터는

        self.cur.executemany("INSERT INTO lang VALUES(%s,%s)",[(lang.name , lang.first_appeared) for lang in  data])
        self.con.commit()

    # def insert_data(selfself, res : Lang) : # --- 2. 데이터 추가 res =data 하면 아래처럼 해야한다.
    #     self.cur.executemany("INSERT INTO lang VALUES(?,?)",
    #                          [(lang.name , lang.first_appeared) for lang in  res])
    #     self.con.commit()
    def select_all(self):
        self.cur.execute("SELECT * FROM lang")
        result =[Lang(*row)   for  row  in   self.cur.fetchall()]
        return result

    # def update_data(self, name, year):
    #     #year = int(year)
    #     self.cur.execute("UPDATE lang SET name = ?, first_appeared = ?  WHERE name = 'C'", (name, year))
    #     self.con.commit()

    def update_data(self, res : Lang):
        #year = int(year)
        self.cur.execute("UPDATE lang SET name = %s, first_appeared = %s  WHERE name = 'C'",
                         (res.name, res.first_appeared))
        self.con.commit()


    def __del__(self):  #소멸자 추가
        self.con.close()

if __name__ == '__main__':
    # class Lang: 이라서 g_db는 일반코드인데 h는 데이터 lang로 한 코드이다.
    data = [
        Lang("C", 1972),    # 현재 클래스로 받으니까
        Lang(name= "Fortran", first_appeared=1957),
        Lang(name="Python", first_appeared=1991),
        Lang(name="Go", first_appeared=2009),
    ]

    # print(data) # 클래스로 리턴된다.
    # print(data[0])  # 클래스로 리턴된다.
    print('-------------')
    lang_db = LangDB()      # Lang 테이블의 데이터를 CRUD하는 클래스 -> 생성자 호출   ---- 1
    
    lang_db.insert_data(data)   # 데이터 추가 ---- 2.
    
    all_rows = lang_db.select_all()
    for row in all_rows:
        print(row)

    # lang_db.update_data('Java', 2008)

    update_val = Lang('Java', 2008)
    lang_db.update_data(update_val)
    print('-------------')
    all_rows = lang_db.select_all()
    for row in all_rows:
        print(row)


