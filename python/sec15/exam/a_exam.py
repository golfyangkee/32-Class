import time
from selenium import webdriver
# 샘플 코드가 최신버전이라고 간주화 했을 때
# 오류 엄청 뜨는데

driver = webdriver.Chrome('/path/to/chromedriver')
driver.get('http://www.google.com/');
time.sleep(5)
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)
driver.quit()