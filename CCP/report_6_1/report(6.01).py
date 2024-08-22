# report(6.01.py)
#
# 자습보고서입니다. 언어학과 2021-12659, 박유나에 의해 작성되었습니다.
#

# 예제 6.1

class Employee:
    def __init__(self, name, age):
        self.name = name # 우변과 괄호의 변수는 같아야함
        self.age = age

john = Employee("john", 25)


# 예제 6.2

john.name
john.age

# 예제 6.3

class Employee:
    def __init__(self, name, rate, hours, age):
        self.name = name
        self.rate = rate
        self.hours = hours
        self.age = age

file = open('emp.dat')

employees = []
for line in file:
    (name, rate, hours, age) = line.strip().split('\t')
    print(name)
    e = Employee(name, float(rate), float(hours), int(age))
    employees.append(e)

for e in employees:
    print(e.name, e.rate, e.hours. e.age)

for e in employees:
    print(e.name, e.rate * e.hours. e.age)
