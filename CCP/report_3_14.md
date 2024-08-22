#산술연산자
'''
3 + 4 #덧셈
17 - 9 #뺄셈
8 * 9 #곱셈
8 ** 2 #제곱
3 / 2 #나눗셈
8 // 5 #몫
7 % 2 #나머지
''''

#연습
'''
7 + 4 * 3
13 - 19 / (5+6)
5 + (5 * (2 + 1/2) - 7) / 3
''''

#수학 모듈
#라이브러리 - 패키지 - 모듈
'''
import math # 모듈이용하기 위해서는 import 명령 필요
math.sqrt(2)
math.log(3)
'''

#소스코드 파일 작성하기
# Hashbang : #!로 시작, 해당 스크립트를 실행시키는 데 필요한 인터프리터의 경로 명시

#자료형과 변수
#int(정수), float(소수), str(문자열)
x = 8 + 5 #변수 
t = [0, 1, 2, 3, 4, 5] #list
d = {'a' : 1, 'b' : 2, 'C' : 3} #dict

#함수
def add(x, y ):
    return x + y

x = 3
y = 4
s = add(x, y)
print(s)

#연습
def cels2fahr(x):
    fahr = (9/5)*x +32
    return fahr

def  fahr2cels(x):
    cels = 5/9*(x-32)
    return cels

#조건문
def f(x):
    if x> 0 : 
        return 1
    else : 
        return 0

#반복문
temperatures = [13.8, 15.7, 17.0, 18.1, 18.5]
for i in temperatures:
    print(i)

#연습
for i in temperatures:
    cels2fahr(i)
    