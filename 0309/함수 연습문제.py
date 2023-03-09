'''
#1~n까지의 합을 계산하는 함수
def sum_(n):
    tot = 0
    for i in range(1,n+1):
        tot += i
    return tot

print(sum_(10))

#반지름을 전달하면 원의 면적을 반환하는 cir_area(r) 함수와 원의 둘레를 반환하는 cir_cirm(r) 함수를 작성하라.
#이들 함수를 이용하여 반지름이 3.5cm인 원의 면적과 둘레를 소수점 아래 첫 자리까지 구하라.
def cir_area(r):
    return 3.14*r**2
def cir_cirm(r):
    return 2*3.14*r

print(round(cir_area(3.5),1)) #round() 반올림
print(round(cir_cirm(3.5),1))


#den(n) 함수를 이용하여 약수를 구하여 반환하는 프로그램을 작성
#12 -> [1, 2, 3, 4, 6, 12]
def den(n):
    cd = []
    for i in range(1,n+1):
        if n%i == 0:
            cd.append(i)
    return cd
print(den(12))

# 지역 변수와 전역 변수
x = 'global'

def my_function():
    # global x # 함수 안에 있지만 전역변수화 됨. 전역변수 값 수정 가능
    x = 'local' # 지역변수. 함수 내에서만 사용됨. 밖의 전역변수와 다른 변수임.

my_function()
print(x)

#두 개의 매개변수 n, m을 전달받아 m x n개의 * 상자를 출력하는 프로그램을 함수로 작성
#예: 2, 4 -> ****
#            ****
def box():
    pass

#하나의 숫자를 전달받아 숫자의 자리 합을 구하는 함수를 작성
#예: 123 -> 1+2+3 = 6
number = input("number : ")
#def sum_():
    for num in number:
        print(num)
'''    

#두 개의 문자열이 서로 다른 처음 위치를 반환하는 함수를 작성. 두 개의 문자열이 같으면 -1을 반환

#문자열과 하나의 문자를 전달받아 문자열에서 문자의 위치를 모두 찾아 리스트로 반환하는 함수를 작성

#재귀 함수를 이용하여 1부터 100까지의 합을 계산하는 프로그램
def sum_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_n(n-1)
print(sum_n(100))

'''
# 내부 함수를 이용하여 간단한 계산기 함수를 구현한 예제
def calculator():
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        return a / b

    return add, subtract, multiply, divide # 튜플임, 소괄호 없어도 됨

add, subtract, multiply, divide = calculator()

print(add(10, 20))  # 출력결과: 30
print(subtract(10, 20))  # 출력결과: -10
print(multiply(10, 20))  # 출력결과: 200
print(divide(10, 20))  # 출력결과: 0.5

# 함수 내 변수 참조 순서
# Local -> Enclosing -> Global -> Built-in
x = 'global'

def outer():
    x = 'outer'
    
    def inner():
        x = 'inner'
        print('x in inner:', x)
    
    inner()
    print('x in outer:', x)

outer()
print('x in global:', x)
'''