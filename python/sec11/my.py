# https://docs.python.org/3/library/sqlite3.html?highlight=sqlite3#sqlite3-tutorial
# 메이커 쪽 패턴 iso 포맷 패턴

import datetime
import sqlite3
################################### python -> sqlite3
def adapt_date_iso(val):
    """Adapt datetime.date to ISO 8601 date."""
    return val.isoformat()

def adapt_datetime_iso(val):
    """Adapt datetime.datetime to timezone-naive ISO 8601 date."""
    return val.isoformat()

def adapt_datetime_epoch(val):
    """Adapt datetime.datetime to Unix timestamp."""
    return int(val.timestamp())

sqlite3.register_adapter(datetime.date, adapt_date_iso)
sqlite3.register_adapter(datetime.datetime, adapt_datetime_iso)
sqlite3.register_adapter(datetime.datetime, adapt_datetime_epoch)


############################## sqlite3 -> [문자열] -> python 데이트타입의 객체로 변환할 때 쓰는 것
def convert_date(val):
    """Convert ISO 8601 date to datetime.date object."""
    return datetime.date.fromisoformat(val.decode())

def convert_datetime(val):
    """Convert ISO 8601 datetime to datetime.datetime object.""" # 버전마다 다르니 찾아보자.
    return datetime.datetime.fromisoformat(val.decode())

def convert_timestamp(val):
    """Convert Unix epoch timestamp to datetime.datetime object."""
    return datetime.datetime.fromtimestamp(int(val))
    # 인트값을 주면 사용하겠다. DECODE로 해서 맞췄다.
    # 그래서 여기 부분을 수정해야 하는데 멀 어쩌라는 거지..?
    if isinstance(val, bytes):
        val = val.decode('utf-8')
    try:
        return datetime.datetime.fromtimestamp(int(val))    # 유닉스 타임스탬프 (정수)
    except ValueError:
        return datetime.datetime.strptime(val, '%Y-%m-%d %H:%M:%S') # 정수가 아닌 날짜 | 시간으로 맞추고 싶을 때

# 데이터 타입의 형식을 선언하는 함수를 핸들링 :  detect_types=sqlite3.PARSE_DECLTYPES 로 패턴인식 함수를 찾는다.
# 각각 꺼내와서 진행하겠다.
# sqlite3.PARSE_DECLTYPES 이거 호출하면 resiter_converter 호출? 명시 호출?
sqlite3.register_converter("date", convert_date)
sqlite3.register_converter("datetime", convert_datetime)
sqlite3.register_converter("timestamp", convert_timestamp)