# 뷰티풀샵 파서
from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup, type(soup))
# print(dir(soup))
'''
'find', 'findAll', 'findAllNext', 'findAllPrevious', 'findChild', 'findChildren', 'findNext', 'findNextSibling', 
'findNextSiblings', 'findParent', 'findParents', 'findPrevious', 'findPreviousSibling', 'findPreviousSiblings', 
'find_all', 'find_all_next', 'find_all_previous', 'find_next', 'find_next_sibling', 'find_next_siblings', 
'find_parent', 'find_parents', 'find_previous', 'find_previous_sibling', 'find_previous_siblings',

'format_string', 'formatter_for_name'
node 시리즈??

get도 있고 
has도 있다.
'''
print(soup.html.body.a['class'])
print(soup.html.body.a['href'])
print(soup.html.body.a['id'])
print(soup.html.body.p.text)

print(help(soup.find))
'''
find(name=None, attrs={}, recursive=True, string=None, **kwargs) method of bs4.BeautifulSoup instance
-> 파인드에서 네임을 주던, 속성을 {}로 주던, 딕트 등등으로도 가지고 올 수 있다.
    Look in the children of this PageElement and find the first
    PageElement that matches the given criteria.

    All find_* methods take a common set of arguments. See the online
    documentation for detailed explanations.

    :param name: A filter on tag name.
    :param attrs: A dictionary of filters on attribute values.
    :param recursive: If this is True, find() will perform a
        recursive search of this PageElement's children. Otherwise,
        only the direct children will be considered.
    :param limit: Stop looking after finding this many results.
    :kwargs: A dictionary of filters on attribute values.
    :return: A PageElement.
    :rtype: bs4.element.Tag | bs4.element.NavigableString
'''
print(soup.find('p').text)  # soup.find('p'). = soup.html.body.p

res = soup.findAll('a')
for m_res in res:
    print(m_res)
print('===============')
for m_res in res:
    print(m_res['href'])     # print(link.get('href')) 이거도 가능

'''
네이버 : http://www.naver.com 이렇게 수집해서 리턴하고 싶다
그러면 앞에 value 받고 text 받고 싶다.
'''
res = soup.findAll('a')
for m_res in res:
    print(f"{m_res.text} \t {m_res['href']}")

'''
print(soup.get_text())
# The Dormouse's story
#
# The Dormouse's story
#
# Once upon a time there were three little sisters; and their names were
# Elsie,
# Lacie and
# Tillie;
# and they lived at the bottom of a well.
#
# ...
이렇게 글만 가지고 옴
'''

# attr은 키와 밸류로 이루어진 딕트 타입이구나.
# tag.attrs
# # {'id': 'boldest'}

'''
Multi-valued attributes
여기서 부터 눈도장
어떻게 가지고 오는지

css_soup = BeautifulSoup('<p class="body"></p>', 'html.parser')
css_soup.p['class']
# ['body']

css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')
css_soup.p['class']
# ['body', 'strikeout']
body strikeout 한칸 뛰고니까 하위에 있는게 2개로 나온다.

id_soup = BeautifulSoup('<p id="my id"></p>', 'html.parser')
id_soup.p['id']
# 'my id'
id는 더블로 묶어 뒀으니까 이름 1개구나 한다. 중복 속성되었다고 간주하는 거

rel_soup = BeautifulSoup('<p>Back to the <a rel="index first">homepage</a></p>', 'html.parser')
rel_soup.a['rel']
# ['index', 'first']
피 태그 안에 rel 주고 문서로 맵핑했을 때 아니면 라벨링 했을 때 공백기준으로 콤바로 나열

rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)
# <p>Back to the <a rel="index contents">homepage</a></p>
콤마로 나열하면 공백처리 된다.

no_list_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser', multi_valued_attributes=None)
no_list_soup.p['class']
# 'body strikeout'
피 클래스를 파서하는건 똑같은데 none이라고 선언하면 하나로 읽어가지고 오더라

id_soup.p.get_attribute_list('id')
# ["my id"]
어차피 아이디는 적용 안되니까 하나로 읽어가지고 온다. xml도 마찬가지다

class_is_multi= { '*' : 'class'}
xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml', multi_valued_attributes=class_is_multi)
xml_soup.p['class']
# ['body', 'strikeout']
뷰티풀 숩이 가지고 있는 
하나로 지정해도 된다. 공백 지정

뎁스로 구현되는 애들?

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
태그 가지고 오고
tag.string
스트링 가지고 왔떠니 스트링 값 나옴 text랑 get_textstring() 를 더 많이 쓴다?
# 'Extremely bold'

type(tag.string)
# <class 'bs4.element.NavigableString'>

footer = BeautifulSoup("<footer>Here's the footer</footer>", "xml")
xml로도 파싱함

주석은 어떻게 할까?
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, 'html.parser')
comment = soup.b.string
type(comment)
# <class 'bs4.element.Comment'>
주석 인지한다.
해보자 b.py
'''
# 24.01.08 5시 20분쯤 영상 3시 30분쯤?
print('-------------------')
for string in soup.strings:
    print(repr(string))

