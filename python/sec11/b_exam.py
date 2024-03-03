import sqlite3
import datetime

def adapt_date(date_obj):
    return date_obj

def convert_date(s):
    return datetime.datetime.strptime(s.decode('utf-8'), '%Y-%m-%d').date()

sqlite3.register_converter('DATE', convert_date)    # 패턴 모듈 등록

conn = sqlite3.connect('example.db', detect_types=sqlite3.PARSE_DECLTYPES)

