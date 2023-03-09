days = {'January':31, 'February':28, 'March':31, 'April':30,
        'May':31, 'June':30, 'July':31, 'August':31,'September':30, 'October':31, 'November':30, 'December':31}
#사용자가 월을 입력하면 해당 월에 일수를 출력하라
'''
mon = input("월을 입력하세요 : ")
print(days[mon.title()]) # title() 첫번째 문자 대문자로 바꿈

#알파벳 순서로 모든 월을 출력하라
key_list = list(days.keys())
print(sorted(key_list))

#일수가 31인 월을 모두 출력하라
for x in days:
    if days[x] == 31:
        print(x)

# key값 출력
for x in days:
    print(x)

#월의 일수를 기준으로 오름차순으로 (key-value) 쌍을 출력하라
# values-key 위치 변경, 일수 기준으로 정렬, 다시 현재 key와 values 순으로  정렬
# 리스트 컴프리헨션
days_item = days.items() # list로 변경되어 정렬 가능
days_item = [(day, month) for (month, day) in days_item] # 현재: month,day -> 변경 후 day,month
days_item.sort()
#print(days_item)
#print(sorted(days_item)) # sorted() 정렬. 튜플에서 앞에 있는 값을 기준으로 정렬
days_item = [(month, day) for (day, month) in days_item]
print(days_item)

#사용자가 월을 3자리만 입력하면 월의 일수를 출력하라.(Jan, Feb 등)
month = input("month : ")

for x in days:
    if x[0:3] == month.title():
        print(days[x])
'''        
#다음 딕셔너리에 대해 물음에 답하라.
# list 안에 딕셔너리 구조
d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
   {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
   {'name':'Princess', 'phone':'555-3141', 'email':''},
   {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

#전화번호가 8로 끝나는 사용자 이름을 출력하라
#문자열은 인덱싱 가능
'''
for people in d:
    if people ['phone'][7] == '8':
        print(people['name'])
        
#이메일이 없는 사용자 이름을 출력하라
for people in d:
    if people ['email'] == '':
        print(people['name'])
'''        
#사용자 이름을 입력하면 전화번호, 이메일을 출력하라. 이름이 없으면 '이름이 없습니다'라는 메시지를 출력하라
s_name = input("name to search : ")
flag = 1
for people in d:
    if people['name'] == s_name.title():
        print(people['phone'],people['email'])
        flag = 0
if flag == 1:
    print("없는 사람입니다.")