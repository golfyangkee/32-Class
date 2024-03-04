import os
import re
import subprocess
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)
url='https://comic.naver.com/webtoon?tab=tue'

sleep(10) # 하얀화면으로 엣지 뜬다.
driver.get(url)     # 3. 브라우저 실행해서 url 요청을 한다.
sleep(10)
soup=BeautifulSoup(driver.page_source,'html.parser') # 파싱 객체 생성
print(soup)

li_list = soup.select('.component_wrap .item')
# print(li_list)
for li in li_list:
    title = li.find('span', class_='ContentTitle__title--e3qXt').text
    star = li.find('span', class_='Rating__star_area--dFzsb').text
    print(f'{star} "{title}"')

driver.close()