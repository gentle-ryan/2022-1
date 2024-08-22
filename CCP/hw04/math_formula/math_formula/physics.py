# physics.py
# 과제04 컴퓨터의 개념 및 실습 수업용 파일입니다.
# 언어학과, 2021-12659 박유나가 작성하였습니다.
#
# mass1 : mass of the object 1 (unit: kg)
# mass2 : mass of the object 2 (unit: kg)
# distance : distance between the centers (unit: m)
#
#function of calculating gravity
def force(mass1, mass2, distance):
    G = 6.67408 * (10 ** (-11))
    force = G * (mass1 * mass2) / distance ** 2
    return force
