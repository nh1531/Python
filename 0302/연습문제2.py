# 기본값 print() = print("", end="\n") -> 기본적으로 개행이 됨
# 중첩반복문
'''
for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end="")
    print()

for i in range(4, 0, -1):
    for j in range(1, i+1):
        print("*", end="")
    print()
'''

#3의 배수와 5의 배수의 합
'''
n = int(input("양의 정수를 입력하세요 :"))
if n => 1:
    if n%3 == 0:
     for i in range(1, n+1):
        print(i)
    if n%5 == 0:
     for j in range(1, n+1):
        print(j)
'''
"""
n = int(input("양의 정수를 입력하세요 :"))
sum = 0
for i in range(1, n+1):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
        
output = f"\n[결과]\n 부터 {n}까지의 자연수 중에서 3의 배수와 5의 배수의 합 : {sum}"
print(output)
"""

#최댓값과 최솟값 찾기
'''
n1 = int(intput("1번째 숫자를 입력하세요 :"))
n2 = int(intput("2번째 숫자를 입력하세요 :"))
n3 = int(intput("3번째 숫자를 입력하세요 :"))
n4 = int(intput("4번째 숫자를 입력하세요 :"))
n5 = int(intput("5번째 숫자를 입력하세요 :"))

min = 100
max = 1

if n1<min:
    
    
output = f"\n입력받은 숫자들 : "
print(output)
'''

"""
max_num = 0
min_num = 100

for i in range(5):
    num = int(input(f"{i+1}번째 숫자를 입력하세요 : "))

    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

output = f"입력받은 숫자들 : {[max_num, min_num]}\n 최댓값:{max_num}\n 최솟값:{min_num}"
print(output)
"""
# 숫자의 합이 100보다 작을 때까지 입력받기
# 반복횟수 정해지지 않았을 때 while
'''
sum = 0
while sum < 100:
    num = int(input(f"숫자를 입력하세요 : "))
    sum += num
output = f"입력받은 숫자들의 합 : {sum}"
print(output)
'''

# 피보나치 수열
'''
n = int(input("몇 번째 항을 출력할까요? (1 이상의 양의 정수) :"))

if n == 1 or n == 2:
    result = 1
else:
    a,b = 1,1
    i = 3
    while i <= n:
        result = a + b
        a = b
        b = result
        i += 1
output = f"피보나치 수열의 {n}번째 항은 {result}입니다."
print(output)
'''
        
# 주사위 게임
'''
import random

while True:
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    sum = d1 + d2
    print(f"주사위1 : {d1}, 주사위2 : {d2}, 합 : {sum}")

    if sum == 7:
        print("이김")
        break
    else:
        print("짐")
'''
# 동전 게임 프로그램
'''
from random import randint
mon = 50

while True:
    coin = randint(1,2)
    guess = int(input("앞면(1) 또는 뒷면(2)을 선택하세요 : "))
   
    if coin == guess:
        mon = mon + 9
        
        print(f"동전:{coin}, 선택:{guess}, 결과:{mon}")
    else :
        mon = mon - 10
        print(f"동전:{coin}, 선택:{guess}, 결과:{mon}")
    
    if mon <= 0 or mon >= 100:
        break

'''
#최대 공약수
'''
n1 = int(input("숫자 1 : "))
n2 = int(input("숫자 2 : "))

if n1 > n2:
    max = n1
    min = n2
else:
    max = n2
    min = n1

rem = 1
while rem != 0:
    rem = max % min 
    max = min
    min = rem

print("최대 공약수는", max, "입니다")
'''
    
        
        
        


