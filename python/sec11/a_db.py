import sqlite3  #sqlite3  CRUD

'''
231229 오후영상 3시 40분쯤??
https://docs.python.org/3/library/sqlite3.html#sqlite3.connect
연결
명령 수행  select (커서 한 줄 이상의) - execute가 한다.,
    insert, delete, update - fetchone, fetmany, fetchall ??로 받아야 하는게 다르다.
결과 리턴
닫기
'''


#1.연결   db 생성
conn  = sqlite3.connect("employee.db")
#2. 커서 생성
cursor   = conn.cursor()
#3. 테이블 생성    employees    id (pk, auto)  정수  , name  문자열  nn, age 정수 nn, city 문자열  nn
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id    INTEGER PRIMARY KEY AUTOINCREMENT,        
        name  TEXT NOT NULL,        
        age   INTEGER NOT NULL,        
        city  TEXT NOT NULL
       )    
""")

# 예를 들면
# 다 만들어 놔야 호출을 할 수 있지
# 메소드 인데 실제는
# insert_emp = "insert into employees ( name, age,city) values ( ?,?,?)"
# 이렇게 쿼리문만 상수값으로 만들어 놓는다.
# 이래야 수정하기가 편하다.

#4.  insert_t, select, delete_t, update_t
def  insert_employees(name, age, city):
    cursor.execute('insert into employees ( name, age,city) values ( ?,?,?)',(name,age,city) )
    conn.commit()
def  selectall_employees():
    cursor.execute('select   * from  employees' )    # 한줄 이상
    return cursor.fetchall()    # select 결과 리턴하겠다. -> list형태로 리턴하겠다.
'''
fetchone은 turple
나머지는 list 형태로 리턴
'''

def update_employees(id, name, age, city):
    # 해당 id로 찾아서 name, age, city로 변경하겠다. 순서에 맞게끔 진행하자! 입력은 id가 먼저지만 실행은 id가 뒤다. 파라미터 대입 시 괄호로 묶어서 대입
    cursor.execute('UPDATE employees SET name=?, age=?, city=? WHERE id=?', (name, age, city, id))
    conn.commit()
def  delete_employees(id):
    cursor.execute('DELETE FROM employees WHERE id=?', (id,))
    conn.commit()

#5. 실행 결과
#########insert

# insert_employees('홍길동1', 21, '서울1')
# insert_employees('홍길동2', 22, '서울2')
# insert_employees('홍길동3', 23, '서울3')

# print(selectall_employees())

# 수정 : 번호로  이름 , 나이 , 주소 변경해보자.
#     1번 친구를   정길동   35  인천 으로 변경해 보자.
# update_employees(1 ,'정길동', 35, '인천')
# print(selectall_employees())

delete_employees(1)
print(selectall_employees())

#6. conn. close()
conn.close()

