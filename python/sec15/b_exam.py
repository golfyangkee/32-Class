# 파이썬 사이트 가서 하나를 긁어가지고 오자.
"""
https://requests.readthedocs.io/en/latest/user/quickstart/
import requests
r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
r.status_code
->200
r.headers['content-type']
->'application/json; charset=utf8'
r.encoding
->'utf-8'
r.text
->'{"authenticated": true, ...'
r.json()
->{'authenticated': True, ...}
"""
import requests
from bs4 import BeautifulSoup

r = requests.get('https://python.org')
# print(r, type(r)) response [200] 이라고 뜨는데 이게 연결되었다는 뜻인가 보다.
# 접속할때 get 방식으로 가서 받아서 response임 r 자체가 response이고 바로 status_code로 연결된거다.
if r.status_code==200:
    print("연결됐어")

# 연결 확인 법 이것도 있음
if r.status_code == requests.codes.ok:
    print("연결됐어")

# .content = text
print(r.content)        # response 가 r 이니까 r.만 쳐도 response 객체의 메소드 나오고// 페이지 html 전체 리턴
print(type(r.content))


# .text = content
print(r.text)        # response 가 r 이니까 r.만 쳐도 response 객체의 메소드 나오고// 페이지 html 전체 리턴
print(type(r.text))

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())