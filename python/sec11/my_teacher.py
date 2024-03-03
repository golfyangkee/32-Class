# https://docs.python.org/3/library/sqlite3.html?highlight=sqlite3#sqlite3-tutorial
import datetime
import sqlite3
#  ####################### python  -> sqlite3
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

# ##################### sqlite3->[문자열]->python  datetime객체로
def convert_date (val):
    """Convert ISO 8601 date to datetime.date object."""
    return datetime.date.fromisoformat(val.decode())

def convert_datetime (val):
    """Convert ISO 8601 datetime to datetime.datetime object."""
    return datetime.datetime.fromisoformat(val.decode())

def convert_timestamp (val):
    """Convert Unix epoch timestamp to datetime.datetime object."""
    if isinstance(val, bytes):
        val = val.decode('utf-8')
    try:
        return datetime.datetime.fromtimestamp(int(val))  # 유닉스 타임스탬프  (정수)
    except ValueError:
        return datetime.datetime.strptime(val, '%Y-%m-%d %H:%M:%S')   # 정수가 아닌 날짜 /시간


# 데이타 타입의 형식을 선언하는 함수를 핸들링   : detect_types=sqlite3.PARSE_DECLTYPES 로  패턴인식 함수를 찾는다.
sqlite3.register_converter("date", convert_date)
sqlite3.register_converter("datetime", convert_datetime)
sqlite3.register_converter("timestamp", convert_timestamp)

