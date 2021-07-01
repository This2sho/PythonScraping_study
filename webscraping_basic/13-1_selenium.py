from selenium import webdriver

from selenium.webdriver.common.keys import Keys # 키보드 입력할 때 사용

browser = webdriver.Chrome() # 같은 경로에 있어서 chromdriver.exe위치를 안적어줘도됨 ("./chromedriver.exe") 이렇게 하는거랑 지금 똑같음.. (다른 위치면 경로 적어줘야함!!)
browser.get("http://naver.com") 
elem = browser.find_element_by_class_name("link_login")
elem
elem.click()
browser.back()
browser.forward()
browser.refresh()
browser.back()
elem = browser.find_element_by_id("query")

elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)
elem = browser.find_element_by_tag_name("a") # tag a인거 하나
elem = browser.find_elements_by_tag_name("a") # tag a인거 다 찾기 find all 느낌
elem
for e in elem:
    e.get_attribute("href") # bs4에서는 [href] 느낌

browser.get("http://daum.net")
elem = browser.find_element_by_name("q")
elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)
browser.back()
elem.send_keys("나도코딩")
elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
elem.click() 
browser.quit()
exit()