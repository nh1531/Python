# 초를 입력하면 분과 초로 표시하는 프로그램. 예를 들어, 200초를 입력하면 3분 20초로 표현하라
"""
sec = int(input("초를 입력하세요 :"))
time1 = sec//60
time2 = sec%60

print(f"{time1} 분 {time2} 초")
"""

# 분(min)을 입력 하면, 일, 시간, 분으로 출력하는 프로그램을 만들어라. (예 : 1550분은 1일 1시간 50분)
'''
min = int(input("분을 입력하세요: "))
day = min//(60*24)
hour = (min%(60*24))//60
min1 = (min%(60*24))%60

print(f"{day}일 {hour}시간 {min1}분")
'''
#hour = (min //60)%24
#min1 = min % 60

# 500만원을 년이율 5%로 복리 저금했을 때 5년 후의 원리금의 합계를 출력하는 프로그램
principal = 5000000
interest_rate = 0.05
years = 5
total_amout = principal * (1 + interest_rate ) ** years
print("5년 후 원리금 총액은", int(total_amount), "원")


# 1부터 n까지의 합은 n(n+1)/2로 주어진다. 1부터 100까지의 합을 구하여 출력하는 프로그램을 작성하고 실행하라.
n = 100
total = n*(n+1)//2
print(f"1부터 {n}까지의 합은 {total}")

# 판매자가 딸기와 포도를 판매하고 있다. 포도 한 알의 무게는 75g이고 딸기 한 알의 무게는 113.5g이다.
# 사용자로부터 포도 알의 개수와 딸기의 개수를 입력 받아 총 무게를 계산하여 출력하는 프로그램을 작성하고 실행하라.
gr = int(input("포도 알의 개수 : "))
st = int(input("딸기의 개수 : "))
result = """
총 무게 :
(75 * gr ) + (113.5 * st) = 
"""


