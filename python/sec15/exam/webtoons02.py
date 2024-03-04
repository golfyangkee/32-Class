from selenium import webdriver  # 크롬 드라이버 라이브러리
from bs4 import BeautifulSoup
from time import sleep

url = 'https://comic.naver.com/webtoon?tab=tue'
# ver 4.6 이상부터는  수동드라이버 X
# driver = webdriver.Chrome(service=service) 이렇게 주면 안된다든 말이다.
service = webdriver.chrome.service.Service('./chromedriver.exe')    # 1. 크롬 드라이브 셋팅 같은 공간에 있으니까
                                                                        # chromedriver.exe 이렇게만 써도 된다.
driver = webdriver.Chrome(service=service)      # 2. 브라우저 생성 3초 있다 브라우저 실행
sleep(3)
driver.get(url)  #브라우저 실행해서 url 요청을 한다.
sleep(10)       # 내가 제어할 수 있게 잠시 멈춰봐
soup = BeautifulSoup(driver.page_source, 'html.parser')     # 4. 파싱 객체 생성
print(soup)
'''
li_list = soup.select('.component_wrap .item')
print(li_list)
for li in li_list:
    title = li.find('span', class_='ContentTitle__title--e3qXt').text
    star = li.find('span', class_='Rating__star_area--dFzsb').text
    print(f'{star} "{title}"')
'''
driver.close()
