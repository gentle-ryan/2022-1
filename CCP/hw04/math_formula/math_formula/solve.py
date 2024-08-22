# solve.py
# 과제04 컴퓨터의 개념 및 실습 수업용 파일입니다.
# 언어학과, 2021-12659 박유나가 작성하였습니다.
 
from physics import force
from finance import fv

#calculate prob01
def answer01():
    earth_to_moon = force(5.97 * (10 ** 24), 7.3 * (10 ** 22), 3.84 * (10 ** 8))
    return earth_to_moon

#calculate prob02
def answer02():
    earth_to_apple = force(240 * 0.001, 5.97 * (10 ** 24), 64 * (10 ** 5))
    return earth_to_apple

#calculate prob03
def answer03():
    month = fv(0.025/12, 5 * 12, 10000000)
    year = fv(0.025, 5, 10000000)
    difference = month - year
    return difference

