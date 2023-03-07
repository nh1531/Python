#문자열의 문자수를 출력하라
s="Hello world"
print(len(s))

#문자열을 10번 반복한 문자열을 출력하라
s="A"
s1 = s * 10
print(s1)

#문자열의 첫 번째 문자를 출력하라
s="Hello world"
print(s[0])

#문자열에서 처음 3문자를 출력하라
s="Hello world"
print(s[:3])

#문자열에서 마지막 3문자를 출력하라
s="Hello world"
print(s[-3:])

#문자열의 문자를 거꾸로 출력하라
s="Hello world"
print(s[::-1])

#문자열에 7번째 문자가 있으면 출력하고 없으면 '문자가 없습니다'라는 메시지를 출력하라
s="Hello world"
if len(s) >= 7:
    print(s[6])
else:
    print("문자가 없습니다")

#문자열에서 첫 번째 문자와 마지막 문자를 제거한 문자열을 출력하라
# 첫번째 문자 : 0 , 마지막 문자 : -1, end-1=-2
s="Hello world"
print(s[1:-1])

#문자를 모두 대문자로 변경하여 출력하라
s="Hello world"
print(s.upper())

#문자를 모두 소문자로 변경하여 출력하라
s="Hello world"
print(s.lower())

#문자열에서 'a'를 'e'로 대체하여 출력하라
s="apple"
print(s.replace('a','e'))

'''
문자 'a'가 들어가는 단어를 키보드에서 입력 받아 첫 번째 줄에는 'a'까지의 문자열을 출력하고
두 번째 줄에는 나머지 문자열을 출력하는 프로그램을 작성하라.
'''
'''
string = input("'a'가 들어가는 단어를 입력하세요 : ")
index_a = string.find('a')

if index_a != -1:
    #문자 'a'가 존재하면, 문자열을 분리하여 출력
    print(string[:index_a+1])
    print(string[index_a+1:])
else:
    #문자 'a'가 존재하지 않으면, 문자열을 그대로 출력
    print(string)
    
# a 가 여러개 있는 경우
s = "dkfjkadfjayyd"
print(s.replace('a','a\n'))
'''

'''
숫자를 문자열로 변화하는 방법은 str(num)을 이용한다.
str(12) -> '12'가 된다. 반대로 문자열을 숫자로 변환하려면 int(string)을 이용한다.
int('12') -> 12가 된다. 이를 이용하여 1부터 1000까지의 숫자의 각 자리수의 합을 모두 구하라.
예를 들어 234 -> 2+3+4=9가 된다

[Hint]
sum = 0
for s in '234':
sum += int(s)
'''

total = 0

for num in range(1,1001):
    #각 자리수의 합을 구함
    digits_sum = 0
    for digit in str(num):
        digits_sum += int(digit)
        
    #전체 합에 더함
    total += digits_sum
    
print(total)


