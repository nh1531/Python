'''
사용자 정의 모듈을 작성하여 간단한 수학 연산을 수행해 보세요.
mymath.py라는 파일을 만들고, 이 파일에 사용자 정의 모듈을 작성하세요.
모듈에 다음 함수들을 구현하세요:
add(x, y): 두 숫자 x와 y를 더한 값을 반환합니다.
subtract(x, y): x에서 y를 뺀 값을 반환합니다.
multiply(x, y): x와 y를 곱한 값을 반환합니다.
divide(x, y): x를 y로 나눈 값을 반환합니다. 단, y가 0이면 "0으로 나눌 수 없습니다."라는 메시지를 출력합니다.
main.py라는 파일을 만들어 mymath 모듈을 임포트하고, 각 함수를 호출하여 결과를 출력하세요.
'''

def add(x,y):
    return x+y
def subtract(x, y):
    return x-y
def multiply(x, y):
    return x*y
def divide(x, y):
    if y==0:
        print("0으로 나눌 수 없습니다")
    else:
        return x/y
    