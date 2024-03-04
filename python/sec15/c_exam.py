import requests
from bs4 import BeautifulSoup
# https://requests.readthedocs.io/en/latest/user/quickstart/

r = requests.get('https://python.org')  # 1. 페이지 요청
r2 = requests.request('GET','https://python.org') # 메소드는 항상 대문자여야 한다.
#  GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE.

soup = BeautifulSoup(r.content, 'html.parser')  # 2. 요청된 전체 문서를 객체로 리턴

print(r.headers)
'''
>>> r.headers
{
    'content-encoding': 'gzip',
    'transfer-encoding': 'chunked',
    'connection': 'close',
    'server': 'nginx/1.0.4',
    'x-runtime': '148ms',
    'etag': '"e1ca502697e5c9317743dc078f67693f"',
    'content-type': 'application/json'
}


>>> r.headers['Content-Type']
'application/json'

>>>r.headers.get('content-type')
'application/json'

>>> url = 'http://example.com/some/cookie/setting/url'
>>> r = requests.get(url)

>>> r.cookies['example_cookie_name']
'example_cookie_value'
'''

'''
req = requests.Request('GET', 'https://httpbin.org/get')
이거 많이 썼는데
대문자 R인거 봐야 한다.

>>> s = requests.Session()
>>> s.send(r)
<Response [200]>
'''

#content > div > section > div:nth-child(2) > div.small-widget.get-started-widget > p:nth-child(2)
res=soup.select("div.small-widget.get-started-widget > p:nth-child(2)")
for item in res:
    print(item.get_text())

# div:nth-child(2) > div.small-widget.download-widget > p:nth-child(2)
res2=soup.select("div.small-widget.download-widget > p:nth-child(2)")
for item in res2:
    print(item.get_text())

print("####################각각의 div들의 p")
# #content > div > section
res3=soup.select("div > section> div:nth-child(2) > div > p:nth-child(2)")
for item in res3:
    print(item.get_text())

print("----------------------------------------")
p_tags=soup.select('section.main-content > div:nth-child(2)')
for p in p_tags:
    print(p.get_text())
