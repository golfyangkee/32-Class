import sqlite3
con = sqlite3.connect(":memory:")
cur = con.execute("CREATE TABLE lang(name, first_appeared)")
# 선언시 데이터 타입이 없는데 처음 들어오는 게 바로 데이터 타입으로 인식한다.
def insert_data(data):
    cur.executemany("INSERT INTO lang VALUES(:name, :year)", data)
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

    cur.execute("UPDATE lang SET name = ?, first_appeared = ?  WHERE name = 'C'" , (name,year))
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

    update_data('Java',2008);  #name c를 찾아서  각각 변경을 해본다. 추가이다. 수정아니다.
    print('-------------')
    all = select_all()
    for row in all:
        print(row)
