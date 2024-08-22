#
# scientific_computing.py
#
# 실습05 컴퓨터의 개념 및 실습 수업용 파일입니다.
# 언어학과 2021-12659, 박유나에 의해 작성되었습니다.
#

#
# sqrt.py
#
# Compute the sqare root of a number using the Netwon Method
#

# compute sqrt (2)
# find x such that x**2 = 2
#
# x[n+1] = x[n] - (x[n] ** 2 - 2) / (2 * x[n])
# x1 = x0 - (x0 ** 2 - 2) / (2 * x0)

from lib2to3.pgen2.token import PLUS


n = 100
x0 = 1
for i in range(n):
    x1 = x0 - (x0**2 - 2) / (2 * x0)
    if abs(x1 - x0) < 1e-15:
        break

    print(x1)
    x0 = x1

# compute sqrt(y)
# find x such that x**2 = y 
#
# x[n+1] = x[n] - (x[n] ** 2 - y) / (2 * x[n])
#
# x1 = x0 - (x0 ** 2 - y) / (2*x0)
#    = x0 - x0/2 + y / (2*x0)
#    = (x0 + y/x0) / 2

def sqrt(y):
    n = 50
    x0 = 1
    for i in range(n):
        x1 = (x0 + y/x0) / 2
        if abs(x1 - x0) < 1e-15:
            break
        x0 = x1 
    return(x0)

#
# log fucntion
# compute log(2)
#

n = 500
log1 = 0
for i in range(1, n+1):
    log2 = log1 + (1/i) * ((-1)**(i+1))
    print(log2)
    log1 = log2
print(log2)

# compute log(x)
# 

def log(x):
    n = 500
    z = (x - 1) / (x + 1)
    plus = 0
    for i in range(n):
        plus += z**(2*i + 1) / (2*i + 1)
    log = 2 * plus
    return log

#
# pi.py
# compute pi
#
# Compute pi using Monte Carlo Method
#

import random

def calc_pi(n):
    count = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        dsq = x**2 + y**2
        if  dsq < 1:
            count += 1
    pi = 4*count/n

    return pi

#
# dlog.py
# compute log(x)
#
def dlog(x):
    h = 10**(-5)
    dlog = (log(x + h) - log(x - h)) / 2*h
    return dlog

#
# green.py
# lower sum of the function y = x**2

def green(n):
    total1 = 0
    h = 1 / n
    for k in range(1, n):
        x = h * ((k-1)*h)**2
        total1 += x
    return total1

print(green(10))
print(green(100))
print(green(1000))

# 구간의 개수가 늘어날수록 1/3에 근접한다.

#
# orange.py
# upper sum of the function y = x**2

def orange(n):
    total2 = 0
    h = 1 / n
    for k in range(1, n):
        x = h * (k*h)**2
        total2 += x
    return total2

print(orange(10))
print(orange(100))
print(orange(1000))

# 구간의 개수가 늘어날수록 1/3에 근접한다.