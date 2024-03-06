from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("https://www.jobkorea.co.kr/company/1801053/PassAvgSpec?Page=1&IsAlumniPersonOn=0&Tab=3&VPage=1")

bsObject=BeautifulSoup(html, "html.parser")