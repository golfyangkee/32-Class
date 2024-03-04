# 240109(화) 오전 10시 10분쯤? 영상 1시쯤
# a 파일은 파인드로 밸류 가지고 왔는데

from bs4 import BeautifulSoup

# 1. olview.html 파일을 로드해서 soup 객체를 생성한다.
print("# 1. olview.html 파일을 로드해서 soup 객체를 생성한다.")
with open("sec03/olview.html", encoding='utf-8') as fp:
    soup=BeautifulSoup(fp, 'html.parser')
# print(soup.prettify())
print('----------------------------------------------------------')

# 2. 모든 <ol> 태그를 추출하자.
print("# 2. 모든 <ol> 태그를 추출하자.")
ol_tag=soup.find_all('ol')

for ol in ol_tag:
    print(ol.prettify())
print('----------------------------------------------------------')
# prettify() 함수는 원문 그대로를 가지고 오는 거 같다.

# 3. <ol> 태그 중 속성이 type 'a'만 추출해보자.
print("# 3. <ol> 태그 중 속성이 type 'a'만 추출해보자.")
res=soup.find_all('ol', {'type':'a'})
for ol in res:
    print(ol)
print('----------------------------------------------------------')

# 4. <ol> 태그 중 속성이 type 'A'의 li의 값만 추출해보자.
print("# 4. <ol> 태그 중 속성이 type 'A'의 li의 값만 추출해보자.")
res02=soup.find_all('ol',{'type':'A'})
li_texts = [li.get_text() for ol in res02 for li in ol.find_all('li')]
# get_text로 하는게 편하다고 했는데 왜 때문인지는 잘 모르겠다.
for text in li_texts:
    print(text)
print('----------------------------------------------------------')

