import math

def sum(x):
    total = 0
    for i in x:
        total += i
    return total

def max(x):
    max = 0
    for i in x:
        if i > max:
            max = i
        else:
            pass
    return max

def log(x):
    xs = []
    for i in x:
        a = math.log(i)
        xs.append(a)
    return xs

def seqlen(s, e, n):
    xs = []
    for i in range(n):
        if i == 0:
            xs.append(i)[0]
        else:    
            a = e / i
            xs.append(a)[1]
    return xs