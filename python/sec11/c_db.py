import sqlite3
con = sqlite3.connect(":memory:")
# cur = con.cursor() # 커서 생성하고 커서가 가지고 있는 execute해도 된다.
# cur.execute("CREATE TABLE lang(name, first_appeared)") 해도 된다.
cur = con.execute("CREATE TABLE lang(name, first_appeared)")

data = (   {"name": "C", "year": 1972},
           {"name": "Fortran", "year": 1957},
           {"name": "Python", "year": 1991},
           {"name": "Go", "year": 2009},
        )
cur.executemany("INSERT INTO lang VALUES(:name, :year)", data) # 이거는 변수명으로 호출
# 정확하게 딕셔너리의 키 값이 일치 해야 한다.

params = (1972,)
cur.execute("SELECT * FROM lang WHERE first_appeared = ?", params) # 위치로 리턴 물음표는 순서로 맵핑해서 호출
print(cur.fetchall())
con.close()
