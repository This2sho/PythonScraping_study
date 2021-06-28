# Study_Scraping
Dev opt(python Scraping)

크롤링 공부용 파이썬 클론코딩 연습
나도코딩 크롤링 강좌 (https://youtu.be/yQ20jZwDjTE)

기본 지식
 웹 스크래핑 : 웹 페이지에서 내가 필요한 데이터를 추출해오는 행위
 웹 크롤링 : 웹 페이지에서 허용된 링크를 따라가서 모든 데이터를 가져오는 것

내가 필요한 기술
 각 쇼핑몰 사이트마다 상품의 이름, 상품의 가격 상품의 사진을 브라우저 개발자 도구를 이용해 분석하고 파이썬의 selenium을 사용하여 상품의 이름, 상품의 이름, 상품의 이미지(imgUrl)을 가져와 json형식으로 만든다.
 그 후 파이어베이스의 realtime database에 json 가져오기를 통해 데이터를 넣어준다.

9. 쿠팡에서 노트북을 구매하는데 5페이지 내에서 광고가 아닌 리뷰가 많고 평점이 높은순으로 랭킹을 매긴다 

※GET 방식은 ?뒤에 변수와 값 그리고 &로 페이지를 요청한다.

※POST 방식은 아이디와 비밀번호 같은 값을 보안을 이용하여 사이트에 보낼수 있음 (큰 데이터도 POST방식으로 보낸다.)

11. for 반복문 안에서 idx, 객체 in enumerate(객체리스트) <- 함수를 통해 idx를 넣을 수 있다.

f write를 통해 파일 저장가능!
