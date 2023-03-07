# 리스트
# 리스트는 대괄호 [ ] 내에 쉼표(,)로 구분된 요소들을 담을 수 있습니다. 리스트는 수정 가능하며, 순서도 유지됨
# 정수와 실수가 포함된 리스트
'''
mixed_list = [1, 2.5, 3, 4.2, 5]

# 문자열과 불리언 값이 포함된 리스트
string_bool_list = ['hello', True, 'world', False]

# 리스트와 튜플이 포함된 리스트
list_tuple_list = [[1, 2, 3], (4, 5, 6), [7, 8, 9]]

# 리스트와 딕셔너리가 포함된 리스트
list_dict_list = [[1, 2, 3], {'a': 4, 'b': 5, 'c': 6}, [7, 8, 9]]

# 리스트와 집합이 포함된 리스트
list_set_list = [[1, 2, 3], {4, 5, 6}, [7, 8, 9]]

# 리스트 컴프리헨션(List Comprehension)
# [표현식 for 항목 in 반복가능객체 if 조건문]

#1부터 10까지의 숫자 중에서 짝수만 포함하는 리스트를 생성
even_numbers = [num for num in range(1, 11) if num % 2 == 0]
print(even_numbers)  # 출력: [2, 4, 6, 8, 10]

#리스트 내 모든 요소에 1을 더하는 예제
original_list = [1, 2, 3, 4, 5]
new_list = [num + 1 for num in original_list]
print(new_list)  # [2, 3, 4, 5, 6]

#리스트 내 문자열의 길이를 구하는 예제
words = ['apple', 'banana', 'cherry', 'durian']
word_lengths = [len(word) for word in words]
print(word_lengths)  # [5, 6, 6, 6]

#문자열 리스트에서 길이가 5 이상인 문자열만 대문자로 바꾸기
words = ["apple", "banana", "orange", "grape", "watermelon"]
result = [word.upper() for word in words if len(word) >= 5]
print(result)  # ['BANANA', 'ORANGE', 'WATERMELON']

#리스트 내 중첩된 요소들을 단일 리스트로 만드는 예제
original_list = [[1, 2], [3, 4], [5, 6]]
new_list = [num for sublist in original_list for num in sublist]
print(new_list)  # [1, 2, 3, 4, 5, 6]

#주어진 이차원 리스트에서 짝수만 리스트로 생성하기
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [num for row in matrix for num in row if num % 2 == 0]
print(result)  # [2, 4, 6, 8]
'''

# remove() 메서드를 이용하여 요소 제거하기
# 리스트에서 특정 요소를 찾아 제거
my_list = [1, 2, 3, 4]
my_list.remove(3)
print(my_list) # 출력 결과: [1, 2, 4]

# pop() 메서드를 이용하여 요소 제거하기
# 리스트에서 마지막 요소를 제거할 수 있음. 인덱스를 지정하여 특정 위치의 요소를 제거할 수도 있음

my_list = [1, 2, 3, 4]
my_list.pop()
print(my_list) # 출력 결과: [1, 2, 3]

my_list = [1, 2, 3, 4, 5]
removed_item = my_list.pop(2)
print(my_list) # 출력 결과: [1, 2, 4, 5]
print(removed_item) # 출력 결과: 3



# reverse -> list의 메소드 
# reversed() -> 내장함수

