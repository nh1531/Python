# set
# 중복 허용x
# 1부터 45까지의 수 중에서 6개를 선택하여 로또 번호를 만드는 프로그램
'''
import random
pick = set() # 비어있는 set

while len(pick) < 6:
    pick.add(random.randint(1,45))
print(sorted(pick))
'''
# 학생들의 성적을 딕셔너리로 저장하고, 성적 평균을 계산하는 프로그램을 작성해보세요.
grades = {
    "Alice": [85, 90, 95],
    "Bob": [75, 80, 85],
    "Charlie": [95, 95, 95]
}
'''
결과
Average grades:
Alice: 90.0
Bob: 80.0
Charlie: 95.0

# items() key,value 값이 튜플로 생성. 각각 값을 따로 다룰 수 있음
# len() 원소의 개수
for name, grade_list in grades.items():
    print(name, sum(grade_list) / len(grade_list))
    
# 숫자들이 들어있는 리스트에서 중복된 숫자를 제거하고, 남은 숫자들의 합을 계산하는 프로그램을 작성해보세요.
list = [1, 2, 2, 3, 3, 3, 4, 4, 5]
#Sum of unique numbers: 15
print(sum(set(list)))

x = set([1, 2, 2, 3, 3, 3, 4, 4, 5])
print(sum(x))
'''
# 주어진 문자열에서 각 알파벳의 빈도수를 구하는 프로그램을 작성하시오.
text = "Hello, world!"
#결과값
#{'H': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}
'''
for char in text: # 하나씩 분리
    print(char)
'''
freq_dict={}
for char in text:
    if char not in freq_dict:
        freq_dict[char] = 1
    else:
        #freq_dict[char] = freq_dict[char] + 1
        freq_dict[char] += 1 
print(freq_dict)
# isalpha() : 문자열이 알파벳으로만 이루어졌는지 여부를 반환

#두 개의 리스트가 주어졌을 때, 두 리스트에 공통으로 포함된 요소를 모두 담은 리스트를 반환하는 프로그램을 작성하시오.
#리스트A: 임의의 길이와 요소를 가진 리스트
#리스트B: 임의의 길이와 요소를 가진 리스트
list1 = set([1, 2, 3, 4, 5])
list2 = set([2, 4, 6, 8, 10])

# 공통된 요소인 2와 4를 모두 포함한 리스트를 반환한다.
# 결과값
# [2, 4]
print(list(list1 & list2))

'''
sorted 함수의 key 인자를 이용하면 정렬 기준을 커스터마이징할 수 있습니다.
key 인자는 정렬에 사용될 함수를 지정하는 인자로, 이 함수의 반환값을 기준으로 리스트를 정렬합니다.
fruits = ['apple', 'banana', 'cherry', 'date']

# 길이 기준으로 정렬
sorted_fruits = sorted(fruits, key=len)
print(sorted_fruits)
# 출력 결과: ['date', 'apple', 'banana', 'cherry']
'''
