from bs4 import BeautifulSoup

rel_soup = BeautifulSoup('<p>Back to the <a rel="index first">homepage</a></p>', 'html.parser')

print(rel_soup.a['rel'])
# ['index', 'first']

rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)
# <p>Back to the <a rel="index contents">homepage</a></p>

# 이렇게 하면 a['rel'] 이 있는 줄을 가지고 온다?

print("1. 위 문서에 <a href=https://www.example.com>Example 1</a> 를 new_tag로 추가해보자.")
'''
new_tag 예시
soup = BeautifulSoup("<b></b>", 'html.parser')
original_tag = soup.b

new_tag = soup.new_tag("a", href="http://www.example.com")
original_tag.append(new_tag)
original_tag
# <b><a href="http://www.example.com"></a></b>

new_tag.string = "Link text."
original_tag
# <b><a href="http://www.example.com">Link text.</a></b>
'''
original_tag=rel_soup.p
new_tag=rel_soup.new_tag("a", href="https://www.example.com")
original_tag.append(new_tag)
print(original_tag)

print("2. 위 문서에서 a 가 가진 주소만 find_all로 리턴해보자. find_all")
hrefs=[a['href'] for a in rel_soup.find_all('a') if a.has_attr('href')] # 다른 방식으로 할 수 있다.
print("모든 a 태그의 href 속성값:")
print(hrefs)

print("3. 위 문서에서 a 가 가진 문자들만 text로 추출해보자. find_all")
texts=[a.get_text() for a in rel_soup.find_all('a')] # 다른 방식으로 할 수 있다.
print("모든 a 태그의 텍스트:")
print(texts)







