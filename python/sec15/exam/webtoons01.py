from bs4 import BeautifulSoup
import requests
# naver -> 웹툰 -> 웹툰 -> 화요웹툰
resp = requests.get('https://comic.naver.com/webtoon')
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup)  ### 파싱된 결과를 출력하게 되면 tag가 출력되지 않는다.  -> 비동기 페이지구나.

all_webtoons = soup.find_all('div', class_='component_wrap')
print(all_webtoons)     # 내용 출력되지 않는다.

'''
비동기화? 애들은 파인더가 못 가지고 온다.
상당부분을 다 긁어오지만 실제 가지고 와서 봤더니 내용이 너무 단촐하고
태그가 이거 밖에 없을 수가 없는데
실제 있는 거로를 탐색을 못해서 그런거당
바디에 루트밖에 없네?
이럴리가 없는데?
확인하자
'''

