#
# sol.py
#
# 박유나
# 2021-12659

def answer_sum1():
    total = 0
    for n in range(1, 101):
        total += n
    return total

def answer_sum2():
    total = 0
    for n in range(11, 1001):
        total += n
    return total

def answer_sum3():
    total1 = 0
    total2 = 0
    for i in range(1, 51):
        total1 += i
    for i in range(51, 101):
        total2 += i
    total = total1 * total2 
    return total

def answer_sumlines():
    file = open("C:\Workspace\midterm\pp\sumlines.txt")
    total = 0
    for line in file:
        x = float(line)
        total += x
    file.close()
    return total
