from bs4 import BeautifulSoup
html_doc = """
<html>
<body>
<table>
<caption> mylist </caption>
<thead>
<tr>
  <th>Name</th>
  <th>Age</th>
  <th>City</th>
</tr>
</thead>
<tbody>
<tr>
  <td>John</td>
  <td>25</td>
  <td>New York</td>
</tr>
</tbody>
<tr>
  <td>Alice</td>
  <td>30</td>
  <td>London</td>
</tr>
</table>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')  #전체 문서 객체로 리턴

# 1. 테이블의 제목인 thead의 문자열만 출력하자.
res_thed=soup.find_all('thead')  # thead. . 이런식으로 하라는 데 뭔 솔...? ㅋㅋㅋ
for i in res_thed:
    print(i.get_text())

print("############쌤 방법 select")
res_thed=[th for th in soup.select('body table thead tr th')]

for thed in res_thed:
    print(thed.get_text())

print("#############쉬운 방법")
thead_text=soup.thead.get_text().strip()       # 리턴되는 문자열의 앞 뒤 공백 제거
print(thead_text)

# 2. tbody의 문자열만 출력하자.
res_thed=soup.find_all('tbody')
for i in res_thed:
    print(i.get_text())

print("#############쉬운 방법")
tbody_text=soup.tbody.get_text().strip()
print(tbody_text)

# 3. 1,2번으로 추출한 내용을 가지고 caption의 문자열을 파일명으로 지정해서 mylist.txt로 저장하자.
'''
temp=soup.caption.get_text().strip() + '.txt'
with open(temp,'w') as f:
    for string in list1:
        f.write(string+',')
    f.write('\n')
    for string in list2:
        f.write(string+',')
'''
temp=soup.caption.get_text().strip() + '.txt'
with open(temp,'w') as f:
    f.write(thead_text+'\n'+tbody_text)