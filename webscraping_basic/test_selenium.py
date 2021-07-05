# import requests
from bs4 import BeautifulSoup

# url = "http://www.freitag.ch/en/bags"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# # selenium 쓸지 requests 쓸지
# with open("freitag.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())

# # bag = soup.find("div", {"class":"node__content"})
# # print(bag)

from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("windw-size=1902x1080") # pc해상도 설정
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "http://www.freitag.ch/en/bags"
browser.get(url)

browser.find_element_by_class_name("node__content")
soup = BeautifulSoup(browser.page_source, "lxml")
bags = soup.find_all("div", attrs={"class":"w-full lg:w-1/4 px-sm"})
for bag in bags:
    print(bag.get_text())
    print("-" * 100)
browser.quit()