from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("windw-size=1902x1080") # pc해상도 설정
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
# AppleWebKit/537.36 (KHTML, like Gecko) 
# Chrome/91.0.4472.124 Safari/537.36

# user-agent 값이 headless chrome이라서 한번씩 접속이 안될수 있으니
# 사이트에 따라 user-agent값 설정 필요!
detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()