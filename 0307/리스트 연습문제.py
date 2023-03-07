'''
#3명 이상 친구 이름 리스트를 작성하고 다음 내용을 프로그램하시오 
list = ['김','이','박']

#insert()로 맨 앞에 새로운 친구 추가
list.insert(0,'강')
print(list)

#insert()로 3번째 위치에 새로운 친구 추가
list.insert(2,'고')
print(list)

#append()로 마지막에 친구 추가
list.append('백')
print(list)
'''

'''
#리스트 [1, 2, 3]에 대해 다음과 같은 처리를 하라.
#두 번째 요소를 17로 수정
list = [1, 2, 3]
list[1] = 17
print(list)

# 리스트에 4, 5, 6을 추가
list += [4,5,6]
print(list)

#첫 번째 요소 제거
removed_item = list.pop(0)
print(list)

del list[0]
print(list)

# 리스트를 요소 순서대로 배열하기
list.sort()
print(list)

#인덱스 3에 25넣기
list.insert(3, 25)
print(list)
'''

'''
reversed()는 이터러블 객체를 역순으로 순회할 수 있는 이터레이터(iterator)를 반환하는 함수입니다.
따라서 reversed()를 호출한 리스트 자체는 변경되지 않습니다.
reversed()의 반환값 : 이터레이터
list 형태로 보려면 list()로 형변환 필요함

nums = [1, 2, 3, 4, 5]
reversed_nums = list(reversed(nums))
print(reversed_nums)  # [5, 4, 3, 2, 1]
'''
'''
#for 루프를 이용하여 다음과 같은 리스트를 생성하라.
#0~49까지의 수로 구성되는 리스트
list = [num for num in range(0,50)]
print(list)

a_list=[]
for i in range(0,50):
    a_list.append(i)
print(a_list)

#1~50까지 수의 제곱으로 구성되는 리스트
list = [num for num in range(1,51)]
list1 = [num * num for num in list]
print(list1)

a_list=[]
for i in range(1,51):
    a_list.append(i**2)
print(a_list)

#크기가 같은 두 개의 리스트 L, M을 생성하고 두 리스트의 각 요소 합으로 구성되는 새로운 리스트를 생성하라.
#예를 들어 L=[1,2,3]이고 M=[4,5,6]이면 [5,7,9]인 리스트 생성
L = [1,2,3]
M = [4,5,6]
N = []
for i in range(0,len(L)):
    N.append(L[i] + M[i])
print(N)

N = [L[i] + M[i] for i in range(0,len(L))]
print(N)
'''
#사용자로부터 5개의 숫자를 문자열로 입력 받아 각 숫자를 +로 연결한 문자열을 생성하라.
#예를 들어 2, 5, 11, 33, 55를 입력하면 '2+5+11+33+55'를 생성하라.

num_list = input("5개의 숫자를 입력하세요. (구분자 : 띄어쓰기) ").split()
result = "+".join(num_list)
print(result)

