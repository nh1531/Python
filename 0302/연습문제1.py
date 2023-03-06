# cm 변환
'''
num = int(input("cm를 입력하세요 : "))
if num < 0:
    print("잘못 입력하였습니다.")
if num > 0:
    print(f"{num/2.54:.2f} 인치 입니다.")
''' 

# 학점
'''
score = int(input("학점을 입력하세요 : "))
if score < 40:
    print("1학년입니다.")
if 40 <= score < 80:
    print("2학년입니다.")
if score >= 80:
    print("졸업반입니다.")
'''

# 시간
hour = int(input("현재 시간을 1~12 사이의 숫자로 입력하세요: ")) 
hour1 = input("am 또는 pm을 입력하세요 : ")
hour2 = int(input("경과 시간을 입력하세요 : "))

if hour <= 12
    if ((hour+hour1+hour2) % 12) <= 0 :
        print("am")
    else :
        print("pm")
    

# 사용자로부터 현재 시간, 오전/오후, 경과 시간 입력받기
hour = int(input("현재 시간을 1~12 사이의 숫자로 입력하세요: "))
am_pm = input("오전(am) 또는 오후(pm)를 입력하세요: ")
elapsed_time = int(input("경과 시간을 입력하세요: "))

# 입력받은 시간 정보에 따라 최종 시간 계산하기
if am_pm == "pm":
    hour += 12
hour = (hour + elapsed_time) % 24
if hour == 0:
    hour = 12

# 최종 시간 출력하기
if hour <= 12:
    am_pm = "am"
    if hour == 0:
        hour = 12
else:
    am_pm = "pm"
    hour -= 12
print("최종 시간은 {} {}입니다.".format(hour, am_pm))

##
time = 
apm = int

overtime = int(intput())
new_time = time + (overtime %24)