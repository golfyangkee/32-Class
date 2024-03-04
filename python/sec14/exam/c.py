# 24.01.08 오후 5시 9분쯤 영상 3시 14분쯤
from bs4 import BeautifulSoup, Comment

markup = "<b><!--Hey, buddy. Want to buy a used parser?--> abcd</b>"
soup = BeautifulSoup(markup, 'html.parser')

# 주석과 문자열을 저장할 리스트 객체
comment_all = []
text_all = []

# 'recursiveChildGenerator' 이거 서보자.
print(help(soup.recursiveChildGenerator))
# 다운로드 받으면 받은 애 앨리먼트를 포를 돌리지 않아도 싹 가지고 온다. 왠만하면 포를 이용해서 써라 하는 거다.앞으로 없어진다고 함
# 써보고 원리를 보자. 앞에 b.py를 넣어보면 된다는 데 뭔솔?

print(soup.recursiveChildGenerator())

for element in soup.recursiveChildGenerator():
    if isinstance(element, Comment):
        comment_all.append(element)
    elif    isinstance(element, str):
        text_all.append(element.strip())
print(comment_all)
print(text_all)