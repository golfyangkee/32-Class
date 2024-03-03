from mysql.connector import MySQLConnection

con = MySQLConnection(user='root', password = '0000', database='my_emp')
cur=con.cursor()
cur.execute("Drop table IF EXISTS lang")
cur.execute("CREATE TABLE lang(name varchar(20), first_appeared int)")
# 선언시 데이터 타입이 없는데 처음 들어오는 게 바로 데이터 타입으로 인식한다.
def insert_data(data):
    # https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-executemany.html
    # 딕셔너리 데이터를 튜플로 변환했다.
    formatted_data = [(d['name'], d['year']) for d in data]
    cur.executemany("INSERT INTO lang VALUES (%s, %s)", formatted_data)
    con.commit();

def select_all():
    cur.execute("SELECT * FROM lang")
    result = cur.fetchall()
    return result

def update_data(name, year):    # 컬럼도 추가하고 데이터를 수정(추가) 했다. modify 아니다.
    # cur.execute("ALTER TABLE lang ADD COLUMN year INTEGER")
    # year = int(year)
    # cur.execute("UPDATE lang SET name = ?, year = ?  WHERE name = 'C'" , (name,year))
    # con.commit()

    cur.execute("UPDATE lang SET name = %s, first_appeared = %s  WHERE name = 'C'" , (name,year))
    con.commit()

if __name__ == '__main__':
    data = [{"name": "C", "year": 1972},
            {"name": "Fortran", "year": 1957},
            {"name": "Python", "year": 1991},
            {"name": "Go", "year": 2009},
            ]
    insert_data(data)
    all= select_all()
    for  row in all :
        # print(row)
        print( f'{row[0]:<10} \t {row[1] :<15}' )

    # 데이터 업데이트
    update_data('ssan',1991)
    print('-----------')
    all = select_all()
    for row in all:
        print(row)