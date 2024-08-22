#
# sol.py
#
# 실습04 컴퓨터의 개념 및 실습 수업용 파일입니다.
# 언어학과, 2021-12659 박유나가 작성하였습니다.

def answer01():
    total = 0
    for n in range(1, 31):
        x = 1 / n
        total += x
    return total

def answer02():
    total = 0
    for i in range(1, 31):
        for j in range(1, 51):
            x = j/i
            total += x
    return total

def answer03():
    total = 0
    for k in range(0, 100):
        total += 1/100 * (k/100)**2
    return total
