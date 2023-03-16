'''
enumerate() 내장 함수를 이용하여 사용자가 입력한 문자열에서 'a' 문자의 위치를 모두 찾아 출력하는 프로그램을 작성하라.
'a'가 없으면 "a가 없습니다'라는 메시지를 출력하라.


msg = input("message:")

flag = 0

for i, ch in enumerate(msg):
    if ch=='a':
        print(i)
        flag = 1

if flag==0:
    print("a가 없습니다.")
'''

'''
두 수의 합(sum), 차(sub), 곱(mul), 나누기(div)를 수행하는 함수를 각각 정의하라.
딕셔너리를 이용하여 사용자가 '1'을 입력하면 sum()을 호출하고, '2'를 입력하면 sub(),
'3'을 입력하면 mul(), '4'를 입력하면 div() 함수를 호출하여 두 수의 연산을 수행하는 프로그램을 작성하라.

def sum(n, m):
    return n+m
def sub(n, m):
    return n-m

table = {'1':sum, '2':sub}

func = table['1']
print(func(2,3))
'''

'''
다음과 같이 구성되는 문자열을 구분 문자(&, =)로 분리하여 딕셔너리로 반환하는 함수 작성
예: 문자열 'led=on&motor=off&switch=off'이고 구분 문자가 '&',
'='일 때 {'led':'on', 'motor':'off', 'switch':off'} 반환.
Hint: dict([['a','b'], ['c', 'd']]) -> {'a': 'b', 'c': 'd'}
'''
#split() 문자열의 method
def query_parse(query):
    a = query.split("&")
    #print(a)

    temp = [] # 빈 list

    for item in a:
        temp.append(item.split('='))

    return dict(temp)
    
print(query_parse('led=on&motor=off&switch=off'))
