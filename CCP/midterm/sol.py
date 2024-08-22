#
# sol.py
#
# 박유나
# 언어학과, 2021-12659
#
import midterm
import smath

def sqrt(a, n):
    x = a**n
    return x

def answer_calc():
    ans = sqrt(2, 64)
    return ans

def answer_log():
    import math
    ans = math.log10(sqrt(2022, 2022))
    ans = int(ans)
    return ans

def answer_index():
    a = str(sqrt(2022, 2022))
    b = sqrt(10, 99) -1
    ans = int(a[b])
    return ans

    
def answer_chargram():
    s = midterm.chargram('chargram')
    ans = s.split()[236]
    return ans
    
def answer_csv():
    s = midterm.csv('csv')
    ans = len(s.split(','))
    return ans
    
def answer_data():
    x = midterm.data('data')
    ans = x[0]
    return ans
    
def answer_sum():
    x = midterm.data("sum")
    ans= smath.sum(x)
    return ans

def answer_max():
    x = midterm.data("max")
    ans = smath.max(x)
    return ans

def answer_logsum():
    x = midterm.data('logsum')
    logx = smath.log(x)
    ans = smath.sum(logx)
    return ans

def answer_seqlen():
    start = 1
    end = 2
    n = 100
    xs = smath.seqlen(start, end, n)
    logxs = smath.log(xs)
    ans = smath.sum(logxs)
    return ans

def answer_wordlen():
    text = midterm.chargram('wordlen')
    words = text.split()
    total = 0
    for word in words:
        a = len(word)
        total += a
    ans = total / len(words)
    return ans

def answer_effect():
    import finance

    nominal_rate = 0.03
    npery = 4
    ans = finance.effect(nominal_rate, npery)
    
    return ans


def answer_chr():
    start = 0xac00
    end = 0xacff
    s = ''
    for i in range(start, end + 1):
        a = chr(i)
        s += a 
    return s

def answer_diagtext():
    file = open("pp/diagtext.txt")
    s= ''
    for i, line in enumerate(file):
        s += line[i]
    return s

def answer_aprcommit():
    file = open("pp/cpython-log.txt")
    count = 0
    for a in file:
        line = a.strip().split()
        if line[0].startswith('Date'):
            if 'Apr' in line:
                count += 1
    return count
