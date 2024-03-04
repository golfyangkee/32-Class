# 24.01.08 오후 5시 2분 영상 3시 8분쯤
from bs4 import BeautifulSoup

markup = "<b><!--Hey, buddy. Want to buy a used parser?--> abcd</b>"
soup = BeautifulSoup(markup, 'html.parser')
comment = soup.b.string
print(comment)
print(type(comment))
# <class 'bs4.element.Comment'>

print("text로 해보자")
comment = soup.b.text
print(comment)
# 주석은 안 오고 일반 텍스트만 온다.
print(type(comment))
'''
주석은 스트링으로 뽑아오면 되는데
bold채 abcd 는 텍스트로 뽑아오면 된다.
이 텍스트는 abcd만 인지하지 실제 주석은 인지 못함

스트링ㅇ=과 text는 다르다.
get_string? 이랑 get_text랑 은 어떨까?
'''
print("get_text 해보자")
comment = soup.get_text
print(comment)
# 주석 포함해서 다 가지고 온다.
print(type(comment))

'''
html주석과 xml 주석은 다를 수 있는 거 인지해야 한다.
'''
