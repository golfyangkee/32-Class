import sqlite3
import datetime

def adapt_date(date_obj):   #Python  'datetime.date' 객체를 문자열로 변환
    return date_obj.strftime('%Y-%m-%d')   # 2024-01-02
def convert_date(s):        #문자열을 datetime.date객체로 변환
    return datetime.datetime.strptime(s.decode('utf-8'), '%Y-%m-%d').date()


sqlite3.register_adapter(datetime.date, adapt_date)  #python -> saltype로 변환 할 때  사용되는 함수
sqlite3.register_converter('DATE', convert_date)    # sqltype-> python
                                                     # 리턴되는 문자열을 datetime.date 객체로 변환하는 패턴을 등록

conn = sqlite3.connect('example.db', detect_types=sqlite3.PARSE_DECLTYPES)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS test (date_column DATE)")

today = datetime.date.today()
#print(today , type(today))  # 2024-01-02
cur.execute("INSERT INTO test (date_column) VALUES (?)", (today,))
cur.execute( "select  * from test")
###결과 출력
rows  = cur.fetchall()
for row  in rows:
    print( row[0] , type (row[0]))
conn.close()

