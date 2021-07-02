from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url) # url로 이동

browser.find_element_by_link_text("가는날 선택").click()

# 이번달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달
# browser.find_elements_by_link_text("28")[0].click() # [0] -> 이번달

# 다음달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[1].click() # [1] -> 다음달
# browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음달

# 이번달 27일, 다음달 28일 선택
browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달
browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음달

# 제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]/div/span").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

# 10초 동안 기다리는데 element가 나오면 바로 ㄱㄱ
# 브라우저 최대 10초동안 기다림 안나오면 에러 10초안에 뭔가 나오면 바로 진행
# expected_condtion으로 저 xpath값에 해당하는 element가 위치할 때 까지 기다려달라는 뜻(xpath말고도 id,class_name, link_text등 사용 가능)
# 페이지 로딩이 길때 이 방식 사용!
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    # 성공했을 때 동작
    print(elem.text) # 첫번쨰 결과 출력
finally:
    # 어떻게든 실행되는 구문 (자바의 try-catch-finally랑 비슷 하지만 파이썬에서는 catch대신 except 로 오류 처리)
    browser.quit()
# 첫번쨰 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem)

