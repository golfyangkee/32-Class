import bs4
from bs4 import BeautifulSoup
# Create an HTML document
'''
  1. html -> head / body , p,div , ul,li, img,a ,table , form 
  2. css3  -> id, class, element.attrs
'''
html_doc = """
<html>
<head>
<title>Example HTML Document</title>
</head>
<body>
<h1>Heading 1</h1>
<p>This is a paragraph.</p>
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
</body>
</html>
"""

def Element() :
    # < ul >
    # < li > Item 1 < / li >
    # < li > Item 2 < / li >
    # < li > Item 3 < / li >
    # < / ul >
    # body > ul
    soup = BeautifulSoup(html_doc, 'html.parser') #전체 문서를 객체로 리턴

    #요소를 바로 찾아간다.
    title = soup.title.get_text().strip()
    heading = soup.h1.get_text().strip()
    paragraph = soup.p.get_text().strip()

    #객체 메소드로 리턴  find_all
    list_items = [li.get_text() for li in soup.find_all('li')]

    print("Title:", title)
    print("Heading:", heading)
    print("Paragraph:", paragraph)
    print("List Items:", list_items)

def XPath():
    '''
     / : 선택 / : 루트 요소 선택
    // : 모든 요소 선택
    element : 문서의 모든 수준에서 선택합니다.
    element/하위 엘리먼트  : 주어진 이름을 가진 모든 요소를 선택합니다.
    @attribute : 주어진 이름을 가진 속성을 선택합니다.
    predicate : 조건에 따라 요소를 필터링합니다.
    '''

    soup = BeautifulSoup(html_doc, 'html.parser')
    h1_element = soup.select('h1')
    print(h1_element[0].get_text())


    p_element = soup.select('p')
    print(p_element[0].get_text())


    ul_element = soup.select('ul')
    print(ul_element[0])  # Output: <ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>

def Select_m():
    # body > ul
    soup = BeautifulSoup(html_doc, 'html.parser')  # 전체 문서를 객체로 리턴
    res=soup.select("body > ul > li:nth-child(2)") # 컨텐츠나 텍스트 요소복사하니까 Item 3 이대로 넣을 수는 없지
    # body > ul 도 확인해보자.
    print(res, type(res))
    # print(help(bs4.element.ResultSet))


    # ul의 xpath : /html/body/ul  경로 확인할 때 하게된다.
    # li의 텍스트 xpath : /html/body/ul/li[3]/text() 메소드 호출

    # selector들은 의사 요소 태그 요소를 관리하는 구나
    # css 했을 때 챕터 2 5 6 7 했던거 거다.
    # 요소 관리를 css의 selector 형태로 한다는 거다 의사클래스 의사클래스의 엘리먼트

    # 하나는 node로 하나는 요소로 가지고 온다.
if __name__ == '__main__':
    XPath()
