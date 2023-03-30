import requests
from bs4 import BeautifulSoup

#크롤링을 원하는 페이지 주소 html 
url = "https://www.hani.co.kr/arti/list.html?sec=news&subsec=politics"
# url html 코드 받아옴
response = requests.get(url)

# BeautifulSoup -> 파싱하는 모듈
soup = BeautifulSoup(response.text, "html.parser")
# f12 개발자 도구에서 확인가능
# ariticle-title인 h4태그 가지고 옴. h4->태그의 특징
# find_all -> 태그를 넣을 수 있는 함수
# h4.article-title -> h4태그.클래스명
titles = soup.find_all("h4", class_="article-title")
# .strip() 문자열 양쪽 공백 제거
for title in titles:
    print(title.text.strip())
