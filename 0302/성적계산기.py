# 성적 계산기
kor = int(input("국어 성적을 입력하세요: "))
eng = int(input("영어 성적을 입력하세요: "))
math = int(input("수학 성적을 입력하세요: "))

avg_kor = kor
avg_eng = eng
avg_math = math
avg_total = (kor * 0.4 + eng * 0.4 + math * 0.2)

# 평균 점수 소수점 둘째자리까지 출력하기
print("국어 평균 점수: {:.2f}".format(avg_kor))
print("영어 평균 점수: {:.2f}".format(avg_eng))
print("수학 평균 점수: {:.2f}".format(avg_math))
print("총 평균 점수: {:.2f}".format(avg_total))

# 학점 출력하기
if avg_total >= 90:
    print("학점: A")
elif avg_total >= 80:
    print("학점: B")
elif avg_total >= 70:
    print("학점: C")
elif avg_total >= 60:
    print("학점: D")
else:
    print("학점: F")



