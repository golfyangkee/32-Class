'''  json 타입의 문자열을   파이썬 모듈로  인코딩, 디코딩   -> mysql  '''
# https://dev.mysql.com/doc/refman/8.0/en/json.html#json-values
# json 설명
# Merging arrays.
'''
Merging arrays.  
In contexts that combine multiple arrays, the arrays are merged into a single array. 
JSON_MERGE_PRESERVE() does this by concatenating arrays named later to the end of the first array. 
JSON_MERGE_PATCH() considers each argument as an array consisting of a single element (thus having 0 as its index) 
and then applies “last duplicate key wins” logic to select only the last argument. 
You can compare the results shown by this query:
'''
# 겹치는 키가 있는 경우 마지막 배열로 덮어쓰겠다. 없는 경우는 마지막 배열로 리턴하겠다.

import mysql.connector   # 테이블 생성, insert, select
import json
def db_connect():   # DB 연결
    config = {
        'user': 'root',
        'password': '0000',
        'host': '127.0.0.1',
        'database': 'my_emp'
    }
    return mysql.connector.connect(**config)

def  create_table():
    cnx = db_connect()
    cursor=cnx.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            data JSON NOT NULL
        )
    """)
    cursor.close()
    cnx.close()

def insert():
    cnx = db_connect()
    cursor=cnx.cursor()
    ########2. 입력할 데이터를  {} 선언하고 insert
    data = {
        "STUDENT": [
            {"NAME": "Dominica", "SCORE": {"KOR": 10, "ENG": 20, "MATH": 30}},
            {"NAME": "Dominico", "SCORE": {"KOR": 90, "ENG": 40, "MATH": 100}},
            {"NAME": "RuRe", "SCORE": {"KOR": 90, "ENG": 90, "MATH": 90}}
        ]
    }
    print(json.dumps(data))
    cursor.execute("INSERT INTO students (data) VALUES (%s)", (json.dumps(data),)) # 문자열로 들어갈거다.
    cnx.commit()
    cursor.close()
    cnx.close()

#### 3. 테이블 생성 및 데이터를 mysql에서 확인
def select():
    cnx = db_connect()
    cursor=cnx.cursor()
    ##### 4.전체 출력 및 json_type json.loads(row[0]) 로 결과를 추출
    cursor.execute("SELECT data FROM students")
    rows = cursor.fetchall()
    for row in rows:
        #print(json.loads(row[0]))  #전체 출력
        json_data =json.loads(row[0]) #이름만 출력
        print(type(json_data))
        students  =json_data.get("STUDENT",[])
        for  student in students:
            name = student.get("NAME")
            print(name)
    cursor.close()
    cnx.close()

def select_name():
    cnx = db_connect()
    cursor=cnx.cursor()
    ####5. mysql query로 name을 추출하고 싶다.
    query  = "SELECT  data -> '$.STUDENT[*].NAME'    FROM   students"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        names  = row[0]
        print(names)
    cnx.commit()
    cursor.close()
    cnx.close()

###6. 점수의 합을 구하고 싶다.
def select_sum_scores():
    cnx = db_connect()
    cursor=cnx.cursor()

    query = "SELECT  data -> '$.STUDENT[*].SCORE'    FROM   students"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        scores_json = row[0]
        scores_list = json.loads(scores_json)  # []로 리턴한다
        for scores_dict in scores_list:
            sum_score = sum(scores_dict.values())
            print(f"Sum of scores: {sum_score}")
    cursor.close()
    cnx.close()

def select_all():
    cnx = db_connect()
    cursor=cnx.cursor()
    select_all = "SELECT * FROM students"
    cursor.execute(select_all)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    cnx.close()

if __name__ == '__main__':
    # create_table()
    # insert()
    # select()
    select_all()
