import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 키보드 입력할 때 사용

browser = webdriver.Chrome() # 같은 경로에 있어서 chromdriver.exe위치를 안적어줘도됨 ("./chromedriver.exe") 이렇게 하는거랑 지금 똑같음.. (다른 위치면 경로 적어줘야함!!)
# 1. 네이버 이동
browser.get("http://naver.com") 

# 2. 로그인 버튼으로 이동
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)

# 5. id 를 새로 입력
# browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit()  # 모든 창 종료 
