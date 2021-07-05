import requests
from bs4 import BeautifulSoup

url = "http://www.patagonia.co.kr/shop/goods/goods_list.php?&category=003016"
# url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음 발견되는 a elemetn 출력
# print(soup.a.attrs['href']) # a element의 속성 정보를 출력
# print(soup.a["href"]) # a element의 href 속성 정보를 출력

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class = Nbtn_upload 인 a element 를 찾아줘
# print(soup.find(attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인 어떤 element 를 찾아줘

# print(soup.find("li", attrs={"class":"rank01"}))
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a)
suncap = soup.find("li", attrs={"id":"item_3781"})
print(suncap.p.span.get_text())