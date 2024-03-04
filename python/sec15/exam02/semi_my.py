import os
import re
import subprocess
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)
url='https://www.jobkorea.co.kr/company/1696583/PassAvgSpec?Tab=3&VPage=1'

sleep(10) # 하얀화면으로 엣지 뜬다.
driver.get(url)     # 3. 브라우저 실행해서 url 요청을 한다.
sleep(10)
soup=BeautifulSoup(driver.page_source,'html.parser') # 파싱 객체 생성
# print(soup)

li_list = soup.select('.indLists .specListWrap')

# print(li_list)
# for li in li_list:
    # txyear = li.find('span', class_='txYear').text
    # cate = li.find('span', class_='cate').text
    # tx = li.find('span', class_='tx').text
    # num = li.find('span', class_='num').text
    # score = li.find('span', class_='score').text

    # print(f'{txyear} {cate} {tx} {num} {score} {score}')

    # item_list = soup.select('.item')
    # for item in item_list:
    #     score=item.find('span', class_='score').text
    #     print(f'{score}')
    #

scores = soup.select(".score_value")  # 해당 페이지의 학점과 토익 점수 클래스에 따라 수정
for score in scores:
    print(score.get_text())

driver.close()