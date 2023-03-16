'''
Deposit 클래스를 생성하라. 이 클래스는 세 개의 인스턴스 변수 initial과 interest, n을 갖는다.
initial은 원금을 의미하고 interest는 년 이자율을 나타낸다.
초기화 함수에서 세 개의 인스턴스 변수를 전달 받은 값으로 설정해야 한다.
인스턴스 메소드 profit()은 n년 후 원리금을 반환한다. n년 후 원리금은 initial * (1 + interest)n이다.
Deposit 클래스를 이용하여 100만원을 이율 3.5%로 7년간 저축했을 때 원리금을 구하는 프로그램을 작성하라.
단 원리금은 정수로 표시되어야 한다.

class Deposit:
    def __init__(self, initial, interest, n):
        self.initial = initial
        self.interest = interest
        self.n = n
    
    def profit(self):
        return int(self.initial * (1 + self.interest)**self.n)

x = Deposit(1000000, 0.035, 7)
print(x.profit())
'''

'''
예제의 Teacher 클래스에서 People 클래스의 __init__()를 호출하지 않고
부모 클래스의 age, name 인스턴스 변수를 이용할 수 있는가? 이용할 수 없다면 그 이유는?
이용할 수 있게 하려면 프로그램을 어떻게 수정해야 하는가?


class People :
    def __init__(self, age=0, name=None):
        self.__age = age
        self.__name = name

    def introMe(self):
        print("Name :", self.__name, "age :", str(self.__age))
        
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
        
class Teacher(People) :
    def __init__(self, age=0, name=None, school=None) :
        super().__init__(age, name)
        self.school = school

    def showSchool(self):
        print("My School is ", self.school)

t = Teacher(35, 'Kim', 'highschool')
t.introMe()
t.set_name('Lee')
t.introMe()
t.showSchool()
'''

'''
다음 Person 클래스를 상속 받는 Employee 클래스를 정의하라.
Employee 클래스에 employeeID 인스턴스 변수를 추가하고 getID() 메소드를 정의하라.
getID() 메소드는 employeeID를 반환하는 메소드이다.
Employee 클래스를 이용하여 Employee("동양", 65, 2019)로 생성된 객체의 이름, 나이, ID를 출력하라.

class Person:
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    def getName(self): 
        print(self.name) 

    def getAge(self): 
        print(self.age)
        
class Employee(Person):
    def __init__(self, name, age, employeeID):
        super().__init__(name,age)
        self.employeeID = employeeID
        
    def getID(self):
        return self.employeeID
    
emp = Employee("동양", 65, 2019)
print(f'ID:{emp.getID()}, 이름:{emp.getName()}')
'''

'''
문제: 학생 정보를 관리하는 프로그램을 만드세요.
학생(Student) 클래스
인스턴스 변수: 이름(name), 학번(student_id), 학년(year), 전공(major), 평균 성적(avg_score)
메서드: get_info() - 학생의 정보를 문자열로 반환

학생들을 관리하는 클래스(StudentManager)
인스턴스 변수: 학생들(student_list)
메서드:
add_student(student): 학생을 리스트에 추가하는 메서드
remove_student(student_id): 학번을 이용해 학생을 리스트에서 제거하는 메서드
find_student(student_id): 학번을 이용해 학생을 찾는 메서드
show_all_students(): 모든 학생의 정보를 출력하는 메서드
'''
class Student:
    def __init__(self, name, student_id, year, major, avg_score):
        self.name = name
        self.student_id = student_id
        self.year = year
        self.major = major
        self.avg_score = avg_score
    
    def get_info(self):
        return f"이름:{self.name}, 학번:{self.student_id}, 학년:{self.year}, 전공{self.major}, 평균 성적{self.avg_score}"

class StudentManager:
    def __init__(self):
        self.student_list = []
    
    def add_student(self, student):
        self.student_list.append(student)

    def remove_student(self, student_id):
        for student in self.student_list:
            if student.student_id == student_id:
                self.student_list.remove(student)
                return
        print(f'{student_id}학번을 가진 학생이 없습니다.')

    def find_student(self, student_id):
        for student in self.student_list:
            if student.student_id == student_id:
                print(f'{student_id}는 {student.name}학생입니다.')
                return
        print(f'{student_id}학번을 가진 학생이 없습니다.')
    
    def show_all_students(self):
        for student in self.student_list:
            print(student.get_info())
            
student_manager = StudentManager()
student1 = Student('홍길동', '20230001', 2, '컴퓨터공학', 80.5)
student2 = Student('김철수', '20230002', 1, '전자공학', 74.5)
student3 = Student('이영희', '20230003', 3, '건축공학', 92.5)

student_manager.add_student(student1)
student_manager.add_student(student2)
student_manager.add_student(student3)

#에
#student_manager.remove_student(student1)
#student_manager.find_student(student1)

student_manager.show_all_students()
    
    
    
'''
위 클래스들을 이용하여 다음과 같은 프로그램을 작성하세요.
학생 관리자(StudentManager)를 생성합니다.
학생(Student)을 생성합니다. 학생의 인스턴스 변수는 이름, 학번, 학년, 전공, 평균 성적을 포함합니다.
학생 관리자에 학생을 추가합니다.
학생 관리자에서 학생을 삭제합니다.
학생 관리자에서 학생을 찾습니다.
학생 관리자에서 모든 학생의 정보를 출력합니다.
'''