# strings로 가지고 오니가 다 분철해서 가지고 온다.
# 하다보면 값이 안 나올 때가 있는데 오른쪽 마우스 텍스트 했는데 애네들은 주석이었고 그러다 보니
# comment도 쓰고 스트링도 쓰고 다양하게 쓴다.

'''
A list 봐야한다.
'''
'''
find_all 은 리턴값이 리스트인데.
soup.find_all(["a", "b"])
# [<b>The Dormouse's story</b>,
#  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

하나로 추욱 리턴되고 있어서 내가 사용하고자 하는 태그는 어디에 들어가 있는지 보고 싶을 때
for tag in soup.find_all(True):
    print(tag.name)
# html
# head
# title
# body
# p
# b
# p
# a
# a
# a
# p

여기서 사용하고자 하는 펑션을 할 수 있다.
강사가 find랑 find_all이랑 select를 가장 많이 쓰는데
find는 요소를 빨리 찾음 examp에서 하는 거는 find는 요소를 잘 찾음
select 는 css를 빨리 찾음 css 값이 적용된 애들을 가장 잘 찾음
크로스로 다 찾을 순 있지만(select에서 요소를, find가 css를) 명칭을 보면 각 장점을 활용해서 찾아
find는 하나만 리턴
find_all는 하나 이상의 요소 리턴하는 메소드니까
그 괄호안에 함수로 핸들링할 수 있다.
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
클래스만 단독으로 있는 애들을 리턴해주겠다고 핸들링값을 만들어서
soup.find_all(has_class_but_no_id)
# [<p class="title"><b>The Dormouse's story</b></p>,
#  <p class="story">Once upon a time there were…bottom of a well.</p>,
#  <p class="story">...</p>]

구현하면 아이디가 없는 클래스 애들만 리턴해준다.
함수 핸들링도 할 수 있다. find_all 리턴값만 맞으면 된다.

밑에 정규식 패턴이 있다.
import re 로 

import re
def not_lacie(href):
    return href and not re.compile("lacie").search(href)

soup.find_all(href=not_lacie)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

그래서 밑에 보시면

find_all(name, attrs, recursive, string, limit, **kwargs)
샘플로 잘 설명되어 있다.

네임 아규먼트 들은 중복되는 내용이랑 스킵하고

Searching by CSS class¶
여기에서 
find_all에서도 class 찾을 수 있다.
soup.find_all("a", class_="sister")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

정규패턴이 맞는 애들만 가져다가 찾을 수 있다.
펑션 만들어서
soup.find_all(class_=re.compile("itl"))
# [<p class="title"><b>The Dormouse's story</b></p>]

def has_six_characters(css_class):
    return css_class is not None and len(css_class) == 6

soup.find_all(class_=has_six_characters)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

뷰티풀숩해서 html 파서를 줬는데 클래스 명칭을 find_all에서 지정하면 해당 클래스 내용 리턴해준다.
find_all 피태그 주고 클래스 주면 공백을 줬을 때 속성이 없거든 그래서 ㅋㄹ래스 값만 리턴하면 다 리턴이 된다는 말이다. 
그리고 나서 앞에꺼만 body만 줘도 가지고 온다.
css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')
css_soup.find_all("p", class_="strikeout")
# [<p class="body strikeout"></p>]

css_soup.find_all("p", class_="body")
# [<p class="body strikeout"></p>]

밸류가 가진 클래스 어트리뷰트를 찾고 싶을 때

베리어블 스트링 값은 리턴되지 않는다. 거꾸로 주면 안 나온다.
css_soup.find_all("p", class_="strikeout body")
# []

css_soup.select("p.strikeout.body")
# [<p class="body strikeout"></p>]
가장 빠르게 가지고 온다.
파인드처럼... 찾으면 바로 리턴해주는 형태이다. 앞뒤로 바뀌어 있어도

attrs 키 밸류로 가지고 있으니까
soup.find_all("a", attrs={"class": "sister"})
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
잘 리턴해준다.
곽괄호해서 편하게 쓰기도 한다.

밑에 가보면
find_all 해당 스트링, 텍스트도, 문자열 찾아줘 세개 찾아줘 컴파일 찾워 핸들링도 찾아준다.
soup.find_all(string="Elsie")
# ['Elsie']

soup.find_all(string=["Tillie", "Elsie", "Lacie"])
# ['Elsie', 'Lacie', 'Tillie']

soup.find_all(string=re.compile("Dormouse"))
# ["The Dormouse's story", "The Dormouse's story"]

def is_the_only_string_within_a_tag(s):
    """Return True if this string is the only child of its parent tag."""
    return (s == s.parent.string)

soup.find_all(string=is_the_only_string_within_a_tag)
# ["The Dormouse's story", "The Dormouse's story", 'Elsie', 'Lacie', 'Tillie', '...']

soup.find_all("a", limit=2)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
2개만 찾아줘

find_parents() and find_parent()¶
여기서 부터는 노드로 찾아간다?
매개인자는 똑같다.
find, find_all 다 똑같다 매개인자가

html 태그 중 
find_all_next() and find_next()
next라는 태그가 있다.

속성에서
next시리즈가 있는데 그냥 next가 있는 애들이 있다.
여기서는 단문이 잠깐 body를 클릭하면 
next가 있고 all_next이러면서 메소드를 만들었다.
나중에 나오면 봅시다.

그리고 그대로 시블링 얘들 이용해서
next, previous 등등 찾아가는데 우리는 
find find_all select 만으로도 잘 찾아갈 수 있다.

select는 css를 발리 찾는다고 했는데
의사 요소 찾을대는 select 쓴다.
soup.css.select("body a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie"  id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.css.select("html head title")
# [<title>The Dormouse's story</title>]

이런 얘들

의외로 태그는 찾기 쉬운데
사실 이름이 간단하지도 않고 보면
클래스도 뎁스를 많이 만들어서 중복으로 많이 만들어서
단촐하게는 없어서
soup.css.select("#link1 ~ .sister")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie"  id="link3">Tillie</a>]

soup.css.select("#link1 + .sister")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

이런식으로 단어가 있으면 찾아와 이런거 많이 슨다.
지금 클래스는 . 아이디는 # 어트리뷰트값[''] 'a[href=""]' 
잘 찾음

그리고 is 시리즈? 
파인드 객체에서 찾은 거 중에 css로 찾을 수도 있다. 그 중 필터 'a'만
[tag.string for tag in soup.find('p', 'story').css.filter('a')]
# ['Elsie', 'Lacie', 'Tillie']

네임스페이스는 xml 할때 잘 쓰는데

불러오는 법
from bs4 import BeautifulSoup
xml = """<tag xmlns:ns1="http://namespace1/" xmlns:ns2="http://namespace2/">
 <ns1:child>I'm in namespace 1</ns1:child>
 <ns2:child>I'm in namespace 2</ns2:child>
</tag> """
namespace_soup = BeautifulSoup(xml, "xml")

namespace_soup.css.select("child")
# [<ns1:child>I'm in namespace 1</ns1:child>, <ns2:child>I'm in namespace 2</ns2:child>]

namespace_soup.css.select("ns1|child")
# [<ns1:child>I'm in namespace 1</ns1:child>]
요 부분은 내일 진행하자.

그리고 받은 거 중에 exam 말고
a 보면
html 독스를 파싱하는데 셀렉트하는 거 중에 href만 추출하고 싶다 니까
list for로 함축 코드로 가지고 올 ㅅ 있다.
크로링할 때 어려운건 코드가 안 읽어진다.

b
현재 문자열이 구현이 되어 있다 이거는 테이블
테이블 가져다가 orw 셀렉트 로우즈 하는 거 bcd 쭉 있다.
수업 전에 한번씩 돌려보자.

5시 46분경 영상 3시 52분경
갑자기 멀티잇 사이트 들어가서
검사 해서 요소 보기 시작
복사 해본다.
가지고 와야 이미지 달랑 가지고 올 수 있다고
요령 배워보자고 하심

오늘의 수업 내용은
아침에 css 가서 박스모델하고 namespace selector(주역) attribute, box model(연습처럼) 이렇게 해서 selector level3 가면 E: 이런거 보자.
챕터 2 그리고 6 7 5는 콤마 나열? 
도움말 보면서 하다 보니 시간이 좀 오래 걸렸고
내일은 뷰티풀숩 정리하고
크롤링 하고
크롬가져다가 비동기통신 하는거 한다는데

오늘 css 접근하는 거 했는데
재미있었냐고?
html 하고 css 재미가 없어서
하....
'''