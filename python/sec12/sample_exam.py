# https://dev.mysql.com/doc/connector-python/en/connector-python-tutorial-cursorbuffered.html
# 버퍼 커서
# 특정 조건을 만족하는 직원들의 급여 정보를 업데이트하는 구문

from __future__ import print_function

from decimal import Decimal # 소수이하 자리수 프로시전 지정해주는 함수?
from datetime import datetime, date, timedelta  # 년 월일 시간 날짜 관리하는 프로시저

import mysql.connector

# Connect with the MySQL Server
cnx = mysql.connector.connect(user='root', password = '0000',database='employees')

# Get two buffered cursors
curA = cnx.cursor(buffered=True)    # 버퍼링 커서하는 역할: 모든 결과를 메모리에 저장한다. : 작은 데이터들을 다룰 때 사용
curB = cnx.cursor(buffered=True)

# Query to get employees who joined in a period defined by two dates
query = (
  "SELECT s.emp_no, salary, from_date, to_date FROM employees AS e "
  "LEFT JOIN salaries AS s USING (emp_no) "
  "WHERE to_date = DATE('9999-01-01')"
  "AND e.hire_date BETWEEN DATE(%s) AND DATE(%s)")
# 주어진 기간 내에 입사한 사원들의 정보를 리턴하겠다.
# 레프트 조인이니까 사원의 정보는 다 나오고 샐러리와 겹쳐지는 거만 나온다.
# 종속 관계는 실선으로 표현한다.

# UPDATE and INSERT statements for the old and new salary
update_old_salary = (
  "UPDATE salaries SET to_date = %s "
  "WHERE emp_no = %s AND from_date = %s")
# 기존 급여의 종료 날짜를 업데이트 하겠다.

insert_new_salary = (
  "INSERT INTO salaries (emp_no, from_date, to_date, salary) "
  "VALUES (%s, %s, %s, %s)")
# 새로운 급여 정보를 인서트 하겠다.

# Select the employees getting a raise
curA.execute(query, (date(2000, 1, 1), date(2000, 12, 31)))
# 업데이트 실행

# Iterate through the result of curA
for (emp_no, salary, from_date, to_date) in curA:
# 커서 객체로 리턴해서 업데이트 인서트 동시에 한다.

  # Update the old and insert the new salary
  new_salary = int(round(salary * Decimal('1.15')))
  tomorrow = date.today()+timedelta(days=1)
  curB.execute(update_old_salary, (tomorrow, emp_no, from_date)) # 종료 날짜 샐러리 업데이트 투모로우 없어서 앞단 코드 +1 했다.
  curB.execute(insert_new_salary,
               (emp_no, tomorrow, date(9999, 1, 1,), new_salary))

  # Commit the changes
  cnx.commit()

cnx.close()

'''
굳이 버퍼링을 하는 이유가 멀까?
버퍼링된 애들 실행 결과를 보면
a execute하고 다시 b에서 execute 하는데
버퍼가된 커서를 하는 이유는(장점)
하나의 커서에서 쿼리를 실행한 후 다른 커서로 다른 쿼리를 실행할 수 있다.
주의!!(단점)
버퍼링된 커서에서는 한 쿼리의 결과룰 모두 처리하기 전까지 다른 쿼리를 실행할 수 없다.
버퍼는 많은 양의 메모리를 차지해서 작은 데이터로 사용하기 유용해서 안 쓰는게 좋다
특정 조건에 따라 결과를 반복적으로 사용할 때 쓴다.
'''

