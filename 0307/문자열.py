'''
string = "abcdefghij"

result = ""
for i in range(len(string)):
    if i % 2 == 1:
        result += string[i]

print(result)  # 출력값: "acegi"
'''

'''
문자열 슬라이싱
string[start:end:step]
step은 선택적이며, 추출하고자 하는 문자 사이의 간격
start, end, step은 모두 정수. 생략한다면, start는 0, end는 문자열의 길이, step은 1.

'''
# step 생략 : 1
# end-1 값 까지 출력 - 1:4까지
'''
string = "hello world"
substring = string[1:5]
print(substring)  # "ello"
'''

# 처음부터 끝까지 2씩 증가
'''
string = "hello world"
substring = string[::2]
print(substring)  # "hlowrd"
'''
# 처음부터 끝까지, 증감값 step -1
'''
s = "Hello, world!"
reversed_s = s[::-1]
print(reversed_s)  # "!dlrow ,olleH"
'''
# "문자열".upper() -> method
# 문자열 구성 파악 메소드 예시
'''
print("hello123".isalnum())  # True
print("123".isalpha())  # False
print("123".isdecimal())  # True
print("123".isdigit())  # True
print("hello".isidentifier())  # True
print("hello".islower())  # True
print("123".isnumeric())  # True
print("Hello, World!".isprintable())  # True
print("   ".isspace())  # True
print("\t".isspace())  # True
print("Hello, World!".istitle())  # True
print("HELLO".isupper())  # True
'''

# 문자열 대소문자 변환 함수 예시
'''
print("hello, world!".upper())  # "HELLO, WORLD!"
print("HeLLo, wOrLd!".lower())  # "hello, world!"
print("hello, world!".capitalize())  # "Hello, world!"
print("hello, world!".title())  # "Hello, World!"
print("Hello, World!".swapcase())  # "hELLO, wORLD!"
'''

# 문자열 찾기 함수 예시
'''
s = "hello, world!"

print(s.find("l"))  # 2
print(s.rfind("l"))  # 10
print(s.index("l"))  # 2
print(s.rindex("l"))  # 10
print(s.count("l"))  # 3
'''

# 문자열 공백 삭제 및 변경 함수 예시
'''
s = "  hello,   world!  "

print(s.strip())  # "hello,   world!"
print(s.lstrip())  # "hello,   world!  "
print(s.rstrip())  # "  hello,   world!"
print(s.replace("o", "0"))  # "  hell0,   w0rld!  "
print(s.replace("o", "0", 1))  # "  hell0,   world!  "
'''

# 문자열 분리, 결합 함수
'''
string = "hello world"
string_list = string.split()  # 기본값인 공백을 구분자로 사용
print(string_list)  # ['hello', 'world']

string = "apple,banana,grape"
string_list = string.split(",")  # 쉼표를 구분자로 사용
print(string_list)  # ['apple', 'banana', 'grape']

s = "apple,banana,grape"

print("apple\nbanana\rgrape".splitlines())  # ["apple", "banana", "grape"]
print(",".join(["apple", "banana", "grape"]))  # "apple,banana,grape"
'''

# 문자열 정렬, 채우기 함수 예시
s = "hello"

print(s.center(10))  # "  hello   "
print(s.center(10, "-"))  # "--hello---"
print(s.ljust(10))  # "hello     "
print(s.ljust(10, "*"))  # "hello*****"
print(s.rjust(10))  # "     hello"
print(s.rjust(10, "+"))  # "+++++hello"
print("123".zfill(5))  # "00123"



