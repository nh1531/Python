import pandas as pd

df = pd.read_csv('일별평균대기오염도_2022.csv', encoding="cp949") #encoding="cp949" -> 한글 인코딩
#print(df.info())
#print(df.head())
#print(df.tail(10))
print(df.columns)
# 열 선택 방법 3: 대괄호([])를 이용한 복수 열 선택
name_age_col = df[['측정일시', '측정소명', '이산화질소농도(ppm)']]
print(name_age_col)

# 열 선택 방법 5: iloc[]를 이용한 열 선택
name_age_col = df.iloc[:, [0, 1]]
print(name_age_col)

# 행 선택 방법 4: loc[]를 이용한 복수 행 선택
rows_2_4 = df.loc[[2, 4]]
print(rows_2_4)

sub_df = df.loc[df['미세먼지농도(㎍/㎥)'] >= 30]
print(sub_df)

# 조건을 사용하여 데이터 선택
df.loc[(df['미세먼지농도(㎍/㎥)'] >= 30) & (df['초미세먼지농도(㎍/㎥)'] > 20)]

# 부분 데이터 선택 방법 5: 조건에 따른 선택 후 열 지정
# age>30 인 항목 중에 name과 city를 가져와라
#sub_df_5 = df[df['age'] > 30][['name', 'city']]
#print(sub_df_5)

# 나이가 30 이상이고, 도시가 'London'인 데이터 선택
# 미세먼지농도 30이상(하나의 dataframe) dataframe 중에서  -> 모든 조건 다 가지고 옴
# '측정일시', '측정소명' 만 뽑아냄
#sub_df = df.query('미세먼지농도(㎍/㎥) >= 30')[['측정일시', '측정소명']]
#print(sub_df)

sub_df = df.loc[(df['미세먼지농도(㎍/㎥)'] >= 30)].loc[:,['측정일시', '측정소명']]
print(sub_df)

sub_df_3 = df.iloc[1:3, 1:3]
print(sub_df_3)

# 부분 데이터 선택 방법 5: 조건에 따른 선택 후 열 지정
sub_df_5 = df[df['age'] > 30][['name', 'city']]
print(sub_df_5)




