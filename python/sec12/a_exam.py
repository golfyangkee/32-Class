# https://dev.mysql.com/doc/connector-python/en/connector-python-option-files.html

from __future__ import print_function

from decimal import Decimal
from datetime import datetime, date, timedelta
import mysql.connector
from mysql.connector import MySQLConnection

# Connect with the MySQL Server
# cnx = mysql.connector.connect(user='root', password = '0000', database='employees')
# print(type(cnx))
cnx = MySQLConnection(user='root', password = '0000', database='employees')

if cnx.is_connected():
    print("연결했어")

print(cnx,type(cnx))
print(cnx.get_server_info())
print(cnx.get_server_version())

cur = cnx.cursor(buffered=True)
# cur.execute("SHOW STATUS LIKE 'Ssl_cipher'")
cur.execute("select * from my_emp.emp")
res=cur.fetchall()
for i in res:
    print(i)
cur.close()
cnx.close()