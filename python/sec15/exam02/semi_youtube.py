import requests
from bs4 import BeautifulSoup
import datetime

keyword=input("키워드를 입력하세요 : ")
pageNum= input("몇 페이지까지 출려하세요?")

for n in range(1, int(pageNum)+1):
    try:
        soup = requests.get

    except: