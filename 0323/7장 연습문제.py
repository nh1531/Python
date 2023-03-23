'''
data = {"Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6} 이 주어질 때
try-except문을 이용하여 다음과 같이 동작하는 프로그램을 작성하라.
사용자로부터 문자열을 입력 받는다
문자열이 data의 key와 같으면 value를 출력하고 다시 문자열을 입력 받는다
문자열 에 해당하는 key가 없으면 "항목이 없습니다"라는 메시지를 출력하고 종료한다.
'''
data = {"Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6}

'''
while True:
    try:
        user_input = input("Enter a day of week : ")
        value = data[user_input]
        print(value)
    except:
        print("항목이 없습니다.")
        break
'''
# 딕셔너리 .get() 해당되는 key값으로 조회, 반환값이 없을 때는 None이 나옴
while True:
    try:
        user_input = input("Enter a day of week : ")
        value = data.get(user_input,None)
        if value is not None:
            print(value)
        else:
            print("항목이 없습니다.")
            break
    except Exception as e:
        print(f"An error occurred: {e}")

        