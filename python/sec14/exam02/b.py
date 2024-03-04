# 240109(화) 오전 10시 25분쯤? 영상 1시 14분쯤?
# b 파일은 파인드로 css 추출해서 탐색해보자.

from bs4 import BeautifulSoup

# 1. olview.html 파일을 로드해서 soup 객체를 생성한다.
print("# 1. olview.html 파일을 로드해서 soup 객체를 생성한다.")
with open("sec03/olview02.html", encoding='utf-8') as fp:
    soup=BeautifulSoup(fp, 'html.parser')
# print(soup.prettify())

css_classes=set()   # 클래스들을 담을 변수
clss_id=set()       # id들을 담을 변수

# 모든 태그를 탐색 find_all(True)
# 클래스 속성이 있는 경우 값을 추출해서 저장      'class' in tag_attrs:
# id 속성이 있는 경우 값을 추출해서 저장         'id' in tag_attrs:

# print("css_classes :",css_classes)  # 셋으로 추출가능 파이썬 코드임
# print("clss_id :", clss_id)

print("##########모든 태그를 탐색 find_all(True)")
for tag in soup.find_all(True):
    print(tag)

    ########## 클래스 속성이 있는 경우 값을 추출해서 저장
    if 'class' in tag.attrs:
        css_classes.update(tag['class'])

    ######### id 속성이 있는 경우 값을 추출해서 저장
    if 'id' in tag.attrs:
        clss_id.add(tag['id'])

print("css_classes :",css_classes)
print("clss_id :", clss_id)