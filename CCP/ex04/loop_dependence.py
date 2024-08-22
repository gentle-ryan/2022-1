#
# loop_dependence.py
#
# 실습 04 컴퓨터의 개념 및 실습 수업용 파일입니다.
# 언어학과 2021-12659 박유나에 의해 작성되었습니다.
#

# 1. Accumulation
#  
# Generate a sequence a[0], a[1], ..., a[n] 
# where a[0] = 0 and a[k+1] = a[k] + k for k = 1, ..., n
#

def accu(n):
    a = [0]
    for i in range(n):
        aknew = a[i] + i
        a.append(aknew)

    return a


# 2. Fibonacci Sequence
#
# Generate a sequence a[0], a[1], ..., a[n] 
# where a[0] = 0, a[1] = 1, and 
# a[k+2] = a[k+1] + a[k] for k = 1, ..., n
#

def fibonacci(n):
    if n == 0:
        return [0]
    else:
        fibo = [0, 1]
        for i in range(n-1):
            fibonew = fibo[i + 1] + fibo[i]
            fibo.append(fibonew)
        
    return fibo
    

# 3. Random Walk
#
# y[0] = 0
# y[i+1] = y[i] + e[i+1]
# e ~ random.gauss(mu=0, sigma=1)  
#
import matplotlib.pyplot
import random

r = 500
n = [0]
y = [0]

for i in range(r):
    n.append(i+1)
    err = random.gauss(mu=0, sigma=1)
    ynew = y[i] + err
    y.append(ynew)

matplotlib.pyplot.plot(n, y)
matplotlib.pyplot.show()

# 4. Two-Dimensional Random Walk
#
# x[0] = 0 
# y[0] = 0
# x[i+1] = x[i] + e1[i+1]
# y[i+1] = y[i] + e2[i+1]
# e ~ random.gauss(mu=0, sigma=1)
r = 500
x = [0]
y = [0]

for i in range(r):
    e1 = random.gauss(mu=0, sigma=1)
    e2 = random.gauss(0, 1)
    xnew = x[i] + e1
    ynew = y[i] + e2
    x.append(xnew)
    y.append(ynew)

matplotlib.pyplot.plot(x, y)
matplotlib.pyplot.show()

# 5. Two-Dimensional Random Walk On Lattice
#
# x[0] = 0
# y[0] = 0
#
# with probability 0.5 : 
#  x[i+1] = x[i] + random.choice([-1, 0, 1])
#  y[i+1] = y[i]
# with probability 0.5 :
#  x[i+1] = x[i]
#  y[i+1] = y[i]  + random.choice([-1, 0, 1])
#
r = 500
x = [0]
y = [0]

for i in range(r):
    if random.random() < 0.5:
        xnew = x[i] + random.choice([-1, 0, 1])
        ynew = y[i]
    
    else:
        xnew = x[i]
        ynew = y[i]  + random.choice([-1, 0, 1])
    
    x.append(xnew)
    y.append(ynew)

matplotlib.pyplot.plot(x, y)
matplotlib.pyplot.show()