'''
그러면 
1. 실행된 쿼리의 결과를 자동으로 전체가 메모리에 로드된다.
curA = cnx.cursor(buffered=True)
curB = cnx.cursor(buffered=True)
얘네들은 어떤 식으로 사용한 걸까?

두개 선언 시 얘네들은
실행 쿼리의 결과를 자동으로 전체가 메모리에 로드된다.

2. 전체 결과 집합을 로드 : 쿼리가 실행되자마자 결과가 [클라이언트 측의 메모리에 저장]된다. 결과가 크면 많은 메모리를 클라이언트 측에 저장 시킨다.
-> 서버 메모리 사용 감소, 임시 기억 장소 사용 감소 = 네트워크 트래픽 감소 (전송횟수가 줄어들어서 네트워크 트래픽 감소했다라고 한다.) 
= 서버 측 처리 간소화 (서버 부하 줄임) = 비용 감소
클라이언트가 소스 다 가져가버리니까 서버는 좋다? 이런 말인가?


3. 결과 집합 이란? : 밑ㅇ에 반복을 처리했는데 for (emp_no, salary, from_date, to_date) in curA:
커서 A가 반복을 하면서 결과 집합의 한 행을 메모리에서 직접 접근하면서 처리된다.

4. 동시 쿼리 싱행 (curA, curB) = 다중 커서의 독립적 운용
커서 A 커서 B 두개를 버퍼로 사용하고 있고 커서 A는 조건에 따른 반복으로 돌고 있고 그 안에 커서 B가 업데이트랑 인서트 하고 있다.
커서에이가 돌 때 커서비가 execute 2개 하고 있다.
동시 쿼리 실행 (curA, curB) 하나의 커서로 쿼리를 실행하고 있는 동안 다른 하나는 별도의 쿼리를 실행하고 있다.
curA:
  curB.execute(update_old_salary, (tomorrow, emp_no, from_date))
    curB.execute(insert_new_salary,
               (emp_no, tomorrow, date(9999, 1, 1,), new_salary))
그림에 대한 얘기를 해주자면
커서 A하나 커서 B 2개가 동시에 돌고 있다. B가 2개 동싱가 아니라 A 랑 B해서 동시 쿼리이다.

귀찮으면 일반 쿼리 실행해도 된다. - 트리거를 써서 개념이 좀 다르긴 하다.
많이 쓰고 있으니까 튜토리얼에 커서 진행 도와주고 있다.

적어진다.
버퍼링된 커서는 
서버는 이 결과를 저장하지 않는다.
그러면 여기를 쓰자 마자 메모리에 로드가 되면서 클라이언트

[질문] 그런데 트리거, 프로시저를 이용해서 서버가 자체적으로 수정하게 하는게 네트워크 트래픽 감소 아닌가요?
트리거랑 프로시저는 서버 측에서 처리하는 거다.
트리거랑 프로시저는 목적이 복접하거나 반복적인 데이터 사용할 때
1. 자주 사용하거나 복잡한 패턴을 사용할 때, 트리거, 프로시저를 해라
2. 서버 측에서 데이터 처리 로직을 실행 => 처리 속도가 빠르다.
3. 데이터 무결성이 원칙의 개념에서 네트워크 트래픽 감소이다.
 -> 프로시저랑 트리거가 네트워크 트래픽 감소가 맞으나
 상황에 따라 다르다. 모든 상황에서 처리 효율점의 이점은 트리거 프로시저가 답이다 라는 의미가 아니다.
 
버퍼는 클라이언트 측에서 처리하고 모듈 결과 집합이 작은 애들이 사용하는 거다.

[질문2] 버퍼 커서 두개를 이용하면 curA가 데이터를 계속 가져와야 하는거 아닌가요?
메모리에 보관이 되고 하나의 커리가 실행하는 동안 다른 커리가 실행이 된다. 라고 하고 동시 쿼리 라고 하니까
독립 동시 쿼리 실행이니까 다중 쿼서 독립적으로 운영하겠다는 의미

[질문3] 그러면 클라이언트가 데이터 처리를 하는 동안 서버는 아예 관여를 안 하는 거군요?
맞다. 쿼리 결과가 클라이언트로 가고 모든 처리가 클라이언트가 한다 추가적인 작업 안 한다.
일단은 쿼리 버퍼에이로 받아왔으니까 먼 일을 하던 서버는 안 한다.

-> 이쯤 문제는
클라이언트가 결과를 가져갔으니 서버는 관여 안한다는 건데
네트워크 트래픽이 감소한다는 거는 클라이언트랑 서버가 계속 소통할 필요가 없다.
주의 사항: 메모리 의존성이 강하다.
작은 얘들을 버퍼가 하는데
많은 결과 집합을 버퍼가 하면
클라이언트 용량이 작으면 문제가 된다.
시스템 메모리 부족해진다.
그래서 적절하게 클라이언트 사이즈를 체크하면서
버퍼를 구현하는 게 핵심이다.
큰 데이터는 사용 안하는게 원칙이다.
'''