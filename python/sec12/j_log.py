# https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html
from sec12.my_log import connect_to_mysql

config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "0000",
    "database": "my_emp",
}

cnx = connect_to_mysql(config, attempts=3)

if cnx and cnx.is_connected():

    with cnx.cursor() as cursor:

        result = cursor.execute("SELECT * FROM emp LIMIT 5")

        rows = cursor.fetchall()

        for rows in rows:

            print(rows)

    cnx.close()     # 생성 순의 역순으로 클로즈

else:

    print("Could not connect")