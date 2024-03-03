import sqlite3
import datetime
import my
# 주석하고 하면 오류나진 않지만... 뭔가 이상하다 그냥 0이 나오고 빨간게 있으면 기분이 안 좋으니까 ㅎㅎ 버전때문에 그런 듯
# 모듈 패턴을 my.py로 만들어줘야 사용할 수 있는 거 같다. adapt랑 convert 메소드 사용
# my의 resigter로 패턴 인식 함수로 진행 iso 타입으로 데이터베이스 진행

#connect () 데이터 베이스에 연결
# ":memory:" -> 특수 문자열 ,실제 데이터 베이스가 디스크의 실제 파일이 아닌 RAM에 생성 및 저장된다.
# detect_types -> 데이터 유형을 제어하는 처리 방법
# sqlite3.PARSE_DECLTYPES  : sqlite3 모듈이 create  table 문에서 선언된 유형을 기반으로  열의 데이터를 자동감지
#                                   create table test( )
# sqlite3.PARSE_COLNAMES  : 열의 유형을 자동감지  date  ,  timestamp
#                           date라고 선언하게되면 sqlite3의 date 타입으로 처리한다.
# date,timestamp 으로 선언을 하게 되면  python의 datetime모듈의  객체로 관리된다.

con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cur = con.cursor()
cur.execute("create table test(d date, ts timestamp)")

today = datetime.date.today()
now = datetime.datetime.now()

cur.execute("insert into test(d, ts) values (?, ?)", (today, now))
cur.execute("select d, ts from test")
row = cur.fetchone()
print(today, "=>", row[0], type(row[0]))
print(now, "=>", row[1], type(row[1]))

# cur.execute('select current_date as "d [date]", current_timestamp as "ts [timestamp]"')
# row = cur.fetchone()
# print("current_date", row[0], type(row[0]))
# print("current_timestamp", row[1], type(row[1]))

con.close()