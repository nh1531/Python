import requests
from bs4 import BeautifulSoup

url = 'https://movie.daum.net/ranking/reservation'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)

# select -> css 선택자 사용
ol = soup.select_one('.list_movieranking')
#print(ol)

#ol 태그 안의 li 태그 가지고 나옴
li_list = ol.find_all('li') # 태그들의 리스트
print(li_list)

# 저장 list로 , 빈 list 생성 -> []
movie = []

# li -> 태그
for li in li_list:
    # .rank_num -> 클래스명
    # select, find 위에서부터 하나
    rank = li.select_one('.rank_num').text #순위
    name = li.select_one('.link_txt').text #제목
    see = li.select_one('.ico_see').text #관람가
    grade = li.select_one('.txt_grade').text #평점
    # text[:-1]로 예매율의 % 제거함
    num = li.select_one('.txt_num').text[:-1] #예매율
    mvdate = li.select_one('.txt_info > .txt_num').text #개봉일
    print(rank, name, see, grade, num, mvdate)
    
    movie.append([rank, name, see, grade, num, mvdate])

print(movie)

import pandas as pd

#list-> dataframe -> csv
df = pd.DataFrame(movie, columns = ['순위', '영화제목', '관람가', '평점', '예매율', '개봉일'])
df.to_csv('movie_info.csv', index=False, encoding='cp949')

df = pd.read_csv('movie_info.csv', encoding='cp949') # read로 읽어오면 알아서 숫자만 있는 것은 int로 변환해줌 

print(df.info())

# 조건 여러개 사용시에는 소괄호() 사용
# 그냥 파일을 info해서 봤을 때 datatype이 전부 object임(평점>8 하면 에러남)-> 형변환. 저장하고 읽어오기
print(df[df['평점']>8])

#그래프
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family'] = 'Malgun Gothic' #한글이 들어가있으면 폰트추가

# 개봉일 23.01.04 -> '%y.%m.%d' 날짜형식 데이터로 형변환
df['개봉일'] = pd.to_datetime(df['개봉일'], format = '%y.%m.%d')
#print(df.info()) # 개봉일이 datetime으로 변환된 것 확인

# W -> 주별 week
# 숫자가 아닌것들이 있으면 에러는 아니지만 워닝이 뜸. 그래서 numeric_only
# 숫자인것은 평균을 내겠다
df_weekly = df.resample('W', on='개봉일').mean(numeric_only = True)
#print(df_weekly)

#NaN notanumber 값 때문에 중간에 데이터가 날아감. 그래프가 안나옴.  결측치 처리 필요. 9장 34p. 결측치 처리
df_weekly = df_weekly.fillna(0) #결측치를 0으로 채우겠다
print(df_weekly)

#index가 x값
plt.plot(df_weekly.index, df_weekly['예매율'])
plt.show()

크롤링
csv 파일 분석

크롤링 판다스로 저장해서 그래프로 보여주거나

