from bs4 import BeautifulSoup

# 1. olview.html 파일을 로드해서 soup 객체를 생성한다.
with open("sec03/olview02.html", encoding='utf-8') as fp:
    soup=BeautifulSoup(fp, 'html.parser')
# print(soup.prettify())

# c 파일의 클래스랑 id를 셀렉트로 확인해봤다.
# for tag in soup.select('*'):
# css_classes : {'b1', 'a1'}
# clss_id : {'d1', 'e1', 'c1'}

############# select()
print("############# select()")
# 1. id 중에 e1인 태그를 찾아서 값만 출력해보자. id중 e1은 하나니까 select_one()으로 찾고
id_res = soup.select_one('#e1')
if id_res:
    print(id_res.get_text())
print('-----------------------------')

# 2. class 중에 a1인 태그를 찾아서 값만 출력해보자. 여기서는 select()로 하는게 좋겠다.
class_res= soup.select('.a1')
for tag in class_res:
    print(tag.get_text())

######### find_all()
print("######### find_all()")
# 1. id 중에 e1인 태그를 찾아서 값만 출력해보자. find()
id_res=soup.find(id='e1')
if id_res:
    print(id_res.get_text())
print('-----------------------------')

# 2. class 중에 a1인 태그를 찾아서 값만 출력해보자. find_all()
class_res= soup.find_all(class_='a1')
for tag in class_res:
    print(tag.get_text())
print("----------------------------")