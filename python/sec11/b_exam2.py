## 우리 사용자 커스텀 패텀

import sqlite3
import datetime

def adapt_date(date_obj):   #Python 'datetime.date' 객체를 문자열로 변환
    return date_obj.strftime('%Y-%m-%d')    # 2024-01-02 각 부분을 년 월 일로 인식하겠다.

def convert_date(s):        # 문자열을 datetime.date 객체로 변환하겠다.
    return datetime.datetime.strptime(s.decode('utf-8'), '%Y-%m-%d').date()

# ver. 3.12 이상부터는 명시해주자. 오류는 안 나고 실행되었는데 deplecate?되어 있으니까
sqlite3.register_adapter(datetime.date, adapt_date) # python -> sqltype로 변할할 때 사용되는 함수
# 파이썬의 문자열을 가져다가 sql 문자열로 바꿔주는 것
sqlite3.register_converter('DATE', convert_date)    # sqltype -> python
                                                    # 리턴되는 문자열을 datetime.date 객체로 변환하는 패턴을 등록 파이썬으로 변환

'''
detect_types = sqlite3.PARSE_DECLTYPES : 테이블 생성 시 정의된 데이터 기반으로 converter 하겠다.
                                        m_date DATE ;                         
                sqlite3.PARSE_COLNAMES : 쿼리 결과의 열 이름에 명시된 데이터 타입을 기반으로 converter 하겠다.
                                        select my_clo as "my_clo [DATE]~"
사용자 함수를 정의할 때 주의할 점 : ISO 형식의 문자열을 변환하는 로직, 유닉스 타입 스탬프로 변환하는 형식으로 각 함수를 나눠서 선언 후 핸들링해라.
iso adapt 2개 convert 2개 필요?
'''

conn = sqlite3.connect('example.db', detect_types=sqlite3.PARSE_DECLTYPES) # detect_types=sqlite3.PARSE_DECLTYPES 이 친구 때문에 하고 있는 것
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS test (date_column DATE)")

# conn = sqlite3.connect('example.db')
# cur = conn.cursor()
# cur.execute("CREATE TABLE IF NOT EXISTS test (date_column DATE)")
# # class 타입과 여기 있는 타입이 다르니까 adapt 형식으로 인식하겠다. 그래서 db에 넣겠다.

today = datetime.date.today()
print(today, type(today)) # 2024-01-02 파이썬 꺼
cur.execute("INSERT INTO test (date_column) VALUES (?)", (today,))

# select 해보자
cur.execute("select * from test")

### 결과 출력
rows = cur.fetchall()  # rows는 리스트 니까
for row in rows:
    print(row[0], type(row[0]))

conn.close()
