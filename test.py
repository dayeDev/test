import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# Chrome 브라우저를 사용하여 WebDriver 객체를 생성합니다.
driver = webdriver.Chrome()

# WebDriver의 실행이 완료될 떄 까지 최대 5초간 대기
driver.implicitly_wait(5)

# 크롬 브라우저 실행
driver.get("https://www.naver.com")

# Naver 검색 입력창에 입력
driver.find_element(By.NAME, "query").send_keys("네이버검색")

# Naver 검색 버튼 클릭
driver.find_element(By.CLASS_NAME, "btn_search").click()


sleep(5) #5초 쉼
