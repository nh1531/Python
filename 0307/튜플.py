#튜플(tuple)은 여러 개의 값을 담을 수 있는 데이터 타입 중 하나로,
#리스트와 비슷하지만 수정할 수 없는(immutable) 특징을 가지고 있습니다.

# 소괄호 없이도 생성 가능
t = 1, 2, 3
print(t)  # (1, 2, 3)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# 튜플 이어붙이기
tuple3 = tuple1 + tuple2
print(tuple3)  # (1, 2, 3, 4, 5, 6)

# 튜플 반복하기
tuple4 = tuple1 * 3
print(tuple4)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# 튜플 언패킹
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # 1
print(b)  # 2
print(c)  # 3

#튜플 언패킹을 이용하면 두 변수의 값을 쉽게 교환할 수 있습니다
x = 1
y = 2
x, y = y, x
print(x)  # 2
print(y)  # 1

# 튜플을 리스트로 변환
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print(my_list)

# 리스트를 튜플로 변환
my_list = [6, 7, 8, 9, 10]
my_tuple = tuple(my_list)
print(my_tuple)

#리스트 안에 요소가 변경 가능한 객체인 경우, 튜플로 변환하더라도 요소 값이 변경될 수 있다는 점입니다.
#예를 들어, 다음과 같은 리스트를 튜플로 변환하면 튜플의 요소 값이 변경될 수 있습니다.
my_list = [1, 2, [3, 4]]
my_tuple = tuple(my_list)
print(my_tuple) # 출력 결과: (1, 2, [3, 4])

my_tuple[2][0] = 5
print(my_tuple) # 출력 결과: (1, 2, [5, 4])


