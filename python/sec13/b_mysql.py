import mysql.connector

## 메소드 단위 - 객체 지향은 메소드로 만들어서 클로즈 시키지 않는다.
def my_conn():
      config = {
        'user': 'root',
        'password': '0000',
        'host': '127.0.0.1',
        'database': 'my_emp',
        'raise_on_warnings': True
      }
      cnx = mysql.connector.connect(**config)
      print(cnx)
      return cnx
def  select_All(conn):
    cur  = conn.cursor()
    cur.execute("select  * from emp")  #return 없이 실행 되는 구문
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()

if __name__ == '__main__':
    # 연결 객체를 생성한 곳에서 소멸을 선언 및 구현한다.
    select_All(my_conn())
'''
마이콘에 객체를 입력해서 셋렉트얼에서 했으니까 소멸시켜야 한다. 소멸이 중요하다.
클로즈 시점을 찾기 힘드니까
연결된 커서 객체 가져다가 실행
'''