import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 데이터프레임 정보 출력
print(df.head())            # 상위 5개 데이터 출력
print(df.tail())            # 하위 5개 데이터 출력
print(df.info())            # 데이터프레임 정보 출력 -> 형변환 하기 전에 info()로 타입 확인
print(df.describe())        # 수치형 열의 기술 통계 정보 출력
print(df.columns)           # 열 이름 출력 
print(df.index)             # 행 인덱스 출력
print(df.dtypes)            # 열의 데이터 타입 출력
print(df.shape)             # 데이터프레임의 크기 출력
print(df.isnull().sum())    # 결측치 개수 출력


import pandas as pd

# 열(column) 선택 -> 사용많이 함 
# iloc[]는 정수 인덱스를 기반으로 데이터를 선택
# loc[]는 인덱스의 이름을 기반으로 데이터를 선택
# loc만 조건 넣어서 사용 가능 (?) 

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 열 선택 방법 1: 대괄호([])를 이용한 단일 열 선택
name_col = df['name']
print(name_col)

# 열 선택 방법 2: 점(.)을 이용한 단일 열 선택
age_col = df.age
print(age_col)

# 열 선택 방법 3: 대괄호([])를 이용한 복수 열 선택
name_age_col = df[['name', 'age']]
print(name_age_col)

# 열 선택 방법 4: loc[]를 이용한 열 선택
# 행,열 적어줘야 함.
#[:, 'name'] -> name 열의 모든 행
name_col = df.loc[:, 'name']
print(name_col)

# 열 선택 방법 5: iloc[]를 이용한 열 선택
# 위치 인덱스 이용
name_age_col = df.iloc[:, [0, 1]]
print(name_age_col)


# 행(row) 선택
'''
query() 메소드
데이터프레임에서 특정 조건에 맞는 데이터를 선택하는 메소드
조건을 문자열로 입력
'''
import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 행 선택 방법 1: 대괄호([])를 이용한 단일 행 선택
row_0 = df.iloc[0]
print(row_0)

# 행 선택 방법 2: loc[]를 이용한 단일 행 선택
row_1 = df.loc[1]
print(row_1)

# 행 선택 방법 3: iloc[]를 이용한 복수 행 선택
rows_1_3 = df.iloc[[1, 3]]
print(rows_1_3)

# 행 선택 방법 4: loc[]를 이용한 복수 행 선택
rows_2_4 = df.loc[[2, 4]]
print(rows_2_4)

sub_df = df.loc[df['age'] >= 30]
print(sub_df)

# 행 선택 방법 5: 슬라이싱을 이용한 범위 지정
rows_1_3 = df[1:4]
print(rows_1_3)

# 행 선택 방법 6: query()를 이용한 조건에 따른 행 선택
rows_age_over_30 = df.query('age > 30')
print(rows_age_over_30)
