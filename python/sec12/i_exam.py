import sqlite3
from dataclasses import dataclass

@dataclass
class Lang:
    name: str
    year: int

def adapt_lang(lang):
    return (lang.name, lang.year)
def convert_lang(value):    # 값을 전달 받아
    return Lang(*value)     # tuple 객체로 전달

###################################################################################
con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)     # 명시 패턴을 찾겠다.
sqlite3.register_adapter(Lang, adapt_lang)
sqlite3.register_converter("lang", convert_lang)

cur = con.cursor()
cur.execute("CREATE TABLE lang(name TEXT, year INTEGER)")
###################################################################################



def insert_data(cur, data):
    # adapt_lang 는 Lang 객체가 데이터 베이스에 삽입될 때 호출되어 Lang 객체를 튜플로 변환한다.
    for lang in data:
        cur.execute("INSERT INTO lang(name, year) VALUES (?, ?)", (lang.name, lang.year))
    con.commit()
def select_all(cur):
    # convert_lang 는 데이터베이스에서 데이터를 조회할 때 호출되어 튜플 데이터를 Lang 객체로 변환한다.
    cur.execute("SELECT * FROM lang")
    result = cur.fetchall()
    return [Lang(name=row[0], year=row[1]) for row in result]

if __name__ == '__main__':
    data = [
        Lang(name="C", year=1972),
        Lang(name="Fortran", year=1957),
        Lang(name="Python", year=1991),
        Lang(name="Go", year=2009),
    ]
    insert_data(cur, data)
    all_rows = select_all(cur)
    for row in all_rows:
        print(f'{row.name:<10} {row.year:<10}')
