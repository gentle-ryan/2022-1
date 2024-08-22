#
# plot.py
#
# 실습03 컴퓨터의 개념 및 실습 수업용 파일입니다.
# 언어학과, 2021-12659 박유나가 작성하였습니다.
#

import matplotlib.pyplot
import math

matplotlib.pyplot.plot([1, 2, 3], [4, 7, 2])
matplotlib.pyplot.plot([1, 2, 3], [3, 6, 4])
matplotlib.pyplot.show()

#
# plot
#
# xmin < x < xmax
# n : number of intervals

def f(x):
    return 3*x**3 - x**2 + 3*x + 1

n = 100
xmin = -2
xmax = 3

xs = []
ys = []
for i in range(0, n+1):
    x = xmin + (xmax - xmin) * i/n
    y = f(x)
    xs.append(x)
    ys.append(y)

matplotlib.pyplot.plot(xs, ys)
matplotlib.pyplot.show()

#
# circle
#
# x**2 + y**2 - 1
# x = cos(t)
# y = sin(t)
# 0 <= t <= 2pi

n = 40

xs = []
ys = []
for i in range(0, n+1):
    t = 2 * math.pi * i/n
    x = math.cos(t)
    y = math.sin(t)
    xs.append(x)
    ys.append(y)

matplotlib.pyplot.plot(xs, ys)
matplotlib.pyplot.show()

#
# normal distribution
#
# -3 <= x <= 3
# 

def normal(x, mean, sd):
    f = (1 / math.sqrt(2*math.pi*sd**2)) * math.exp(-(x - mean)**2 / 2 * sd**2)
    return f

xmin = -3
xmax = 3

xs = []
ys = []

for i in range(0, 101):
    x = xmin + (xmax - xmin) * i/n
    y = normal(x, 0, 1)
    xs.append(x)
    ys.append(y)

matplotlib.pyplot.plot(xs, ys)
matplotlib.pyplot.show()

#
# heart
#
# x = 16sin(t)**3
# y = 13cos(t) - 5cos(t) - 2cos(3t) - cos(4t)
# 0 <= t <= 2pi

xs = []
ys = []

for i in range(0, 101):
    t = 2 * math.pi * i/100
    x = 16*(math.sin(t)**3)
    y = 13*math.cos(t) - 5*math.cos(2*t) - 2*math.cos(3*t) - math.cos(4*t)
    xs.append(x)
    ys.append(y)

matplotlib.pyplot.plot(xs, ys)
matplotlib.pyplot.show()

#
# bmi
#
# x = weight
# y = height
# 20 <= x <= 120

def height(w, bmi):
    h = math.sqrt(w / bmi)
    return h

bmi = [18.5, 25, 30, 35, 40]
xmin = 20
xmax = 120

for i in bmi:
    xs = []
    ys = []
    for j in range(0, 101):
        x = xmin + (xmax - xmin) * j/100
        y = height(x, i)
        xs.append(x)
        ys.append(y)
    matplotlib.pyplot.plot(xs, ys)

matplotlib.pyplot.show()
