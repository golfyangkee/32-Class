# 24.01.08 오후 5시 19분쯤 영상 3시 24분쯤
from bs4 import BeautifulSoup, Comment

markup = "<b><!--Hey, buddy. Want to buy a used parser?--> abcd</b>"
soup = BeautifulSoup(markup, 'html.parser')

# 주석과 문자열을 저장할 리스트 객체
comment_all = []
text_all = []
print(help(soup.recursiveChildGenerator))
print(soup.recursiveChildGenerator())

for element in soup.b.children:
    if isinstance(element, Comment):    # 객체의 타입 유무 확인 메소드
        comment_all.append(element)
    elif    isinstance(element, str):
        text_all.append(element.strip())
print(comment_all)
print(text_all)
# 잘 나오니 앞으로 이거 쓰라고 하심
# 파싱할 때 주석하고 문자열이랑 섞어 들어올때가 가장 힘드니까 파이참에서 이렇게 실행하면 된다.

# repr로도 뽑아올 수 있다. 이거는 d파일이다.
for string in soup.strings:
    print(repr(string))