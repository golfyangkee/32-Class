# https://docs.python.org/3/library/sqlite3.html#tutorial
# tutorial 복붙해서 변환한거다.

import sqlite3
con=sqlite3.connect('abc.db')  # insert, delete, update -> commit(), rollback()
print(type(con))  # 연결하면 끝났다. -> 커서 생김
cur = con.cursor()  # 명령을 실행하겠다.
#cur.execute("CREATE TABLE movie(title, year, score)")
insert_sql = 'insert into movie values (1,1,1)'
cur.execute(insert_sql)
con.commit()
res = cur.execute("SELECT * FROM movie")
print(res.fetchone())
con.close()

